# 🚀 SecureLLM Shield

> **Advanced AI Research Project & Enterprise Security Gateway for Large Language Models (LLMs)**

SecureLLM Shield is an enterprise-grade AI security gateway, privacy engineering framework, and real-time prompt sanitizer designed to protect confidential enterprise data, prevent privacy leakage, enforce regulatory compliance, and defend against adversarial LLM attacks.

---

## 🌟 Key Research Features

### 1. Universal 20-Entity Privacy Detection & Partial Masking
Unlike basic regex filtering systems, SecureLLM Shield uses a unified hybrid detection engine that scans prompts for 20 sensitive entity types and applies intelligent **partial masking** instead of full redaction, preserving contextual utility while eliminating data leakage.

### 2. Multi-Stage Hybrid Privacy Pipeline
Every prompt passes through a 6-stage detection pipeline:
```
Regex Pattern Engine ➔ Named Entity Recognition (NER) ➔ Transformer Classifier ➔ LLM Self-Verification ➔ Risk Aggregator ➔ Final Action (Mask / Block / Pass)
```

### 3. Adaptive Privacy Policy Engine
Administrators can toggle pre-configured security profiles or customize individual regulations:
- **Enterprise Profile:** Shields API keys, source code, employee records, and internal documents.
- **Healthcare Profile:** Strictly blocks Patient IDs, HIPAA-protected health information (PHI), and medical diagnoses.
- **Banking Profile:** Masks credit/debit card credentials, bank account numbers, and IFSC codes.
- **Government Profile:** Enforces strict protection on national identity tags (Aadhaar cards, PAN, Passports).

### 4. AI-Based Risk Prediction Engine
Assigns real-time risk scores (0–100%) based on entity sensitivity weights, prompt injection probability, user role clearance, and prompt complexity index:
- `0% – 25%` $\rightarrow$ **Safe**
- `26% – 50%` $\rightarrow$ **Moderate Risk**
- `51% – 75%` $\rightarrow$ **High Risk**
- `76% – 100%` $\rightarrow$ **Critical Risk**

### 5. Secure Retrieval-Augmented Generation (Secure RAG)
Provides role-based access control (RBAC) over vector databases (FAISS, ChromaDB, Pinecone). Search results are dynamically sanitized or restricted based on the querying user's active role (**Guest**, **Employee**, **Researcher**, **Manager**, **Administrator**).

### 6. Multi-Stage Prompt Injection & Jailbreak Defense
Detects and blocks complex adversarial attacks including Do-Anything-Now (DAN) jailbreaks, system prompt overrides, context poisoning, and indirect prompt injection attempts.

### 7. Automated AI Red Team Simulation Sandbox
Executes automated adversary campaigns against deployed LLM nodes to evaluate safety scores, bypass rates, and defensive posture.

### 8. Cross-LLM Security Benchmarking & Migration
Evaluates leading foundation models (**OpenAI GPT-4o**, **Claude 3.5 Sonnet**, **Llama 3.1 70B**, **Gemma 2 27B**, **DeepSeek V3**) under identical threat vectors. Includes an LLM migration wizard for cloning safety policy gates between providers.

### 9. Explainable AI (XAI) Security Dashboard
Accompanies every security decision with an entity-level explanation table displaying confidence scores, regulatory reasons, and masking strategies.

### 10. Differential Privacy & Homomorphic Encryption
- **Differential Privacy ($\epsilon$-budget):** Injects calibrated noise into analytical database queries to guarantee statistical privacy.
- **Homomorphic Encryption:** Performs math operations directly on encrypted payloads without decrypting sensitive values.

### 11. Blockchain Audit Trail
Stores security events, policy updates, and prompt evaluations as cryptographically linked, tamper-proof blocks in an immutable ledger.

### 12. Intelligent Security Copilot
An embedded AI assistant that provides instant guidance on HIPAA, GDPR, DPDP Act compliance, and security alert explanations.

---

