# 07 — Large Steiner Systems

```python
Problem(
  name="Large Steiner Systems",
  domain={"n,q,r": Int, "n>q>r>5", "r<10", "n<200"},
  claim="Construct (n,q,r)-Steiner system",
  certificate=["block family B"],
  verifier="for each r-subset, count_containing_blocks == 1",
  search=["SAT/ILP", "exact cover", "group-action constructions"]
)
```

- **Loop-proofability score:** 90/100
- **Most likely near-term outcome:** Constructive success with full machine verification.
- **Why:** Perfect for certificate + deterministic verifier loops.
