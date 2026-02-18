# 09 — Inverse Galois (Mathieu group M23)

```python
Problem(
  name="Inverse Galois for M23",
  domain={"f": Polynomial(Q[x])},
  claim="Find f with Gal(f) ≅ M23",
  certificate=["explicit polynomial f", "Galois-group computation transcript"],
  verifier="verify_galois_group(f) == M23",
  search=["parametric polynomial families", "specialization + resolvent filters"]
)
```

- **Loop-proofability score:** 67/100
- **Most likely near-term outcome:** If candidate found, proof is checkable; otherwise inconclusive search.
- **Why:** Witness-verification is strong, discovery space is huge.
