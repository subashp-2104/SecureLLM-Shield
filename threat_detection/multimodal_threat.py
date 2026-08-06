import re
from typing import List, Dict, Any

class MultimodalThreatDetector:
    # Threat Categories & Pattern Vectors
    INJECTION_PATTERNS = [
        (r'(?i)system\s+override', "Instruction Override Attack", "Critical", 99.4, "Attempts to override base system instructions."),
        (r'(?i)ignore\s+(?:all\s+)?previous\s+(?:instructions|directives|rules)', "Direct Prompt Injection", "Critical", 99.8, "Tries to erase system boundary instructions."),
        (r'(?i)do\s+anything\s+now', "DAN Jailbreak Attempt", "Critical", 98.9, "Classic DAN jailbreak persona override."),
        (r'(?i)you\s+are\n?now\s+in\s+(?:developer|diagnostic|jailbroken)\s+mode', "Jailbreak Persona Switch", "Critical", 97.5, "Attempts to force developer bypass mode."),
        (r'(?i)read\s+(?:the\s+)?root\s+config', "Data Exfiltration Attempt", "High", 95.0, "Attacks target server configuration files."),
        (r'(?i)reveal\s+(?:system\s+prompt|secret\s+keys)', "System Prompt Extraction", "High", 96.2, "Attempts to exfiltrate base prompt instructions."),
        (r'(?i)disregard\s+security\s+rules', "Instruction Override Attack", "Critical", 98.1, "Explicit request to disable security filters."),
        (r'(?i)bypass\s+safety\s+guardrails', "Guardrail Bypass Attack", "High", 94.8, "Attacks safety validation checks.")
    ]

    @classmethod
    def detect_threats(cls, extracted_blocks: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        threats = []
        for block in extracted_blocks:
            text = block.get("text", "")
            source_type = block.get("source_type", "file")
            location = block.get("location", {})
            timestamp = block.get("timestamp", "Page 1")

            for pattern, threat_category, severity, confidence, explanation in cls.INJECTION_PATTERNS:
                if re.search(pattern, text):
                    threats.append({
                        "threat_category": threat_category,
                        "severity": severity,
                        "confidence": confidence,
                        "explanation": explanation,
                        "source_type": source_type,
                        "timestamp": timestamp,
                        "location": location,
                        "recommended_action": "Block / Quarantine" if severity == "Critical" else "Sanitize & Review"
                    })
                    break
        return threats