## 🔒 Supported Entities & Partial Masking Strategy

| Entity Type | Example Input | Masked Output | Masking Strategy |
| :--- | :--- | :--- | :--- |
| **Aadhaar Number** | `4567 8912 3456` | `XXXX XXXX 3456` | Preserve last 4 digits |
| **PAN Number** | `ABCDE1234F` | `XXXXX1234F` | Mask first 5 letters |
| **Bank Account** | `12345678901` | `XXXXXXX8901` | Preserve last 4 digits |
| **IFSC Code** | `SBIN0001234` | `SBINXXXX234` | Preserve bank code & suffix |
| **Credit / Debit Card** | `4111111111111111` | `XXXXXXXXXXXX1111` | PCI-DSS compliant masking |
| **Passport Number** | `K1234567` | `XXXX4567` | Mask first 4 digits |
| **Driving License** | `DL-1420110012345` | `DL-XXXXXXXX12345` | Mask state ID / middle digits |
| **GST Number** | `22AAAAA0000A1Z5` | `22XXXXXXXXXA1Z5` | Mask PAN component |
| **Voter ID** | `ABC1234567` | `XXXXX34567` | Preserve last 5 digits |
| **UPI ID** | `sonuz@oksbi` | `s****@oksbi` | Preserve 1st char & domain |
| **Email Address** | `sonuz@gmail.com` | `s****@gmail.com` | Domain-preserving masking |
| **Mobile Number** | `9876543210` | `XXXXXX3210` | Preserve last 4 digits |
| **API Keys** | `sk_test_abc123xyz` | `sk_********xyz` | Key prefix/suffix preservation |
| **JWT Tokens** | `eyJhbGc...` | `[MASKED_JWT]` | Full structural redaction |
| **Secret Key** | `secret_key_12345` | `secret_****12345` | Mask key body |
| **IP Address** | `192.168.1.1` | `XXX.XXX.1.1` | Subnet-preserving masking |
| **MAC Address** | `00:1A:2B:3C:4D:5E` | `XX:XX:XX:XX:4D:5E` | Preserve last 2 octets |
| **Employee ID** | `EMP12345` | `EMPXXXX5` | Mask middle numerical ID |
| **Medical Record** | `MRN-987654` | `MRN-XXXX54` | HIPAA PHI anonymization |

---

## 📋 Compliance Matrix

SecureLLM Shield automatically audits system posture against global regulatory frameworks:
- **GDPR (Europe):** Data minimization & differential privacy compliance.
- **HIPAA (USA):** Health record & PHI masking verification.
- **DPDP Act 2023 (India):** Mandatory national identity (Aadhaar/PAN) protection.
- **EU AI Act:** Explainable AI (XAI) auditing & AI Red Team validation.
- **PCI-DSS:** Payment card data protection.

---

## ⚡ Quick Start Guide

### Running Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/subashp-2104/SecureLLM-Shield.git
   cd SecureLLM-Shield
   ```

2. Launch a local web server (using Python):
   ```bash
   python -m http.server 8000
   ```

3. Open your browser and navigate to:
   ```
   http://localhost:8000
   ```

---

## 🎯 Benchmark Verification Test

Input prompt containing multiple sensitive entities:
```text
My name is SONUZ.
My Aadhaar number is 4567 8912 3456.
My PAN is ABCDE1234F.
My bank account number is 12345678901.
Email is sonuz@gmail.com
Phone is 9876543210
UPI is sonuz@oksbi
IFSC is SBIN0001234
```

Sanitized Gateway Output:
```text
My name is SONUZ.
My Aadhaar number is XXXX XXXX 3456.
My PAN is XXXXX1234F.
My bank account number is XXXXXXX8901.
Email is s****@gmail.com
Phone is XXXXXX3210
UPI is s****@oksbi
IFSC is SBINXXXX234
```

---

## 📜 License & Citation

Distributed under the MIT License. Feel free to use, modify, and contribute to this project.
