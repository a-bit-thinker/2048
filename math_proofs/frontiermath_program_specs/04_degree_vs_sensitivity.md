# 04 — Degree vs Sensitivity for Boolean Functions

```python
Problem(
  name="Degree vs Sensitivity",
  domain={"f": BooleanFunction({0,1}^n -> {0,1})},
  claim="Improve exponent in upper bound deg(f) <= C * s(f)^alpha",
  certificate=["family of functions", "symbolic or exhaustive sensitivity/degree data"],
  verifier="compute_degree_and_sensitivity(f)",
  search=["exhaustive search small n", "genetic search", "SAT over truth tables"]
)
```

- **Loop-proofability score:** 73/100
- **Most likely near-term outcome:** Better constants/exponents for restricted families.
- **Why:** Finite checks are exact; asymptotic proof still difficult.
