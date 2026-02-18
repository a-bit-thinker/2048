# 05 — Explicit Deformations of Algebras

```python
Problem(
  name="Explicit Deformations of Algebras",
  domain={"A": FiniteDimensionalAlgebra},
  claim="Construct explicit deformation path from curvilinear algebra to monomial algebra",
  certificate=["deformation equations", "flatness/invariant checks"],
  verifier="verify_deformation_constraints(path)",
  search=["symbolic Gröbner-basis workflows", "template solving"]
)
```

- **Loop-proofability score:** 40/100
- **Most likely near-term outcome:** Verified examples, not full general theorem.
- **Why:** CAS can test candidates, but proving universality is hard.
