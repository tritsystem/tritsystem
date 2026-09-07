#!/usr/bin/env python3
"""Refresh the live open-source contribution status table in README.md.

Queries the GitHub REST API for every tracked PR/issue and rewrites the
table between the OSS-STATUS markers. This table lists ONLY what has
actually landed:

  * pull requests authored here that were **merged**, and
  * bugs reported here (issue, no authored PR) that a maintainer then
    fixed -- rendered only when the crediting PR is itself merged.

Everything still in review lives in the full audited record at
research-portfolio/oss. No hand-typed status: this script (run daily by
.github/workflows/oss-status.yml) is the only thing that writes the block,
and every row it emits is re-verified against the API on each run.
"""
import json
import os
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone

# (repo, number) -- PRs authored here. Rendered only if currently merged.
# Kept in the list after merging so the row stays; kept before merging so a
# later merge appears automatically.
AUTHORED = [
    ("fangwei123456/spikingjelly", 743),
    ("fangwei123456/spikingjelly", 744),
    ("fangwei123456/spikingjelly", 745),
    ("fangwei123456/spikingjelly", 750),
    ("kornia/kornia", 4210),
    ("kornia/kornia", 4299),
    ("kornia/kornia", 4303),
    ("kornia/kornia", 4319),
    ("kornia/kornia", 4336),
    ("kornia/kornia", 4337),
    ("jeshraghian/snntorch", 441),
    ("SynSense/sinabs", 336),
    ("Brainchip-Inc/tenns-core", 1),
    ("reservoirpy/reservoirpy", 245),
    ("stefanonardo/pytorch-esn", 27),
    ("huggingface/transformers", 48509),
    ("pytorch/audio", 4228),
    ("lucidrains/rotary-embedding-torch", 50),
    ("lucidrains/perceiver-pytorch", 70),
    ("lucidrains/vit-pytorch", 373),
    ("lucidrains/denoising-diffusion-pytorch", 370),
    ("lucidrains/video-diffusion-pytorch", 40),
    ("lucidrains/imagen-pytorch", 392),
    ("ultralytics/ultralytics", 26075),
    ("celery/celery", 10571),
]

# (repo, reported_issue, fixing_pr, credited_to) -- a bug reported here as an
# issue that a maintainer then fixed with their own PR. Rendered only if the
# fixing PR is currently merged (verified live, never asserted).
FIXED_UPSTREAM = [
    ("python-pillow/Pillow", 9963, 9964, "Andrew Murray"),
    ("aio-libs/aiohttp", 13634, 13637, "Sam Bull"),
    ("scipy/scipy", 26095, 26097, "j-bowhay"),
    ("jeshraghian/snntorch", 430, 418, "maintainers"),
]

TOKEN = os.environ.get("GITHUB_TOKEN", "")
README_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "README.md")

START_MARKER = "<!-- OSS-STATUS:START -->"
END_MARKER = "<!-- OSS-STATUS:END -->"


def api_get(path):
    req = urllib.request.Request(
        f"https://api.github.com{path}",
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "oss-status-script",
            **({"Authorization": f"Bearer {TOKEN}"} if TOKEN else {}),
        },
    )
    with urllib.request.urlopen(req, timeout=20) as resp:
        return json.loads(resp.read())


def _month(iso):
    if not iso:
        return ""
    return datetime.fromisoformat(iso.replace("Z", "+00:00")).strftime("%Y-%m")


def _short(title, n=70):
    title = (title or "?").replace("|", "\\|")
    return title if len(title) <= n else title[: n - 3] + "..."


def authored_rows():
    """Merged authored PRs, most-recent first."""
    rows = []
    for repo, number in AUTHORED:
        try:
            d = api_get(f"/repos/{repo}/pulls/{number}")
        except urllib.error.HTTPError as e:
            print(f"  ! {repo}#{number}: HTTP {e.code}", file=sys.stderr)
            continue
        if not d.get("merged"):
            continue
        rows.append(
            {
                "sort": d.get("merged_at") or "",
                "repo": repo,
                "number": number,
                "url": d.get("html_url", f"https://github.com/{repo}/pull/{number}"),
                "what": _short(d.get("title")),
                "status": f"Merged {_month(d.get('merged_at'))}".rstrip(),
            }
        )
    rows.sort(key=lambda r: r["sort"], reverse=True)
    return rows


def fixed_upstream_rows():
    """Reported-then-fixed bugs whose crediting PR is merged."""
    rows = []
    for repo, issue_no, pr_no, who in FIXED_UPSTREAM:
        try:
            pr = api_get(f"/repos/{repo}/pulls/{pr_no}")
        except urllib.error.HTTPError as e:
            print(f"  ! {repo}#{pr_no}: HTTP {e.code}", file=sys.stderr)
            continue
        if not pr.get("merged"):
            continue
        try:
            issue = api_get(f"/repos/{repo}/issues/{issue_no}")
            what = _short(issue.get("title"))
        except urllib.error.HTTPError:
            what = _short(pr.get("title"))
        rows.append(
            {
                "sort": pr.get("merged_at") or "",
                "repo": repo,
                "number": issue_no,
                "url": f"https://github.com/{repo}/issues/{issue_no}",
                "what": what,
                "status": (
                    f"Reported; fixed upstream by {who} "
                    f"([#{pr_no}]({pr.get('html_url')}), merged {_month(pr.get('merged_at'))})"
                ),
            }
        )
    rows.sort(key=lambda r: r["sort"], reverse=True)
    return rows


def build_table():
    merged = authored_rows()
    fixed = fixed_upstream_rows()

    header = (
        f"**{len(merged)} merged &middot; {len(fixed)} reported &amp; fixed upstream** "
        f"&middot; refreshed {datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC"
    )
    lines = [header, "", "| Repo | # | What | Status |", "|---|---|---|---|"]
    for r in merged + fixed:
        short_repo = r["repo"].split("/")[-1]
        repo_url = f"https://github.com/{r['repo']}"
        lines.append(
            f"| [{short_repo}]({repo_url}) | [#{r['number']}]({r['url']}) | {r['what']} | {r['status']} |"
        )
    return "\n".join(lines)


def main():
    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    pattern = re.compile(re.escape(START_MARKER) + r".*?" + re.escape(END_MARKER), re.DOTALL)
    if not pattern.search(content):
        print("OSS-STATUS markers not found in README.md", file=sys.stderr)
        sys.exit(1)

    new_block = f"{START_MARKER}\n{build_table()}\n{END_MARKER}"
    updated = pattern.sub(lambda _: new_block, content)

    if updated != content:
        with open(README_PATH, "w", encoding="utf-8") as f:
            f.write(updated)
        print("README.md updated")
    else:
        print("No change")


if __name__ == "__main__":
    main()
