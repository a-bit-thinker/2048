# 11 — Symplectic Ball Packing

```python
Problem(
  name="Symplectic Ball Packing",
  domain={"epsilon": Real>0, "embeddings": SymplecticMaps},
  claim="Construct explicit embeddings filling all but ε volume",
  certificate=["embedding formulas/data", "symplectic condition checks", "volume estimate"],
  verifier="verify_symplectic_jacobian_and_volume(embeddings, epsilon)",
  search=["optimization over embedding ansatz", "computer-assisted inequalities"]
)
```

- **Loop-proofability score:** 46/100
- **Most likely near-term outcome:** Better constructions with numeric evidence; full proof harder.
- **Why:** Numerical validation helps but exact global proof is subtle.
