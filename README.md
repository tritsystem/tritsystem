# Hi, I'm Gavin 👋

I research **ML security and low-level systems security**. I find memory-safety, correctness and isolation bugs in machine-learning libraries and in the native code underneath them, reproduce each one through the real target, fix it upstream, and build the tools and study material that make the next one faster to find and easier to check.

**[Portfolio: the work, how I learn, and how it all connects](https://tritsystem.github.io/research-portfolio/)** · [Security track record](https://tritsystem.github.io/sec-portfolio/) · [The Method](https://github.com/tritsystem/research-portfolio/blob/main/METHOD.md) · [LinkedIn](https://www.linkedin.com/in/gavin-branaa-a23448170/)

## The record

As of 2026-11-04, from a snapshot of every pull request I've authored in other people's repositories (98 across 54 repos):

- **35 merged** fixes and features across 16 projects. That's 71% of the 49 that have been decided (95% interval 58–82%), with a median of 3.4 days from opening to merge. The other 49 are still open, and I count them as undecided, not failed.
- **1 published security advisory:** [GHSA-gvp8-978c-rx2q](https://github.com/advisories/GHSA-gvp8-978c-rx2q) / CVE-2026-103001. `PyJWT.decode()` mutated the caller's `options` dict, so a reused dict could silently switch off claim verification.
- **Memory safety and systems:** use-after-free and double free in [cfengine](https://github.com/cfengine/core/pull/6358), a leak and NULL dereference in [DeepSpeed's native shared-memory init](https://github.com/deepspeedai/DeepSpeed/pull/8565), allocation-failure and nftables/netlink fixes in [miniupnp](https://github.com/miniupnp/miniupnp/pulls?q=is%3Apr+author%3Atritsystem+is%3Amerged), and an authorization-boundary fix in [Woodpecker CI](https://github.com/woodpecker-ci/woodpecker/pull/7365).
- **ML correctness:** silent precision loss, broken gradients, cross-sample leakage and state that doesn't follow `.to()`, in kornia, MONAI, timm, transformers, NVIDIA Model-Optimizer, llm-compressor, librosa, snntorch and SpikingJelly.
- **In review:** GPU out-of-bounds write and read in bitsandbytes' 4-bit path, shown with compute-sanitizer, with the severity measured rather than assumed ([write-up](https://tritsystem.github.io/bitsandbytes-4bit-memory-safety/)).

Only merged work counts. The table below is regenerated daily from the GitHub API by [a workflow](.github/workflows/oss-status.yml): it finds every merged PR I've authored and re-verifies each one before listing it.

<!-- OSS-STATUS:START -->
**35 merged &middot; 7 reported &amp; fixed upstream** &middot; refreshed 2026-11-04 10:31 UTC

| Repo | # | What | Status |
|---|---|---|---|
| [miniupnp](https://github.com/miniupnp/miniupnp) | [#941](https://github.com/miniupnp/miniupnp/pull/941) | netfilter_nft: keep the netlink socket in sync when a rule-cache re... | Merged 2026-11 |
| [miniupnp](https://github.com/miniupnp/miniupnp) | [#942](https://github.com/miniupnp/miniupnp/pull/942) | upnphttp: check malloc() when sending the 100 Continue response | Merged 2026-11 |
| [miniupnp](https://github.com/miniupnp/miniupnp) | [#923](https://github.com/miniupnp/miniupnp/pull/923) | miniupnpd/netfilter: create DNAT rules with the kernel's highest re... | Merged 2026-11 |
| [miniupnp](https://github.com/miniupnp/miniupnp) | [#925](https://github.com/miniupnp/miniupnp/pull/925) | miniupnpd/nftables: keep the remote host of IPv4 port mappings | Merged 2026-10 |
| [miniupnp](https://github.com/miniupnp/miniupnp) | [#922](https://github.com/miniupnp/miniupnp/pull/922) | miniupnpd/netfilter: check calloc() results in iptables rule builders | Merged 2026-10 |
| [woodpecker](https://github.com/woodpecker-ci/woodpecker) | [#7365](https://github.com/woodpecker-ci/woodpecker/pull/7365) | Harden store scoping for org-level secret and registry retrieval | Merged 2026-10 |
| [transformers](https://github.com/huggingface/transformers) | [#49767](https://github.com/huggingface/transformers/pull/49767) | Fix background_color handling across DeepSeek-VL and Janus image pr... | Merged 2026-10 |
| [pytorch-image-models](https://github.com/huggingface/pytorch-image-models) | [#2849](https://github.com/huggingface/pytorch-image-models/pull/2849) | Fix features_only backward with grad checkpointing for in-place ste... | Merged 2026-10 |
| [llm-compressor](https://github.com/vllm-project/llm-compressor) | [#3252](https://github.com/vllm-project/llm-compressor/pull/3252) | [Quantization] Flag layers narrower than group_size in the early gr... | Merged 2026-10 |
| [MONAI](https://github.com/Project-MONAI/MONAI) | [#9104](https://github.com/Project-MONAI/MONAI/pull/9104) | fix(networks): AffineHead follows the module's dtype, not just device | Merged 2026-10 |
| [pytorch-image-models](https://github.com/huggingface/pytorch-image-models) | [#2848](https://github.com/huggingface/pytorch-image-models/pull/2848) | Fix GCViT global query mixing images within a batch | Merged 2026-10 |
| [Model-Optimizer](https://github.com/NVIDIA/Model-Optimizer) | [#2651](https://github.com/NVIDIA/Model-Optimizer/pull/2651) | Export unquantized FP8Linear layers in the export dtype, not fp32 | Merged 2026-10 |
| [MONAI](https://github.com/Project-MONAI/MONAI) | [#9103](https://github.com/Project-MONAI/MONAI/pull/9103) | fix(losses): BarlowTwinsLoss preserves float16/bfloat16 input dtype | Merged 2026-10 |
| [librosa](https://github.com/librosa/librosa) | [#2106](https://github.com/librosa/librosa/pull/2106) | Preserve float32 in spectral features; add dtype= to frequency cons... | Merged 2026-09 |
| [snntorch](https://github.com/jeshraghian/snntorch) | [#454](https://github.com/jeshraghian/snntorch/pull/454) | Add homeostasis: adaptive, time-varying threshold on SpikingNeuron | Merged 2026-09 |
| [ansible](https://github.com/ansible/ansible) | [#87503](https://github.com/ansible/ansible/pull/87503) | vars: copy facts in set_host_facts() to stop cross-host fact aliasi... | Merged 2026-09 |
| [core](https://github.com/cfengine/core) | [#6358](https://github.com/cfengine/core/pull/6358) | Fix use-after-free and double-free in RemoveFilament | Merged 2026-09 |
| [kornia](https://github.com/kornia/kornia) | [#4361](https://github.com/kornia/kornia/pull/4361) | fix(geometry): render_gaussian2d pixel-coordinate linspace built at... | Merged 2026-09 |
| [kornia](https://github.com/kornia/kornia) | [#4360](https://github.com/kornia/kornia/pull/4360) | fix(enhance): image_histogram2d bin centers built at image.dtype | Merged 2026-09 |
| [DeepSpeed](https://github.com/deepspeedai/DeepSpeed) | [#8565](https://github.com/deepspeedai/DeepSpeed/pull/8565) | Fix memory leak and NULL-deref in shm_initialize | Merged 2026-09 |
| [snntorch](https://github.com/jeshraghian/snntorch) | [#455](https://github.com/jeshraghian/snntorch/pull/455) | Add neuron_from_equations(): generate a custom neuron class from st... | Merged 2026-09 |
| [snntorch](https://github.com/jeshraghian/snntorch) | [#453](https://github.com/jeshraghian/snntorch/pull/453) | Add SynapticDelay: per-channel axonal/synaptic delay with a learnab... | Merged 2026-09 |
| [snntorch](https://github.com/jeshraghian/snntorch) | [#441](https://github.com/jeshraghian/snntorch/pull/441) | Fix LeakyParallel silently ignoring a per-neuron beta; correct the ... | Merged 2026-09 |
| [kornia](https://github.com/kornia/kornia) | [#4359](https://github.com/kornia/kornia/pull/4359) | fix(feature): CoarseMatching training-mode gt-padding crash + dtype... | Merged 2026-09 |
| [kornia](https://github.com/kornia/kornia) | [#4336](https://github.com/kornia/kornia/pull/4336) | fix(geometry): bbox_to_mask position grid is exact at any image size | Merged 2026-09 |
| [kornia](https://github.com/kornia/kornia) | [#4337](https://github.com/kornia/kornia/pull/4337) | fix(augmentation): register fill_value/sigma as buffers, not plain ... | Merged 2026-09 |
| [ultralytics](https://github.com/ultralytics/ultralytics) | [#26075](https://github.com/ultralytics/ultralytics/pull/26075) | Remove stale SAM3 decoder coordinate caches | Merged 2026-09 |
| [celery](https://github.com/celery/celery) | [#10571](https://github.com/celery/celery/pull/10571) | Fix Signature.clone() sharing kwargs with the original signature | Merged 2026-09 |
| [kornia](https://github.com/kornia/kornia) | [#4319](https://github.com/kornia/kornia/pull/4319) | fix(feature): register RenderingDeFMO's times as a buffer so .to() ... | Merged 2026-09 |
| [kornia](https://github.com/kornia/kornia) | [#4303](https://github.com/kornia/kornia/pull/4303) | fix(geometry): bbox_to_mask3d intersects axis ranges for a full/ove... | Merged 2026-09 |
| [kornia](https://github.com/kornia/kornia) | [#4299](https://github.com/kornia/kornia/pull/4299) | fix(geometry): finite gradients for solve_cubic at its acos boundary | Merged 2026-09 |
| [spikingjelly](https://github.com/fangwei123456/spikingjelly) | [#744](https://github.com/fangwei123456/spikingjelly/pull/744) | Fix MSTDPLearner initialising eligibility without a dtype | Merged 2026-09 |
| [spikingjelly](https://github.com/fangwei123456/spikingjelly) | [#750](https://github.com/fangwei123456/spikingjelly/pull/750) | Add RAFNode: resonate-and-fire neuron | Merged 2026-09 |
| [kornia](https://github.com/kornia/kornia) | [#4210](https://github.com/kornia/kornia/pull/4210) | fix(augmentation): auto-augment ops preserve float16 / bfloat16 inp... | Merged 2026-09 |
| [spikingjelly](https://github.com/fangwei123456/spikingjelly) | [#743](https://github.com/fangwei123456/spikingjelly/pull/743) | Move tensor reset values with the module in MemoryModule._apply | Merged 2026-09 |
| [compressed-tensors](https://github.com/vllm-project/compressed-tensors) | [#920](https://github.com/vllm-project/compressed-tensors/issues/920) | Group quantization of a layer with fewer columns than group_size fa... | Reported; fixed upstream by antar-ghuman ([#924](https://github.com/vllm-project/compressed-tensors/pull/924), merged 2026-10) |
| [sentence-transformers](https://github.com/huggingface/sentence-transformers) | [#4185](https://github.com/huggingface/sentence-transformers/issues/4185) | v6: models with `Normalize` at the model root (path "" in modules.j... | Reported; fixed upstream by tomaarsen ([#4190](https://github.com/huggingface/sentence-transformers/pull/4190), merged 2026-10) |
| [compressed-tensors](https://github.com/vllm-project/compressed-tensors) | [#919](https://github.com/vllm-project/compressed-tensors/issues/919) | [Convert] ModelOptNvfp4Converter with default/"Linear" targets rela... | Reported; fixed upstream by mottopanikeiku ([#926](https://github.com/vllm-project/compressed-tensors/pull/926), merged 2026-10) |
| [superset](https://github.com/apache/superset) | [#43918](https://github.com/apache/superset/issues/43918) | Dataset 'Refresh columns' (fetch_metadata) doesn't bump changed_on,... | Reported; fixed upstream by gps23 ([#43921](https://github.com/apache/superset/pull/43921), merged 2026-09) |
| [Pillow](https://github.com/python-pillow/Pillow) | [#9963](https://github.com/python-pillow/Pillow/issues/9963) | Image.copy() aliases mutable .info values (e.g. list-valued "Commen... | Reported; fixed upstream by Andrew Murray ([#9964](https://github.com/python-pillow/Pillow/pull/9964), merged 2026-09) |
| [aiohttp](https://github.com/aio-libs/aiohttp) | [#13634](https://github.com/aio-libs/aiohttp/issues/13634) | CookieJar.update_cookies() aliases a caller-supplied Morsel instead... | Reported; fixed upstream by Sam Bull ([#13637](https://github.com/aio-libs/aiohttp/pull/13637), merged 2026-09) |
| [scipy](https://github.com/scipy/scipy) | [#26095](https://github.com/scipy/scipy/issues/26095) | BUG: scipy.optimize.milp() silently mutates the caller's options di... | Reported; fixed upstream by j-bowhay ([#26097](https://github.com/scipy/scipy/pull/26097), merged 2026-09) |
<!-- OSS-STATUS:END -->

## Low-level systems

- **[spikeling-os](https://github.com/tritsystem/spikeling-os)**: a from-scratch x86_64 kernel (Rust) with its own filesystem, ELF loader, processes and an in-kernel subset-C compiler. Every milestone is verified by two QEMU boots and hand-computed self-tests. Differential fuzzing of the compiler found and fixed real silent miscompiles: 64-bit literals and case labels truncated to 32 bits, and a `continue` inside a switch that had been dropped for 75 milestones.
- **[Native seam audit](https://github.com/tritsystem/ml-security-curriculum/tree/main/Native%20Seam%20Audit)**: a procedure for the Python-to-C/C++/CUDA boundary of ML libraries. Each of its 9 sanitizer and fuzzer configurations is validated on a planted bug before it's trusted, and the blind spots are recorded.
- **[pytest-numba-cache](https://github.com/tritsystem/pytest-numba-cache)**: fixes a parallel cache-write race. Crashes fell from 8 of 10 rounds to 0 of 10 (measured on Windows).
- **[baton](https://github.com/tritsystem/baton)**: three LoRA adapters on one frozen model with pre-filled KV caches, hardened against a cache-position bug that ended in a CUDA device-side assert.

## ML research

Pre-registered studies with bounded or negative results, reported as such.

- **[Spikeling](https://github.com/tritsystem/Spikeling)**: one spiking-network description runs on Python, C, Verilog and GDScript backends. Event-driven execution was 16–29× faster at low activity, but its resonator neuron didn't beat Goertzel or FFT.
- **Heterogeneous neuron ensembles**: a mixed-type ensemble beat all-LIF 60/60 vs 30/60 in Python ([study](https://github.com/tritsystem/heterogeneous-neuron-ontology)). Its kernel port went through a full retraction (a false positive), then a measured 29/32 vs 12/32.
- **[OBSERVE / ternary weights](https://github.com/tritsystem/012-trit-search)**: 20× compression for 7.35 points of accuracy. Local semantic code search that grep still beats when you know the identifier.
- **[methodlm](https://github.com/tritsystem/methodlm)**: a causal-reasoning harness that cut false causal claims from 100% to about 1%. **[topological-phononics](https://github.com/tritsystem/topological-phononics)** ([preprint](https://doi.org/10.5281/zenodo.21305151)): topological protection holds exactly when chiral symmetry does, and the idealized gain doesn't transfer to hardware.

## Tools I built for the hunt

- **[reagent](https://github.com/tritsystem/reagent)**: 40 bug detectors (32 Python, 8 C) that nominate code from AST patterns, then confirm by running it.
- **[crawlspike](https://github.com/tritsystem/crawlspike)**: a crawler for "one path honors a flag, its sibling drops it". On real OSS so far it has found 5 bugs in itself and 0 in its targets, and it says so.
- **[sec-portfolio](https://github.com/tritsystem/sec-portfolio)**: the track record, regenerated from the real merged diffs with no model in the loop.

## How I learn

- **[The Method](https://github.com/tritsystem/research-portfolio/blob/main/METHOD.md)**: measure, don't infer; validate the instrument on a planted case first; pre-register the verdict; report the worst slice; retract overclaims by name.
- **An evidence ladder, T0 to T5**: from a grep hit to a fix whose sibling code has been searched and guarded. A finding needs T3 (reproduced through the real target), I file at T4, and I never round up.
- **Study material**: an [ML systems security curriculum](https://github.com/tritsystem/ml-security-curriculum) (262 checked links, an 8-hour course, threat models), the [ML memory ladder](https://tritsystem.github.io/ml-memory-ladder/) (16 C++/Python labs, each built on a real bug I fixed), the [ML ladder](https://tritsystem.github.io/ml-ladder/), and [the playbook](https://tritsystem.github.io/the-playbook/).
- **A private research vault**: every result is logged the same day, negatives included (575 work notes, 120 lessons). Mistakes become lessons, and lessons become the rules I check before any outward action.

The [portfolio page](https://tritsystem.github.io/research-portfolio/#map) maps how these connect: the curriculum teaches the evidence ladder, the ladder governs the audits, the audits produce fixes, and the fixes become labs in the memory ladder.

<sub>I use an AI coding assistant heavily for reproducing, testing and drafting. Every claim here is checked against the public record, and findings still under coordinated disclosure are deliberately left out.</sub>
