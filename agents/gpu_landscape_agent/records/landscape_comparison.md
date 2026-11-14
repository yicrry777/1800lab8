# AI Accelerator Landscape Comparison

Assessment date: 2026-11-13

| Landscape option | What current evidence establishes | Primary life-sciences case | Startup contrast case | Evidence still needed |
|---|---|---|---|---|
| NVIDIA data-center GPU stack | Mature GPU class; B300 reference architecture lists 288 GB HBM3e and up to 8 TB/s per GPU | Lowest-friction baseline because the team already has CUDA skills; not automatically the TCO winner | Fastest compatibility baseline for PyTorch experiments | Available cloud or system configuration, matched workload results, quote, support, power, utilization |
| AMD Instinct GPU stack | Credible competing GPU family; MI350X lists 288 GB HBM3E, 8 TB/s, and 1000 W board power | Worth a time-boxed ROCm port to preserve choice; facilities and operator burden are material | Worth testing only if the selected model and kernels work within a fixed engineering budget | Porting effort, software coverage, availability, support, matched workload results, commercial terms |
| AWS Trainium2 | Purpose-built cloud AI ASIC and rental path; AWS documents Trn2 instance scale and Neuron software | Hosted comparison only if security approves and the workload ports; not an on-premises candidate | Potential alternate when AWS access and Neuron compatibility are favorable | Independent or first-party workload run, actual account price, quota, porting effort, failed-run cost |
| Google Cloud TPU | Established cloud ASIC with scalable multi-chip topology | Hosted comparison only if security approves; likely secondary given existing CUDA skills | Potential alternate when JAX or supported PyTorch path fits the model | Actual model compatibility, region/quota, workload result, price and engineering effort |
| CPU, smaller GPU, or previous-generation accelerator | Incumbent alternatives can be sufficient for low utilization or smaller models | Must be measured before sizing a large owned system | Useful for preprocessing, development, and low-duty inference | Service-level performance and completed-work cost |
| Controlled hosted GPU capacity | Separates accelerator access from hardware ownership | Strong comparator because demand and facilities readiness are uncertain | Default access model for the six-month horizon | Security approval, region, retention/logging terms, availability, current quotes |
| Immediate owned production cluster | Technically possible but evidence-poor in these cases | Excluded now: workload, facilities, quotes, and utilization are missing | Excluded: no data-center staff, variable demand, limited capital | Stable utilization, complete-system design, facilities plan, support and exit-adjusted TCO |

## Landscape position

AI GPUs are mature, but vendor competition, cloud ASICs, software ecosystems, product cadence, and system-level power requirements keep the decision environment fluid. The decision is therefore not “which chip has the largest peak number?” It is “which complete access path performs the accepted workload at the required service level with tolerable switching, facilities, and commercial risk?”

## Strongest conventional alternative

For the primary case, the strongest alternative to immediate ownership is controlled hosted GPU capacity while demand and facilities evidence are collected. For the startup, cloud rental is not an alternative to ownership; it is the default, while the meaningful alternative is the accelerator software stack used inside that rental model.
