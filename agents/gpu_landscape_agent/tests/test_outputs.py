#!/usr/bin/env python3
from pathlib import Path
import json

AGENT = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((AGENT / "responses" / name).read_text())


initial_primary = load("initial_primary_response.json")
initial_contrast = load("initial_contrast_1_response.json")
primary = load("primary_response.json")
contrast = load("contrast_1_response.json")

# Preserve evidence that the first run was too generic.
assert initial_primary["change_monitoring_triggers"] == initial_contrast["change_monitoring_triggers"]
assert "NVIDIA, AMD, and one cloud" in initial_primary["recommendation_management_implication"]
assert "NVIDIA, AMD, and one cloud" in initial_contrast["recommendation_management_implication"]

# Stable general landscape claims should survive the context change.
for phrase in [
    "mature deployable infrastructure",
    "AWS Trainium",
    "Google TPU",
    "peak specification",
]:
    assert phrase.lower() in primary["general_et_finding"].lower()
    assert phrase.lower() in contrast["general_et_finding"].lower()

# The revised management actions and monitoring designs must differ materially.
assert "12-week" in primary["recommendation_management_implication"]
assert "power/cooling" in primary["recommendation_management_implication"].lower()
assert "four weeks" in contrast["recommendation_management_implication"]
assert "cloud" in contrast["recommendation_management_implication"].lower()
assert primary["change_monitoring_triggers"] != contrast["change_monitoring_triggers"]
assert not set(primary["change_monitoring_triggers"]) & set(contrast["change_monitoring_triggers"])

# Neither revised output is allowed to overclaim a winner.
for output in [primary, contrast]:
    combined = " ".join([
        output["general_et_finding"],
        output["application_finding"],
        output["organization_specific_finding"],
        output["recommendation_management_implication"],
    ]).lower()
    assert "abstain" in combined or "cannot" in combined or "must wait" in combined or "do not" in combined
    assert len(output["evidence"]) >= 5
    assert all(item["source_or_reference"].startswith("https://") for item in output["evidence"])

print("CONTEXT CONTRAST TEST PASSED")
