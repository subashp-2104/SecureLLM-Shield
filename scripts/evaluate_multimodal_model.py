import os
import json
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from app import detect_entities
from threat_detection.multimodal_threat import MultimodalThreatDetector

dataset_file = os.path.join(BASE_DIR, "test_data", "multimodal", "synthetic_corpus_500.jsonl")

if not os.path.exists(dataset_file):
    print("Error: Dataset file not found.")
    sys.exit(1)

records = []
with open(dataset_file, "r", encoding="utf-8") as f:
    for line in f:
        if line.strip():
            records.append(json.loads(line))

print("==================================================")
print(f"EVALUATING HYBRID SECURITY MODEL ON {len(records)} SYNTHETIC TEST SAMPLES")
print("==================================================")

true_positives = 0
false_positives = 0
false_negatives = 0
true_negatives = 0

threat_tp = 0
threat_fp = 0
threat_fn = 0
threat_tn = 0

for rec in records:
    text = rec["text"]
    expected_entities = rec.get("expected_entities", [])
    expected_threats = rec.get("expected_threats", [])
    
    # 1. PII Detection Evaluation
    detected = detect_entities(text)
    detected_types = set(e.entity_type for e in detected)
    exp_types = set(expected_entities)
    
    if not exp_types:
        if detected_types:
            false_positives += len(detected_types)
        else:
            true_negatives += 1
    else:
        for t in exp_types:
            if t in detected_types:
                true_positives += 1
            else:
                false_negatives += 1
        for d in detected_types:
            if d not in exp_types:
                false_positives += 1

    # 2. Threat Detection Evaluation
    threat_blocks = [{"text": text, "content_type": "text"}]
    threats = MultimodalThreatDetector.detect_threats(threat_blocks)
    threat_detected = len(threats) > 0
    exp_threat_detected = len(expected_threats) > 0
    
    if exp_threat_detected and threat_detected:
        threat_tp += 1
    elif not exp_threat_detected and not threat_detected:
        threat_tn += 1
    elif not exp_threat_detected and threat_detected:
        threat_fp += 1
    elif exp_threat_detected and not threat_detected:
        threat_fn += 1

pii_precision = true_positives / (true_positives + false_positives) if (true_positives + false_positives) > 0 else 1.0
pii_recall = true_positives / (true_positives + false_negatives) if (true_positives + false_negatives) > 0 else 1.0
pii_f1 = (2 * pii_precision * pii_recall) / (pii_precision + pii_recall) if (pii_precision + pii_recall) > 0 else 0.0

threat_precision = threat_tp / (threat_tp + threat_fp) if (threat_tp + threat_fp) > 0 else 1.0
threat_recall = threat_tp / (threat_tp + threat_fn) if (threat_tp + threat_fn) > 0 else 1.0
threat_f1 = (2 * threat_precision * threat_recall) / (threat_precision + threat_recall) if (threat_precision + threat_recall) > 0 else 0.0

print(f"PII Detection Metrics:")
print(f"  • True Positives  : {true_positives}")
print(f"  • False Positives : {false_positives}")
print(f"  • False Negatives : {false_negatives}")
print(f"  • Precision       : {pii_precision * 100:.2f}%")
print(f"  • Recall          : {pii_recall * 100:.2f}%")
print(f"  • F1 Score        : {pii_f1 * 100:.2f}%")
print("--------------------------------------------------")
print(f"Threat Detection Metrics:")
print(f"  • True Positives  : {threat_tp}")
print(f"  • False Positives : {threat_fp}")
print(f"  • False Negatives : {threat_fn}")
print(f"  • Precision       : {threat_precision * 100:.2f}%")
print(f"  • Recall          : {threat_recall * 100:.2f}%")
print(f"  • F1 Score        : {threat_f1 * 100:.2f}%")
print("==================================================")

results_summary = {
    "corpus_size": len(records),
    "pii_metrics": {
        "true_positives": true_positives,
        "false_positives": false_positives,
        "false_negatives": false_negatives,
        "precision": pii_precision,
        "recall": pii_recall,
        "f1_score": pii_f1
    },
    "threat_metrics": {
        "true_positives": threat_tp,
        "false_positives": threat_fp,
        "false_negatives": threat_fn,
        "precision": threat_precision,
        "recall": threat_recall,
        "f1_score": threat_f1
    }
}

with open(os.path.join(BASE_DIR, "test_data", "multimodal", "expected_results", "model_evaluation_metrics.json"), "w") as f:
    json.dump(results_summary, f, indent=2)

print("Saved model evaluation metrics report to model_evaluation_metrics.json.")
