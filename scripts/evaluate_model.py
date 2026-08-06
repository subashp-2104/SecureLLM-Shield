import os
import sys
import json

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import detect_entities
from threat_detection.multimodal_threat import MultimodalThreatDetector

DATASET_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "datasets", "synthetic", "synthetic_multimodal_dataset.jsonl")

def run_evaluation():
    if not os.path.exists(DATASET_FILE):
        print("Dataset file not found. Generating data first...")
        import generate_synthetic_data
        generate_synthetic_data.generate_dataset()

    total_samples = 0
    pii_true_positives = 0
    pii_false_positives = 0
    pii_false_negatives = 0

    inj_true_positives = 0
    inj_false_positives = 0
    inj_false_negatives = 0

    with open(DATASET_FILE, "r", encoding="utf-8") as f:
        for line in f:
            total_samples += 1
            record = json.loads(line.strip())
            text = record["text"]
            category = record["category"]
            has_expected_pii = len(record.get("entities", [])) > 0
            has_expected_inj = record.get("threat_label") != "SAFE"

            # 1. Run PII detection
            detected_pii = detect_entities(text)
            has_detected_pii = len(detected_pii) > 0

            if has_expected_pii and has_detected_pii:
                pii_true_positives += 1
            elif not has_expected_pii and has_detected_pii:
                pii_false_positives += 1
            elif has_expected_pii and not has_detected_pii:
                pii_false_negatives += 1

            # 2. Run Threat Detection
            threats = MultimodalThreatDetector.detect_threats([{"text": text, "source_type": "text"}])
            has_detected_inj = len(threats) > 0

            if has_expected_inj and has_detected_inj:
                inj_true_positives += 1
            elif not has_expected_inj and has_detected_inj:
                inj_false_positives += 1
            elif has_expected_inj and not has_detected_inj:
                inj_false_negatives += 1

    # Calculate metrics
    pii_precision = (pii_true_positives / (pii_true_positives + pii_false_positives)) if (pii_true_positives + pii_false_positives) > 0 else 1.0
    pii_recall = (pii_true_positives / (pii_true_positives + pii_false_negatives)) if (pii_true_positives + pii_false_negatives) > 0 else 1.0
    pii_f1 = (2 * pii_precision * pii_recall / (pii_precision + pii_recall)) if (pii_precision + pii_recall) > 0 else 1.0

    inj_precision = (inj_true_positives / (inj_true_positives + inj_false_positives)) if (inj_true_positives + inj_false_positives) > 0 else 1.0
    inj_recall = (inj_true_positives / (inj_true_positives + inj_false_negatives)) if (inj_true_positives + inj_false_negatives) > 0 else 1.0
    inj_f1 = (2 * inj_precision * inj_recall / (inj_precision + inj_recall)) if (inj_precision + inj_recall) > 0 else 1.0

    print("==========================================================")
    print("HYBRID DETECTION EVALUATION METRICS REPORT")
    print("==========================================================")
    print(f"Total Dataset Test Samples: {total_samples}")
    print("\n--- PII Detection Performance ---")
    print(f"PII Precision : {pii_precision * 100:.2f}%")
    print(f"PII Recall    : {pii_recall * 100:.2f}%")
    print(f"PII F1-Score  : {pii_f1 * 100:.2f}%")
    print(f"False Positives: {pii_false_positives} | False Negatives: {pii_false_negatives}")

    print("\n--- Multimodal Threat & Prompt Injection Performance ---")
    print(f"Threat Precision : {inj_precision * 100:.2f}%")
    print(f"Threat Recall    : {inj_recall * 100:.2f}%")
    print(f"Threat F1-Score  : {inj_f1 * 100:.2f}%")
    print(f"False Positives: {inj_false_positives} | False Negatives: {inj_false_negatives}")
    print("==========================================================")

if __name__ == "__main__":
    run_evaluation()
