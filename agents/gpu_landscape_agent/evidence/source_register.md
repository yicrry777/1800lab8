# Dated Evidence and Source Register

Assessment date: 2026-11-13

| Source | Date and type | Decision use | Limitation |
|---|---|---|---|
| [NVIDIA HGX AI Factory components](https://docs.nvidia.com/enterprise-reference-architectures/hgx-ai-factory/latest/components.html) | January 2026; vendor technical documentation | B300 system memory and bandwidth envelope; NVIDIA baseline | Peak specifications and reference architecture do not establish workload performance, availability, price, or total power. |
| [AMD Instinct MI350X](https://www.amd.com/en/products/accelerators/instinct/mi350/mi350x.html) | Product launched 2025-06-12; vendor specification | MI350X memory, bandwidth, ECC, virtualization, and board-power envelope | Vendor specifications do not establish RAG or computer-vision performance or TCO. |
| [AWS EC2 Trn2](https://aws.amazon.com/ec2/instance-types/trn2/) | Accessed 2026-11-13; cloud-vendor documentation and marketing | Establishes Trainium2 as a cloud ASIC and rental alternative; identifies instance scale and software stack | AWS's 30-40% price-performance statement is a vendor claim and is not used as a decision result. |
| [Google Cloud TPU v5p](https://docs.cloud.google.com/tpu/docs/v5p) | Accessed 2026-11-13; cloud-vendor technical documentation | Establishes another mature cloud ASIC class and its memory/interconnect envelope | Not a controlled comparison with the GPU products; framework and workload fit must be tested. |
| [MLPerf Inference v6.1](https://mlcommons.org/2026/09/mlperf-inference-v6-1-results/) | Published 2026-09-16; independent multi-vendor benchmark program | Supplies an architecture-neutral, reproducible comparison method and evidence of a broad, fast-moving field | Only matched models, scenarios, system scale, software, and quality targets are comparable. It is not this organization's benchmark. |
| [U.S. Data Center Energy Usage Report 2025 Update](https://www.energy.gov/documents/united-states-data-center-energy-usage-report-2025-update) | 2025 update; U.S. DOE and national-laboratory analysis, accessed 2026-11-13 | Supports treating energy, utilization, cooling, and infrastructure as material system-level dimensions | National scenarios do not size a particular facility or candidate system. |
| [Commerce semiconductor export licensing policy release](https://www.bis.gov/sites/default/files/documents/DoC%20Revises%20License%20Review%20Policy%20for%20Semiconductors%20Exports.pdf) | Published 2026-01-13; U.S. government policy release | Demonstrates that advanced-accelerator export policy is changeable and may affect supply or cross-border use | Not directly dispositive for a domestic pilot without a relevant destination, end user, or controlled activity. |

## Evidence policy applied

Vendor sources establish product existence and stated specifications, not superiority. Independent benchmarks establish a comparison method, not the result for these cases. A product or cost winner requires representative workloads, complete-system measurements, engineering effort, facilities evidence, and comparable current written quotes.

## Stale or hype-sensitive claim

The most vulnerable claim is that the latest accelerator's peak low-precision throughput or memory bandwidth automatically lowers application cost. That conclusion can change with model architecture, software maturity, batching, utilization, power, cooling, availability, discounts, and migration effort. It must be remeasured rather than repeated.
