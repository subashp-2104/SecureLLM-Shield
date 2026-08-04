# 🚀 SecureLLM Shield

> **Advanced AI Research Project & Enterprise Security Gateway for Large Language Models (LLMs)**

SecureLLM Shield is an enterprise-grade AI security gateway, privacy engineering framework, and real-time prompt sanitizer designed to protect confidential enterprise data, prevent privacy leakage, enforce regulatory compliance, and defend against adversarial LLM attacks.

---

## 🌟 Key Project Highlights & Updates

- **📊 College Project Review Presentation File (`.pptx`):**
  - Includes `SecureLLM_Shield_Presentation.pptx` containing **18 professional slides** formatted for academic project reviews.
  - Team Details: **BARATHKUMAR M** (Reg No: `111923AM01007`) & **SUBASH P** (Reg No: `111923AM02052`), Dept of AI & ML.
  - Formatted in 16:9 Widescreen with Dark Blue (`#0B132B`), Electric Cyan (`#00F2FE`), and Neon Teal (`#48CAE4`) cybersecurity theme.
  - Embedded high-resolution graphics (`assets/security_shield.jpg` and `assets/threat_nodes.jpg`) and speaker notes for every slide.

- **🛡️ Universal 20-Entity Detection Matrix & Quick Test Presets:**
  - Interactive matrix panel positioned under Prompt Sandbox with zero blank space.
  - Quick test buttons: **`Multi-Entity Test`**, **`DAN Jailbreak Attack`**, and **`API Secret Leakage`**.
  - Displays live PII badges (**Aadhaar**, **PAN**, **Credit Cards**, **Bank Acc**, **IFSC**, **UPI ID**, **API Keys**, **Medical**) and latency chips (`< 45ms`, `99.8% Accuracy`).

- **⚡ Auto-Initialization & Pre-Analysis:**
  - Auto-populates and analyzes prompt sanitizer payloads on initial page load (zero blank states).

- **📐 Responsive Auto-Fit Layout (1300px Breakpoint):**
  - Grid layouts (`.benchmark-layout`, `.playground-layout`, `.policy-layout`, `.rag-layout`, `.redteam-layout`, `.grid-2-1`) dynamically stack right-side cards under 1300px width for zero horizontal clipping on laptops and zoomed viewports.

- **🔍 Interactive Security Audit Details Modal:**
  - Click ANY status badge (`Masked 🔍`, `Blocked 🔍`, `Sanitized 🔍`, `Cleared 🔍`) to open a glassmorphic audit trace modal displaying timestamp, user session, compliance rules, risk scores, and raw log traces.

---

## 🌟 Core Modules

### 1. Universal 20-Entity Privacy Detection & Partial Masking
Unlike basic regex filtering systems, SecureLLM Shield uses a unified hybrid detection engine that scans prompts for **20 sensitive entity types** and applies intelligent **partial masking** instead of full redaction, preserving contextual utility while eliminating data leakage:
- 🇮🇳 **Aadhaar Card Numbers** (`1234 5678 9012` ➔ `XXXX XXXX 9012`) — Universal 12-digit detection across all starting digits (`0-9`).
- 🇮🇳 **PAN Card Identification** (`ABCDE1234F` ➔ `XXXXX1234F`) — Conceals identity prefix.
- 💳 **Credit / Debit Cards** (`4111-2222-3333-4444` ➔ `XXXX-XXXX-XXXX-4444`) — PCI-DSS compliant 12-digit masking.
- 🏦 **Bank Account Numbers** (`12345678901` ➔ `XXXXXXX8901`) — Account number prefix protection.
- 📱 **UPI Payment IDs** (`sonuz@oksbi` ➔ `s****@oksbi`) — Handle privacy shielding.
- 🏛️ **IFSC Banking Codes** (`SBIN0001234` ➔ `SBINXXXX234`) — Conceals branch code.
- 🔑 **API Keys & Developer Secrets** (`sk_test_abc...` ➔ `[API_KEY_SECRET_REDACTED]`).
- 👤 **PII (Email, Phone, IP, MAC, Employee ID, Medical Records)** — Full anonymization.

### 2. Multi-Stage Hybrid Privacy Pipeline
Every prompt passes through a 6-stage detection pipeline:
```
Regex Pattern Engine ➔ Named Entity Recognition (NER) ➔ Transformer Classifier ➔ LLM Self-Verification ➔ Risk Aggregator ➔ Final Action (Mask / Block / Pass)
```

### 3. Adaptive Privacy Policy Engine
Toggle pre-configured security profiles or customize individual regulations:
- **Enterprise Profile:** Shields API keys, source code, employee records, and internal documents.
- **Healthcare Profile:** Strictly blocks Patient IDs, HIPAA-protected health information (PHI), and medical diagnoses.
- **Banking Profile:** Masks credit/debit card credentials, bank account numbers, and IFSC codes.
- **Government Profile:** Enforces strict protection on national identity tags (Aadhaar cards, PAN, Passports).

### 4. AI-Based Risk Prediction Engine
Assigns real-time risk scores (0–100%) based on entity sensitivity weights, prompt injection probability, user role clearance, and prompt complexity index:
- `0% – 25%` ➔ **SAFE (0%)**
- `26% – 50%` ➔ **MODERATE (30%)**
- `51% – 75%` ➔ **HIGH (60%)**
- `76% – 100%` ➔ **CRITICAL (98%)**

