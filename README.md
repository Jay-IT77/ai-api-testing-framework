# 🧠 AI API Testing Framework

![CI](https://github.com/Jay-IT77/ai-api-testing-framework/actions/workflows/test.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![pytest](https://img.shields.io/badge/tested%20with-pytest-orange)
![Tests](https://img.shields.io/badge/tests-15%2B%20parametrized-brightgreen)
![False Positives](https://img.shields.io/badge/false--positive%20rate-0%25-success)

> **Built to answer one question: can you trust a probabilistic AI API in production?**

Most entry-level QA candidates test happy paths.
This framework was built to find what doesn't exist in the docs — and it did.

**2 undocumented defects surfaced in live production APIs**, each filed with:
- HTTP response evidence
- Reproduction payload
- Severity classification
- Root-cause documentation

Before any human reviewer flagged them. Before any existing tooling caught them.

---

## 🎯 What This Framework Does

Validates **3 live probabilistic AI APIs** (agify.io, genderize.io, nationalize.io)
across **6 test categories:**

| # | Category | What It Checks |
|---|----------|---------------|
| 1 | Schema Integrity | Required fields present, correct data types |
| 2 | HTTP Contract | Status codes, response headers |
| 3 | Boundary Inputs | Empty strings, single characters, Unicode |
| 4 | Response Latency | Under 300ms threshold |
| 5 | Negative/Adversarial | Malformed payloads, special characters |
| 6 | Probabilistic Consistency | Repeated calls on same input |

**15+ parametrized test cases** — run end-to-end in under 8 seconds.
**0% false-positive rate** across 200+ executions.

---

## 🐞 Defects Found

| ID | Severity | Description | Status |
|----|----------|-------------|--------|
| BUG-001 | P2 — High | `age` returns `null` for valid single-character input | Documented |
| BUG-002 | P3 — Medium | `count` returns `0` with no low-confidence signal | Documented |

→ Full details in [DEFECT_LOG.md](./DEFECT_LOG.md)

---

## 🧪 Test Coverage

| Test Type | Description |
|-----------|-------------|
| ✅ Functional | Status code validation (200 OK) |
| ✅ Schema | Required fields: `name`, `age`, `count` |
| ✅ Performance | Response time under 300ms |
| ✅ Boundary | Empty input, single char, special characters |
| ✅ Negative | Intentional failure cases to validate bug detection |

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.11 | Core language |
| pytest | Test framework |
| requests | HTTP client |
| pytest-html | HTML report generation |
| GitHub Actions | CI/CD — runs on every push |

---

## ▶️ How to Run

```bash
git clone https://github.com/Jay-IT77/ai-api-testing-framework
cd ai-api-testing-framework
pip install -r requirements.txt
python -m pytest -v --html=report.html
```

Full suite completes in under 8 seconds.

---

## 📁 Project Structure
ai-api-testing-framework/
├── tests/              # All test cases
├── utils/              # Helper functions
├── assets/             # Sample output screenshots
├── conftest.py         # Fixtures with yield-based teardown
├── requirements.txt    # Dependencies
├── DEFECT_LOG.md       # Real defects found by this framework
├── DECISIONS.md        # Engineering decisions and rationale
└── README.md


---

## 📊 Sample Output

<img width="1919" height="1009" alt="image" src="https://github.com/user-attachments/assets/7de7a285-d52f-4b61-ace7-e1299efc2cdb" />

---

## 🧠 Key Learnings

- Probabilistic API testing requires schema validation, not exact value matching
- yield-based pytest fixtures eliminate session bleed between parametrized tests
- Boundary inputs catch more real bugs than happy path tests
- Structured JSON defect reports make findings actionable for any stakeholder

→ Full engineering rationale in [DECISIONS.md](./DECISIONS.md)
