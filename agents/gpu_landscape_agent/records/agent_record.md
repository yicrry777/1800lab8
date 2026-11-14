# Emerging Technologies Specialist Agent Record

## A. Agent and Version

| Field | Student record |
|---|---|
| Student / team | Student name to be added by repository owner |
| Assignment / specialist agent | Assignment 8 — AI GPU Landscape Agent |
| Date | 2026-11-13 |
| GitHub repository | https://github.com/yicrry777/1800lab8 |
| Branch | `codex/assignment-8-gpu-landscape-agent` |
| Tested candidate commit | `25b2d3d1f11b7848db4757fe6947f8a67987a1fa` |
| Agent version | `1.0-tested` |
| Frozen scaffold version | `MASY1800_ET_Agent_Scaffold_v1_0` |

## B. Specialist Purpose and Context

| Field | Student record |
|---|---|
| Governing analytical question | Where do data-center AI GPU accelerators and credible alternatives sit in the current landscape for this application and organization, and which observable signal should cause management to reassess its position? |
| Emerging technology | Data-center AI GPU accelerators for generative-AI inference |
| Intended application | On-premises RAG assistant for proprietary research, quality, and regulatory documents, with employee review of consequential outputs |
| Organization / industry | Mid-sized U.S. life-sciences company with about 2,500 employees |
| Adoption posture | Conservative fast follower; willing to pilot, unwilling to buy from unverified performance or immature controls |
| Risk / consequence context | Research-IP disclosure, unreliable summaries in regulated workflows, outages, stranded capital, vendor lock-in, and power/cooling overruns |
| Management question / time horizon | Decide now whether to authorize a 12-week benchmark and facilities-assessment pilot; possible procurement within 12 months and a three-year infrastructure life |

## C. Three-Level Finding

| Field | Student record |
|---|---|
| ET generally | Data-center GPUs are mature deployable infrastructure, but the landscape is fluid. Competition includes NVIDIA and AMD GPU systems, AWS Trainium, Google TPU, and incumbent smaller or hosted options. Software ecosystems, system design, access model, and workload-specific evidence are at least as consequential as peak chip specifications. |
| ET for this application | The credible shortlist is an NVIDIA CUDA baseline, one AMD ROCm comparison, one security-approved hosted path, and a lower-complexity CPU or smaller-accelerator baseline if concurrency is low. Compare cost per million accepted tokens at an agreed latency and quality threshold, not peak FLOPS. |
| ET for this application in this organization | Existing CUDA skill favors NVIDIA as the lowest-friction baseline, but limited power/cooling readiness, a small platform team, uncertain utilization, and conservative risk posture argue against immediate ownership. AMD and hosted capacity should remain in a bounded pilot to preserve options. |
| Bounded management implication | Authorize a 12-week evidence-gathering pilot and parallel rack-level facilities assessment. Do not authorize production deployment, vendor selection, or hardware purchase yet. |
| Confidence / uncertainty | High confidence in the landscape structure and the insufficiency of peak specifications; moderate confidence in the staged pilot; low confidence in vendor, capacity, ownership, performance, or cost winner without organization-specific measurements and quotes. |
| Evidence or condition that would change the conclusion | A representative workload, stable high utilization, approved service-level targets, favorable complete-system benchmarks, facilities readiness, and comparable written three-year quotes could support ownership. Low utilization, major facilities work, or a favorable controlled-hosting result would support continued rental or deferral. |

## D. Evidence and Testing

