#!/usr/bin/env python3
"""Refresh the live open-source contribution status table in README.md.

Queries the GitHub REST API for every tracked PR/issue and rewrites the
table between the OSS-STATUS markers. No hand-typed status ever goes stale:
this script (run daily by .github/workflows/oss-status.yml) is the only
thing that writes that block.
"""
import json
import os
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone

TRACKED = [
    ("fangwei123456/spikingjelly", 743, "pr"),
    ("fangwei123456/spikingjelly", 744, "pr"),
    ("fangwei123456/spikingjelly", 745, "pr"),
    ("fangwei123456/spikingjelly", 750, "pr"),
    ("jeshraghian/snntorch", 441, "pr"),
    ("Brainchip-Inc/tenns-core", 1, "pr"),
    ("reservoirpy/reservoirpy", 245, "pr"),
    ("stefanonardo/pytorch-esn", 27, "pr"),
    ("huggingface/transformers", 48509, "pr"),
    ("pytorch/audio", 4228, "pr"),
    ("kornia/kornia", 4210, "pr"),
    ("lucidrains/rotary-embedding-torch", 50, "pr"),
    ("lucidrains/perceiver-pytorch", 70, "pr"),
    ("lucidrains/vit-pytorch", 373, "pr"),
    ("librosa/librosa", 2099, "issue"),
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


def status_for_pr(data):
    if data.get("merged"):
        return 0, "Merged"
    if data["state"] == "closed":
        return 5, "Closed, not merged"
    if data.get("draft"):
        return 2, "Draft"
    ms = (data.get("mergeable_state") or "unknown").lower()
    label = {
        "clean": "Open - checks clean, awaiting review",
        "unstable": "Open - CI issue",
        "blocked": "Open - awaiting review",
        "dirty": "Open - merge conflicts",
        "behind": "Open - behind base branch",
    }.get(ms, "Open")
    return 1, label


def status_for_issue(data):
    if data["state"] == "closed":
        return 4, "Issue closed"
    return 3, "Issue open, no PR yet"


def fetch_row(repo, number, kind):
    try:
        if kind == "pr":
            data = api_get(f"/repos/{repo}/pulls/{number}")
            rank, label = status_for_pr(data)
        else:
            data = api_get(f"/repos/{repo}/issues/{number}")
            rank, label = status_for_issue(data)
        title = data.get("title", "?")
        url = data.get("html_url", "")
    except urllib.error.HTTPError as e:
        rank, label = 6, f"couldn't check (HTTP {e.code})"
        title = "?"
        kind_path = "pull" if kind == "pr" else "issues"
        url = f"https://github.com/{repo}/{kind_path}/{number}"
    return {
        "rank": rank,
        "repo": repo,
        "number": number,
        "kind": kind,
        "title": title,
        "url": url,
        "label": label,
    }


def build_table():
    rows = [fetch_row(repo, number, kind) for repo, number, kind in TRACKED]
    rows.sort(key=lambda r: (r["rank"], r["repo"], r["number"]))

    merged = sum(1 for r in rows if r["rank"] == 0)
    open_prs = sum(1 for r in rows if r["kind"] == "pr" and r["rank"] not in (0, 5))

    lines = [
        f"**{merged} merged &middot; {open_prs} open PR{'s' if open_prs != 1 else ''}** "
        f"&middot; refreshed {datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC",
        "",
        "| Repo | # | What | Status |",
        "|---|---|---|---|",
    ]
    for r in rows:
        short_repo = r["repo"].split("/")[-1]
        title = r["title"].replace("|", "\\|")
        if len(title) > 70:
            title = title[:67] + "..."
        repo_url = f"https://github.com/{r['repo']}"
        lines.append(f"| [{short_repo}]({repo_url}) | [#{r['number']}]({r['url']}) | {title} | {r['label']} |")
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
