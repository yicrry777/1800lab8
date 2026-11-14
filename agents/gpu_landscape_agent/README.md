# AI GPU Landscape Agent

Assignment 8 specialist agent for the changing landscape of data-center AI GPU accelerators and adjacent alternatives.

## Cases

- `cases/primary.json`: on-premises private RAG inference for a mid-sized U.S. life-sciences company.
- `cases/contrast_1.json`: rented cloud acceleration for a small computer-vision startup.
- `cases/contrast_2.json`: optional university-library stress test; not used in the required test record.

## Reproduce the prompt packets

```text
python3 tools/build_prompt.py --agent agents/gpu_landscape_agent --case agents/gpu_landscape_agent/cases/primary.json --out work/gpu_landscape_agent_primary_final_prompt.txt
python3 tools/build_prompt.py --agent agents/gpu_landscape_agent --case agents/gpu_landscape_agent/cases/contrast_1.json --out work/gpu_landscape_agent_contrast_1_final_prompt.txt
```

## Validate the saved runs

```text
python3 tools/validate_response.py agents/gpu_landscape_agent/responses/primary_response.json
python3 tools/validate_response.py agents/gpu_landscape_agent/responses/contrast_1_response.json
python3 agents/gpu_landscape_agent/tests/test_outputs.py
python3 tools/check_frozen_core.py
```

The `initial_*` responses and prompt packets preserve the weak first run. The unprefixed responses are the post-revision runs. See `records/test_record.md` for the diagnosis and comparison.