| Field | Student record |
|---|---|
| Most important evidence/source(s) | January 2026 NVIDIA HGX reference architecture; June 2025 AMD MI350X specifications; AWS Trainium2 and Google TPU documentation; September 2026 MLPerf Inference v6.1; DOE 2025 Data Center Energy Usage Report update; January 2026 Commerce export-policy release. Full register: `evidence/source_register.md`. |
| Landscape / comparison summary | `records/landscape_comparison.md` |
| Primary test — result | The Agent abstained from choosing a vendor and recommended a 12-week pilot with week 2/4/8/12 gates, facilities assessment, comparable quotes, and a complete-system cost denominator. Output schema validation passed. |
| Contrast test | Same accelerator technology; changed to a 25-person computer-vision startup renting cloud compute for bursty model development. |
| Contrast — what appropriately stayed stable | GPUs are mature; the field includes NVIDIA, AMD, and cloud ASICs; product cycles are rapid; peak specifications are insufficient; switching costs and representative benchmarks remain material. |
| Contrast — what appropriately changed | Ownership disappeared from the six-month shortlist. The recommendation became a four-week NVIDIA-versus-one-alternate cloud test. Metrics changed to completed-run cost, wall-clock time, accepted images per second, queue delay, failures, and engineer hours. Monitoring changed to per-run telemetry, a two-week porting gate, monthly spend control, and quarterly access review. |
| Weakness / failure found | The schema-valid v0.1 responses gave both cases almost the same generic NVIDIA/AMD/cloud bake-off and identical monitoring triggers. They over-relied on vendor memory and bandwidth figures, failed to separate chip family from access model, and did not require workload-normalized cost or engineering effort. |
| Revision made and why | Revised specialist instructions require accelerator-class analysis, evidence-type labels, complete-system measures, workload-normalized denominators, current written quotes, context-specific cadence and thresholds, a stale/hype-sensitive claim, and abstention from unsupported winners. This directly targets the observed generic and specification-led behavior. |
| Retest and verification | All four saved responses passed the frozen JSON validator. `tests/test_outputs.py` confirmed the preserved initial failure, stable general findings, different final actions and triggers, minimum evidence, and no unsupported winner. Frozen-core integrity and `git diff --check` passed. |
| Stale / hype-sensitive claim | The latest accelerator's peak low-precision throughput or memory bandwidth automatically lowers application cost. Software maturity, batching, utilization, power, cooling, availability, pricing, and migration effort can reverse that result. |
| Remaining limitation / abstention condition | No organization-supplied benchmark, approved production model, service-level target, security approval, facility measurement, cloud discount, vendor quote, or utilization forecast was available. The Agent must not name a product, vendor, capacity, cost, or performance winner until those inputs are supplied. |

## E. Independent Judgment and Handoff

| Field | Student record |
|---|---|
| Is the Agent credible enough for team consideration? Why? | Yes, as a landscape and evidence-gating specialist. It maintains the required three levels, labels vendor claims, resists peak-specification ranking, changes its decision logic across contexts, exposes missing evidence, and keeps authority bounded. It is not a procurement optimizer or application-validation specialist. |
| Independent judgment | AI GPU infrastructure is mature enough for a bounded pilot but not sufficiently evidenced for this organization to purchase. The most consequential development is competition across GPU and cloud-ASIC ecosystems, but the decisive future signal is not another peak specification: it is a matched workload result combined with facilities readiness, utilization, and comparable commercial terms. |
| Most important recommendation to the team | Preserve evidence provenance, assessment dates, workload-normalized metrics, access-model distinctions, abstention conditions, and monitoring triggers in the final mixture-of-experts interface. Pass application quality, cybersecurity, regulatory, financial, and facilities questions to the relevant specialists rather than expanding this Agent's authority. |
| Strongest alternative | Controlled hosted GPU capacity while demand and facilities evidence are collected. |
| Monitoring trigger to carry forward | At the week-12 gate, defer purchase unless projected utilization, matched benchmarks, facilities evidence, and comparable three-year quotes meet thresholds defined before vendor results are reviewed. |
| AI / verification note | ChatGPT/Codex helped interpret the assignment, instantiate the frozen scaffold, draft and critique specialist instructions, create cases, generate structured runs, identify the generic first-run failure, and automate validation. Consequential current claims were checked against dated original or authoritative sources listed in the source register. Vendor claims were labeled and were not treated as independent performance or cost evidence. Model memory and generated summaries were not used as evidence. |

## Preserved Artifacts

- Initial prompts: `work/gpu_landscape_agent_primary_initial_prompt.txt`, `work/gpu_landscape_agent_contrast_1_initial_prompt.txt`
- Revised prompts: `work/gpu_landscape_agent_primary_final_prompt.txt`, `work/gpu_landscape_agent_contrast_1_final_prompt.txt`
- Initial runs: `responses/initial_primary_response.json`, `responses/initial_contrast_1_response.json`
- Revised runs: `responses/primary_response.json`, `responses/contrast_1_response.json`
- Full test record: `records/test_record.md`
