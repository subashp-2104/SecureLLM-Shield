import os
import hashlib
import time
import json
from typing import Dict, Any, List

AUDIT_LOG_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "uploads", "audit_chain.json")

class MultimodalAuditLedger:
    @staticmethod
    def compute_sha256(file_path: str) -> str:
        sha256_hash = hashlib.sha256()
        try:
            with open(file_path, "rb") as f:
                for byte_block in iter(lambda: f.read(4096), b""):
                    sha256_hash.update(byte_block)
            return sha256_hash.hexdigest()
        except Exception:
            return hashlib.sha256(file_path.encode()).hexdigest()

    @classmethod
    def record_event(cls, file_metadata: Dict[str, Any], risk_score: int, risk_label: str, entities: List[Any], threats: List[Any], action_taken: str) -> Dict[str, Any]:
        file_path = file_metadata.get("original_path", "")
        file_hash = cls.compute_sha256(file_path) if os.path.exists(file_path) else "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"

        # Load audit chain
        chain = []
        if os.path.exists(AUDIT_LOG_FILE):
            try:
                with open(AUDIT_LOG_FILE, "r", encoding="utf-8") as f:
                    chain = json.load(f)
            except Exception:
                chain = []

        previous_hash = chain[-1]["block_hash"] if chain else "0000000000000000000000000000000000000000000000000000000000000000"
        block_index = len(chain) + 1
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

        block_data = {
            "block_index": block_index,
            "timestamp": timestamp,
            "file_id": file_metadata.get("file_id"),
            "filename": file_metadata.get("original_filename"),
            "category": file_metadata.get("category"),
            "file_sha256": file_hash,
            "previous_hash": previous_hash,
            "risk_score": risk_score,
            "risk_label": risk_label,
            "entities_count": len(entities),
            "threats_count": len(threats),
            "action_taken": action_taken
        }

        # Calculate block hash
        block_string = json.dumps(block_data, sort_keys=True)
        block_hash = hashlib.sha256(block_string.encode()).hexdigest()
        block_data["block_hash"] = block_hash

        chain.append(block_data)

        try:
            with open(AUDIT_LOG_FILE, "w", encoding="utf-8") as f:
                json.dump(chain, f, indent=2)
        except Exception as err:
            print("Audit log save error:", err)

        return block_data
