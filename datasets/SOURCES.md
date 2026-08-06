# Open Security Datasets & Corpus Metadata (`datasets/SOURCES.md`)

This document records all external open datasets and synthetic dataset resources used for training, evaluating, and benchmarking the **SecureLLM Shield** hybrid multimodal detection engine.

---

## Public & Open Security Datasets

| Dataset Name | Source / Repository | License | Sample Count | Supported Data Types | Categories / Labels | Intended Use |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **`ai4privacy/pii-masking-200k`** | [HuggingFace Datasets](https://huggingface.co/datasets/ai4privacy/pii-masking-200k) | MIT License | 200,000 | Multi-language Text | Global PII, Names, Addresses, Phones, Credit Cards | PII Detection & Token Masking Benchmark |
| **`deepset/prompt-injections`** | [HuggingFace Datasets](https://huggingface.co/datasets/deepset/prompt-injections) | Apache 2.0 | 660 | English Text | Direct Prompt Injection, System Override | Prompt Injection Classifier Training |
| **`fmops/jailbreak-prompts`** | [HuggingFace Datasets](https://huggingface.co/datasets/fmops/jailbreak-prompts) | MIT License | 1,400 | English Text | DAN Jailbreak, Roleplay Persona Override | Jailbreak Threat Evaluation |
| **`OWASP LLM Top 10 Corpus`** | [OWASP Security Project](https://owasp.org/www-project-top-10-for-large-language-model-applications/) | Creative Commons | 500+ Attack Patterns | Multimodal / Text | LLM01 Prompt Injection, LLM06 Sensitive Disclosure | Vulnerability Classification Rules |
| **`SecureLLM Shield Synthetic Corpus`** | Internal Synthetic Generator (`scripts/generate_synthetic_data.py`) | Open Apache 2.0 | 1,000 | Text, OCR Image, PDF, DOCX, Video | Indian PII (Aadhaar, PAN, Bank, IFSC, UPI), Secrets, DAN Injections | Continuous Pipeline Evaluation |

---

## Privacy & Safety Directives

> [!IMPORTANT]
> 1. **Zero Real Personal Data:** Absolutely no real Aadhaar numbers, PAN numbers, bank accounts, passwords, API keys, or private identity data are stored or processed.
> 2. **Synthetic Pattern Safety:** All PII samples are synthetically generated using non-functional random digits, letters, and mock domains (`mockdomain.org`, `example.com`).
> 3. **Reproducibility:** The pipeline is fully reproducible using `python scripts/generate_synthetic_data.py`.
