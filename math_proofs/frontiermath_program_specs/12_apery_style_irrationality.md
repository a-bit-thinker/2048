# 12 — Apéry-style Irrationality Proofs

```python
Problem(
  name="Apéry-style Irrationality Proofs",
  domain={"constant": RealNumber},
  claim="Produce Apéry-style irrationality proof for new constants",
  certificate=["recurrence/sequence", "linear forms", "growth bounds"],
  verifier="check_recurrence_and_bound_chain(certificate)",
  search=["integer-relation discovery", "symbolic recurrence mining"]
)
```

- **Loop-proofability score:** 33/100
- **Most likely near-term outcome:** Heuristic discoveries; rigorous endgame still difficult.
- **Why:** Program search can suggest proof skeletons, but hard inequalities dominate.
