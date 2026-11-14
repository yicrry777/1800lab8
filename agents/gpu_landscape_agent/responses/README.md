# Saved Agent Runs

- `initial_primary_response.json` and `initial_contrast_1_response.json`: schema-valid v0.1 runs preserved because they exposed generic, specification-led analysis and duplicated monitoring triggers.
- `primary_response.json` and `contrast_1_response.json`: post-revision v1.0 runs used for the final record.

All four files are validated by the frozen response validator. The separate context-contrast assertions in `../tests/test_outputs.py` verify both the preserved initial weakness and the intended post-revision differences.
