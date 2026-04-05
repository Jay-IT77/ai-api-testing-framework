# 🧠 AI API Testing Framework (Advanced)

## 🚀 Overview

This project is a PyTest-based automation framework designed to test a probabilistic AI API that predicts age based on name inputs.

## 🎯 Objective

To validate API reliability, response structure, performance, and behavior under different input scenarios.

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

(Add screenshots here)

---

## 🧠 Key Learnings

* API testing using PyTest
* Fixtures and parametrization
* Schema validation
* Performance testing
* Debugging real-world issues

---

## 💬 Interview Summary

"I built a PyTest-based API testing framework that validates response structure, performance, and handles both positive and negative scenarios for a probabilistic AI system."
