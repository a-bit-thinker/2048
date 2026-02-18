# 10 — Stretched Littlewood-Richardson Coefficients

```python
Problem(
  name="Stretched LR coefficients",
  domain={"λ,μ,ν": Partitions},
  claim="Find partitions where stretched LR polynomial has a negative coefficient",
  certificate=["(λ,μ,ν)", "polynomial expansion p(t)"],
  verifier="expand_stretched_lr(λ,μ,ν); check any coeff < 0",
  search=["symbolic-combinatorics enumeration", "integer-programming-guided search"]
)
```

- **Loop-proofability score:** 88/100
- **Most likely near-term outcome:** Explicit counterexample (false-for-all-positive-coeff hypothesis).
- **Why:** Finite witness can be exact and independently verifiable.
