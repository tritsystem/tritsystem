# Hi, I'm Gavin 👋

Independent researcher working at the edge of **unconventional computing** —
ternary and neuromorphic architectures, physical (phononic) reservoirs, and what
happens when you put those ideas inside real software and games.

I build things, measure them honestly, and write down the negative results too.

[LinkedIn](https://www.linkedin.com/in/gavin-branaa-a23448170/)

## 🚀 Production infrastructure
Real, deployed, live services — not demos.
- **[OBSERVE Search API](https://api.observe-search.online/)** *(live product — [source](https://github.com/tritsystem/observe-api))* — a hosted, pay-per-query semantic code search API for AI agents, plus a real ACP (OpenAI/Stripe) and Google UCP-compatible agent-commerce discovery and reputation layer. Read both protocol specs directly before building, since neither one actually defines cross-merchant discovery — that gap is the product. Real Stripe billing, a live production deployment (Caddy, TLS, a reverse-proxied host), and a two-sided reputation system where trust is earned agreement between disconnected buyer/seller keys instead of a self-report. Same honest-negative-results discipline as the research below: three retrieval techniques borrowed from a competing tool were tested against its own corpus and measured net negative, documented instead of dropped quietly.
- **[mcp-gateway](https://github.com/tritsystem/mcp-gateway)** *(private)* — a self-contained, tamper-evident audit log (hash-chained JSONL) plus rate limiting for local MCP tool servers, wired into both OBSERVE's and Spikeling's MCP tool surfaces so every tool call is logged and rate-bounded, single-operator scope, no cloud dependency.
- **[server-guard](https://github.com/tritsystem/server-guard)** — real-time server monitoring and alerting, benchmarked head-to-head against Datadog, Wazuh, PagerDuty, and Netdata on sourced, cited pricing rather than marketing claims.
- **[spikeling-os](https://github.com/tritsystem/spikeling-os)** — a from-scratch x86_64 kernel whose task scheduler is driven by a spiking neural network — the same Spikeling runtime below, running as real kernel-level control logic instead of a simulation of one.

## 🔬 Research

**Ternary & neuromorphic computing**
- **[012-trit-search](https://github.com/tritsystem/012-trit-search)** — ternary-computing research, and its shipping product **OBSERVE**: local, private semantic code search (desktop GUI / CLI / MCP server) with a one-line install. Nothing leaves your machine. Now includes a chunk-provenance/lineage layer (tracks a chunk's edit history across commits), hybrid (lexical + semantic) search, and an incremental indexer so re-indexing a repo only touches what changed.
- **[methodlm](https://github.com/tritsystem/methodlm)** — a verifiable causal-reasoning harness: pre-registers every test, runs real backdoor adjustment (with a robustness value), and keeps an honest ledger so any LLM must *prove* its causal claims. A new REFUTE tool runs DoWhy-backed causal refutation (placebo treatment, random common cause, subset validation) against every accepted claim, and a real-world benchmark suite now covers 10 cited public datasets plus this portfolio's own live server-guard telemetry. Optional ternary second witness via the same `tritkit` readout as OBSERVE.
- **[Spikeling](https://github.com/tritsystem/Spikeling)** — a DSL + runtime for spiking neural networks that runs the *same* `.spk` brain on Python, C, Verilog, and Godot backends. Ships a Godot game-AI plugin, an MCP server exposing the runtime as agent tools, and a real hardware sensor-adapter layer (acoustic, system telemetry, video confirmed against physical devices).
- **[llama-demo](https://github.com/tritsystem/llama-demo)** — genuinely free (Ollama, $0 API cost) local-model experiments applying methodlm's causal-reasoning discipline to LLM tooling: a local coding-agent dispatcher, model vet/quantize/finetune scripts, and honest negative results (a local 7B model failed to fix a real bug even when handed the exact correct lesson).

**Phononic / MEMS reservoir computing**
- **[quasicrystal-mems-reservoir](https://github.com/tritsystem/quasicrystal-mems-reservoir)** — finite-element study of quasicrystal-perforated MEMS resonators, and what their mode structure can (and cannot) compute as a physical reservoir. Includes the paper.
- **[symmetry-selection-rule](https://github.com/tritsystem/symmetry-selection-rule)** — a symmetry selection rule for computation in those reservoirs.
- **[topological-phononics](https://github.com/tritsystem/topological-phononics)** — does topological structure make an analog (SSH) reservoir tolerate a dead element? A pre-registered, honestly-scoped simulation study — boundary conditions and negative results reported as carefully as the positives.

## 🎮 Games (built on the same spiking-brain engine)
Both are in active testing — expect bugs, and some builds may not be playable end-to-end.
- **[tribe](https://github.com/tritsystem/tribe)** — a survival/RTS sim where every NPC (tribe members, animals, rival AI) is driven by a small spiking neural network instead of a behavior tree.
- **[horde-defense-beta](https://github.com/tritsystem/horde-defense-beta)** — a 3D horde-defense game with a deck-building creep system.

## 🛠️ Applied builds
Practical prototypes for real hardware, held to the same standard as the
research above: verify it actually works before calling it done.
- **[doorcam](https://github.com/tritsystem/doorcam)** — a regular USB webcam becomes a driveway monitor: YOLOv8 person/vehicle detection restricted to a hand-drawn driveway boundary, Discord webhook alerts with snapshots, and a live MJPEG feed built for screen-sharing into Discord via its native Go Live (not a bot faking video, which would violate Discord's ToS).
- **[pond-health](https://github.com/tritsystem/pond-health)** — predicts pond water-quality problems (oxygen crashes, algae blooms) before they're visible and recommends organic fixes. Transparent trend-based prediction rather than a black-box model, since there's no real historical sensor data yet to train one honestly. Every run logs to SQLite, visualized in a Grafana dashboard whose color thresholds are generated straight from the same code the app alerts on. A second detector runs the real Spikeling engine (below) as a spiking neural network alongside the trend predictor — honestly measured against it rather than assumed to be better: it never false-alarms, but gives no early warning, the opposite tradeoff of the trend predictor.
- **[sensor-duo](https://github.com/tritsystem/sensor-duo)** — the trend + spiking + SQLite + Grafana pattern above, extracted into a reusable toolkit after building it by hand twice. Generic over any named numeric channel (a temperature, how long someone's lingered in a camera frame, anything with a float), with a normalized schema so a new channel never needs a migration, and a runnable end-to-end demo proving it outside the pond-specific context it came from.

## 📖 Study guide
- **[the-playbook](https://github.com/tritsystem/the-playbook)** — a self-study reference across this whole portfolio, taught from scratch, every claim a real measured number pulled from the corresponding repo.

## The through-line
Two research threads — neuromorphic and phononic — that keep testing the same
question: **when does structure/symmetry actually *help* computation?** That
question doesn't stay theoretical: the same neuromorphic engine drives two
games and a from-scratch kernel scheduler, and the same discipline — measure
it, verify it, report what actually happened, negative results included —
carries all the way through to production software people can actually pay
for and depend on, not just research code that stops at a benchmark script.
