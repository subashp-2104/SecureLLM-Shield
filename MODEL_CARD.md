# Model Card: SecureLLM Shield Hybrid Multimodal Security Engine (`MODEL_CARD.md`)

> **Model Version:** v1.0-Hybrid  
> **Model Type:** Multimodal Hybrid Gateway (Regex Pattern Engine + Token Classifier + Multimodal Threat Classifier + OCR Bounding Box Extractor)  
> **Primary Purpose:** Real-time PII masking, secret credential redaction, and prompt injection / jailbreak threat defense across Text, Images, PDFs, DOCX, and Video files.

---

## 1. Model Overview & Architecture

```
                    USER INPUT
         (Text / Image / PDF / DOCX / Video)
                       │
                       ▼
             MULTIMODAL EXTRACTION
            (OCR / Text / Audio STT)
                       │
                       ▼
          HYBRID DETECTION ARCHITECTURE
      ┌────────────────────────┬────────────────────────┐
      ▼                        ▼                        ▼
 Universal 20-Entity    Multimodal Threat        Deterministic Risk
 PII Regex & NER Engine  Injection Classifier     Scoring Engine (0-100)
      │                        │                        │
      └────────────────────────┼────────────────────────┘
                               ▼
                    POLICY DECISION ENGINE
           ┌───────────────────┼───────────────────┐
           ▼                   ▼                   ▼
      SAFE (0-25)     MODERATE/HIGH (26-75)  CRITICAL (76-100)
           │                   │                   │
         ALLOW          MASK & REDACT       BLOCK & QUARANTINE
           │                   │                   │
           └───────────────────┼───────────────────┘
                               ▼
                  SHA-256 AUDIT LOG TRACE
```

---

## 2. Evaluation Results (Tested on 1,000 Dataset Samples)

| Evaluation Metric Category | Metric | Score / Result |
| :--- | :--- | :--- |
| **PII Detection Precision** | Precision | **100.00%** |
| **PII Detection Recall** | Recall | **91.80%** |
| **PII F1-Score** | F1-Score | **95.72%** |
| **PII False Positive Rate (FPR)** | FPR | **0.00%** (0 false alarms) |
| **Prompt Injection Precision** | Precision | **100.00%** |
| **Prompt Injection Recall** | Recall | **64.00%** |
| **Prompt Injection F1-Score** | F1-Score | **78.05%** |
| **Processing Latency** | Latency | **< 45ms** (Text), **< 280ms** (Multimodal File) |

---

## 3. Supported Entity Categories (20 Universal Entities)

1. **Aadhaar Number** (`XXXX XXXX 9012`)
2. **PAN Number** (`XXXXX1234F`)
3. **Credit Card Number** (`XXXXXXXXXXXX4444`)
4. **Bank Account Number** (`XXXXXXX8901`)
5. **IFSC Code** (`SBINXXXX234`)
6. **UPI ID** (`s****@oksbi`)
7. **Email Address** (`s****@gmail.com`)
8. **Mobile Number** (`XXXXXX3210`)
9. **Passport Number** (`XXXX5678`)
10. **Driving License** (`TNXXXXXXXXX12345`)
11. **GST Number** (`33XXXXXXXXX1Z5`)
12. **Voter ID** (`XXXXX6789`)
13. **API Keys** (`sk_test_****`)
14. **JWT Tokens** (`[MASKED_JWT]`)
15. **Secret Keys** (`secret_****`)
16. **IP Address** (`XXX.XXX.1.100`)
17. **MAC Address** (`XX:XX:XX:XX:AB:CD`)
18. **Employee ID** (`EMPXXXX5`)
19. **Medical Record Number** (`MRN-XXXX54`)
20. **Prompt Injections & Jailbreaks** (DAN Payloads, Direct Overrides, Exfiltration)

---

## 4. Multimodal Format Performance Matrix

| Format | Format Support | Content Extraction Method | Sanitized File Redaction Output | Processing Status |
| :--- | :--- | :--- | :--- | :--- |
| **TEXT** | `.txt`, `.prompt` | Direct Unicode Text Parser | Masked Diff Text | **100% Active** |
| **IMAGE** | `.png`, `.jpg`, `.jpeg`, `.webp` | PIL / Tesseract OCR | Black-Box Visual Mask Image | **100% Active** |
| **PDF** | `.pdf` | PyPDF2 / Stream Reader | Redacted Text PDF Document | **100% Active** |
| **DOCX** | `.docx` | Paragraph & Table Zip XML | Sanitized DOCX Document | **100% Active** |
| **VIDEO** | `.mp4`, `.mov`, `.avi`, `.mkv` | Frame OCR & Speech Transcript | Redacted Frame & Transcript | **100% Active** |

---

## 5. Limitations & Safety Directives

- **Non-Standard Fonts in Images:** Low-resolution OCR text under 150 DPI or severely distorted text may require fallback manual verification.
- **Data Protection:** No real personal identification numbers or active production credentials are used.
