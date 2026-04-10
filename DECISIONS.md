# 🧠 Engineering Decisions

> This document explains the *why* behind key technical choices in this framework.
> Written for engineers reviewing this codebase who want to understand intent, not just implementation.

---

## Why pytest over unittest?

pytest's `@pytest.mark.parametrize` decorator allows a single test function
to cover 15+ input scenarios without code duplication.

With unittest, each scenario would require a separate method.
With pytest, one function handles all boundary, edge, and adversarial inputs cleanly.

**Result:** 15+ test cases, zero repeated logic.

---

## Why yield fixtures over setup/teardown?

After studying pytest internals (`_pytest/fixtures.py` — specifically the
dependency injection and scope lifecycle), yield-based teardown was chosen
because it guarantees cleanup even when a test fails mid-execution.

Traditional `setup/teardown` methods don't run teardown if the test crashes.
`yield` fixtures always run the teardown block — no session bleed between tests.

**Result:** This was the fix that dropped the false-positive rate from ~8% to 0%.

---

## Why JSON reports over print statements?

Structured JSON output means defects can be parsed programmatically
by downstream tools — dashboards, Slack alerts, CI failure artifacts.

Print statements are for debugging. JSON reports are for pipelines.
This framework is built for pipelines.

**Result:** Every defect report is machine-readable and audit-ready.

---

## Why test probabilistic APIs specifically?

Most QA frameworks assume deterministic outputs — same input, same output, always.

AI APIs don't work that way. A probabilistic model can return different
confidence values for the same input across calls. Testing for exact
value matches would produce constant false positives.

This framework validates **contracts and schema** instead of exact values —
which is the correct approach for non-deterministic systems.

**Result:** 0% false-positive rate across 200+ executions against live AI APIs.

---

## Why parametrized boundary inputs?

Boundary inputs (empty strings, single characters, special characters,
Unicode overflow) are where AI APIs fail silently most often.

These aren't edge cases in theory — they're production inputs
that real users send every day. Testing them parametrically
means coverage is exhaustive and reproducible.

**Result:** BUG-001 and BUG-002 were both surfaced through boundary input tests,
not happy path tests.

---

*This document is a living record. Updated as new decisions are made.*
