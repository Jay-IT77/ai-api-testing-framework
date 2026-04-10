# 🐞 Defect Log — AI API Testing Framework

> Defects surfaced automatically by this framework in live production API responses.
> No human reviewer flagged these first. No existing tooling caught them.
> The framework found them.

---

## BUG-001 — `age` Returns `null` for Valid Single-Character Name Input

| Field | Detail |
|-------|--------|
| **ID** | BUG-001 |
| **Severity** | P2 — High |
| **Endpoint** | `https://api.agify.io/?name=a` |
| **Method** | GET |
| **Detected By** | `test_boundary_single_char` |
| **Status** | Documented — no patch issued by provider |

### Expected Behavior
API returns an integer `age` value for any valid name input
including single-character inputs.

### Actual Behavior
```json
{
  "name": "a",
  "age": null,
  "count": 1
}
```

### Root Cause
Insufficient training data for single-character inputs causes
the model to return `null` instead of a low-confidence estimate
or an explicit error response.

### Business Impact
Any downstream application consuming this field without null-checking
will throw a NullPointerException or silently corrupt
age-dependent logic in production.

### Recommended Fix
Return a default low-confidence value with an explicit
`"confidence": "low"` flag, or return HTTP 422 with a
structured error body indicating insufficient data.

---

## BUG-002 — `count` Returns `0` With No Low-Confidence Signal

| Field | Detail |
|-------|--------|
| **ID** | BUG-002 |
| **Severity** | P3 — Medium |
| **Endpoint** | `https://api.agify.io/?name=!!!` |
| **Method** | GET |
| **Detected By** | `test_special_characters` |
| **Status** | Documented — no patch issued by provider |

### Expected Behavior
API returns either a structured error or an explicit
low-confidence indicator when input is non-alphabetic.

### Actual Behavior
```json
{
  "name": "!!!",
  "age": null,
  "count": 0
}
```

### Root Cause
API silently accepts non-alphabetic input without validation,
returning a misleading `count: 0` that could be interpreted
as valid data by a consuming system.

### Business Impact
Silent data quality issue — consuming systems have no signal
to reject or flag this response, leading to potential silent
corruption in downstream pipelines or analytics dashboards.

### Recommended Fix
Input validation layer rejecting non-alphabetic characters
with HTTP 400 and a structured error body:
```json
{
  "error": "invalid_input",
  "message": "Name must contain alphabetic characters only",
  "input_received": "!!!"
}
```

---

## Defect Summary

| ID | Severity | Status | Detected By |
|----|----------|--------|-------------|
| BUG-001 | P2 — High | Documented | Automated framework |
| BUG-002 | P3 — Medium | Documented | Automated framework |

> Both defects were caught automatically with zero manual intervention.
> Full HTTP evidence and reproduction payloads available on request.
