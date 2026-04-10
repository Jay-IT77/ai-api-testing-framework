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

## 🧪 Test Coverage

### ✅ Functional Testing

* Status code validation (200 OK)

### ✅ Schema Validation

* Ensures response contains:

  * name
  * age
  * count

### ✅ Performance Testing

* Response time validation (< 1 second)

### ✅ Edge Case Testing

* Empty input ("")
* Special characters ("!!!")

### ❌ Negative Testing

* Intentional failure cases to validate bug detection

---

## 🛠️ Tech Stack

* Python
* PyTest
* Requests
* PyTest-HTML

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
python -m pytest -v --html=report.html
```

---

## 📊 Sample Output

<img width="1919" height="1009" alt="image" src="https://github.com/user-attachments/assets/7de7a285-d52f-4b61-ace7-e1299efc2cdb" />



---

## 🧠 Key Learnings

* API testing using PyTest
* Fixtures and parametrization
* Schema validation
* Performance testing
* Debugging real-world issues

---



"I built a PyTest-based API testing framework that validates response structure, performance, and handles both positive and negative scenarios for a probabilistic AI system."
