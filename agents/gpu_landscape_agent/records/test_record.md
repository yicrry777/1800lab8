# Primary and Context-Contrast Test Record

Test date: 2026-11-13

## Test design

The emerging technology remained constant: data-center AI GPU accelerators for generative-AI inference. The context changed materially:

- Primary: conservative mid-sized life-sciences company considering owned on-premises RAG infrastructure, with IP, facilities, and regulated-workflow consequences.
- Contrast: aggressive 25-person computer-vision startup using rented cloud compute for bursty training and inference, with reversible failures and scarce capital.

## Initial run and observed failure

The v0.1 prompts produced schema-valid responses, but the test failed the context-sensitivity standard in an important way:

- Both cases received nearly the same generic “compare NVIDIA, AMD, and one cloud accelerator” recommendation.
- Both used an identical four-item monitoring list, including export controls and power requirements even where they were not decision-relevant.
- Both were driven mainly by vendor memory and bandwidth specifications.
- Neither separated accelerator family from ownership/access model or required a workload-normalized cost denominator.
- The startup response changed the tone toward cloud rental, but not the comparison design, cadence, or decision threshold enough.

This is preserved in `responses/initial_primary_response.json`, `responses/initial_contrast_1_response.json`, and the two `work/*_initial_prompt.txt` packets.

## Revision

The specialist instructions were revised to:

1. compare accelerator classes before products;
2. distinguish vendor specification, vendor claim, independent benchmark, quote, and inference;
3. prohibit product or cost winners based on peak specifications;
4. require complete-system and workload-normalized measures;
5. separate chip family from owned, hosted, or cloud access;
6. make shortlist, metrics, cadence, and thresholds context-sensitive;
7. require one stale/hype-sensitive claim and explicit abstention conditions; and
8. flag identical generic bake-offs and monitoring lists as test failures.

## Post-revision result

### What appropriately stayed stable

- Data-center GPUs are mature, but the landscape changes rapidly.
- NVIDIA, AMD, and cloud ASICs are credible classes.
- Peak specifications do not establish workload performance or cost.
- Software switching costs and representative benchmarks remain important.
- A product or cost winner requires comparable current evidence.

### What appropriately changed

| Dimension | Primary case | Contrast case |
|---|---|---|
| Access posture | Pilot with evaluation, loaner, or approved hosted capacity while assessing on-premises ownership | Cloud rental only during the six-month horizon |
| Baseline | NVIDIA because existing CUDA skill reduces near-term migration effort | NVIDIA because it protects time to first completed PyTorch experiment |
| Alternative test | AMD plus one security-approved hosted path; facilities work runs in parallel | One of AMD, Trainium2, or TPU selected by framework compatibility and tested under a strict engineering-time budget |
| Main denominator | Cost per million accepted tokens at latency/quality target, plus three-year facilities and exit costs | Cost and wall-clock time per completed training run, accepted images per second, failures, queue delay, and engineer hours |
| Main risk | Stranded capital, facility delay, data control, support, and low utilization | Runaway cloud spend, quota delay, and scarce engineering time lost to porting |
| Monitoring cadence | Week 2/4/8/12 decision gates plus quarterly market refresh | Per-run telemetry, week 2/4 gates, monthly spend control, quarterly access review |
| Bounded action | Authorize evidence collection; no production purchase | Run a four-week cloud comparison; no hardware purchase |

## Validation result

- Initial primary response: schema validation passed.
- Initial contrast response: schema validation passed.
- Revised primary response: schema validation passed.
- Revised contrast response: schema validation passed.
- Automated context-contrast assertions: passed.
- Frozen-core integrity check: passed.

## Remaining limitations

The runs use verified public evidence but not organization-supplied benchmarks, vendor quotes, facility measurements, cloud-account discounts, or security approvals. The Agent therefore appropriately abstains from naming a vendor, product, capacity, performance, or cost winner.