### 5. Secure Retrieval-Augmented Generation (Secure RAG)
Provides role-based access control (RBAC) over vector databases (FAISS). Search results are dynamically sanitized or restricted based on the querying user's active role (**Guest**, **Employee**, **Researcher**, **Manager**, **Administrator**).

### 6. Privacy Layers (Differential Privacy & Homomorphic Encryption)
- **Differential Privacy ($\epsilon$-budget):** Injects calibrated Gaussian noise into analytical database queries to guarantee statistical privacy.
- **Homomorphic Encryption:** Performs mathematical operations directly on encrypted payloads without decrypting sensitive values.

### 7. AI Red Team Simulation Sandbox
Executes automated adversary campaigns (DAN Jailbreaks, Indirect Injection, PII Harvesting, System Prompt Overrides) against deployed LLM nodes to evaluate safety scores, bypass rates (`0%`), and security ratings (`A+`).

### 8. Cross-LLM Security Benchmarking & Migration Engine
Evaluates leading foundation models (**Claude 3.5 Sonnet**, **OpenAI GPT-4o**, **Llama 3.1 70B**, **Gemma 2 27B**, **DeepSeek V3**) under identical threat payloads with a real-time bubble chart and policy migration wizard.

### 9. Cryptographic Blockchain Audit Ledger
Stores security events, policy updates, and prompt evaluations as cryptographically linked, tamper-proof blocks in an immutable ledger with SHA-256 chain integrity verification.

### 10. Intelligent Security Copilot
An embedded AI assistant drawer providing instant guidance on HIPAA, GDPR, DPDP Act compliance, and risk alert explanations.

---

## 🔒 Supported Entities & Partial Masking Strategy

| Entity Type | Example Input | Masked Output | Risk Classification |
| :--- | :--- | :--- | :--- |
| **Aadhaar Number** | `1234 5678 9012` | `XXXX XXXX 9012` | **Critical Risk** |
| **PAN Number** | `ABCDE1234F` | `XXXXX1234F` | **High Risk** |
| **Bank Account** | `12345678901` | `XXXXXXX8901` | **High Risk** |
| **IFSC Code** | `SBIN0001234` | `SBINXXXX234` | **Moderate Risk** |
| **Credit / Debit Card** | `4111-2222-3333-4444` | `XXXX-XXXX-XXXX-4444` | **Critical Risk** |
| **Passport Number** | `Z1234567` | `ZXXXX567` | **High Risk** |
| **Driving License** | `DL-1420110012345` | `DL-XXXXXX12345` | **Moderate Risk** |
| **GSTIN Number** | `22AAAAA0000A1Z5` | `22XXXXXXXXXA1Z5` | **Moderate Risk** |
| **Voter ID** | `ABC1234567` | `ABCXXXX567` | **Moderate Risk** |
| **UPI ID** | `sonuz@oksbi` | `s****@oksbi` | **Moderate Risk** |
| **Email Address** | `john.doe@company.com` | `j****@company.com` | **Moderate Risk** |
| **Mobile Number** | `+91 9876543210` | `XXXXXX3210` | **High Risk** |
| **API Keys** | `sk_live_51Nz849...` | `[API_KEY_SECRET_REDACTED]` | **Critical Risk** |
| **JWT Tokens** | `eyJhbGciOi...` | `[JWT_TOKEN_REDACTED]` | **Critical Risk** |
| **Secret Passwords** | `BEGIN RSA PRIVATE KEY` | `[SECRET_KEY_REDACTED]` | **Critical Risk** |
| **IP Address** | `192.168.1.100` | `192.168.X.X` | **Low Risk** |
| **MAC Address** | `00:1A:2B:3C:4D:5E` | `00:1A:2B:XX:XX:XX` | **Low Risk** |
| **Employee ID** | `EMP-9821` | `EMPXXXX1` | **Moderate Risk** |
| **Medical Record (MRN)**| `MRN-88219` | `MRNXXXX19` | **Critical Risk (HIPAA)** |

---

## ⚡ Installation & Running Guide

### 💻 Running in Visual Studio Code (VS Code)

1. **Open Project Folder in VS Code:**
   - Launch Visual Studio Code.
   - Click **File ➔ Open Folder...** (`Ctrl + K, Ctrl + O`) and select the `Secure LLM Shield` directory.

2. **Open Integrated Terminal:**
   - Press **`Ctrl + ~`** (or top menu **Terminal ➔ New Terminal**).

3. **Start Python Application Server:**
   ```powershell
   python app.py
   ```

4. **Launch Application in Browser:**
   - Open your web browser and go to:
     👉 **[http://localhost:8000](http://localhost:8000)** (or `Ctrl + Click` the terminal link `http://127.0.0.1:8000`).

---

## 🎯 Verified Multi-Entity Test Case

Input Prompt:
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

Sanitized Output:
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

Risk Assessment Result:
- **Overall Risk Index:** `98% (CRITICAL)`
- **XAI Threat Status:** `YES (7 PII Spans Sanitized)`

---

## 📊 PowerPoint Presentation File

- **File Path:** [`SecureLLM_Shield_Presentation.pptx`](file:///c:/Users/mukes/OneDrive/Desktop/SUBASH_PROJECT/Secure%20LLM%20Shield/SecureLLM_Shield_Presentation.pptx)
- **Slide Count:** 18 Slides with Speaker Notes
- **Team Presenters:** BARATHKUMAR M & SUBASH P

---

## 📜 License

Distributed under the **MIT License**. Free to use, modify, and distribute for academic and enterprise research.
