# 08 — The 2-adic Absolute Galois Group

```python
Problem(
  name="2-adic Absolute Galois Group",
  domain={"G": ProfiniteGroup},
  claim="Give explicit presentation of Gal(Q_2^bar / Q_2)",
  certificate=["generators", "relations", "isomorphism proof objects"],
  verifier="verify_profinite_presentation_equivalence(candidate, target)",
  search=["cohomology computations", "profinite relation mining"]
)
```

- **Loop-proofability score:** 25/100
- **Most likely near-term outcome:** Computational evidence and partial structure; full proof remains hard.
- **Why:** Encoding possible, but complete verification needs heavy abstract theory.
