# 14 — Unknotting Number = 1

```python
Problem(
  name="Unknotting Number = 1 decision algorithm",
  domain={"K": KnotDiagram},
  claim="Decide whether unknotting_number(K) == 1",
  certificate=["crossing change witness OR impossibility proof object"],
  verifier="verify_unknotting_certificate(K, cert)",
  search=["diagram simplification", "knot invariant pruning", "ML-guided branching"]
)
```

- **Loop-proofability score:** 74/100
- **Most likely near-term outcome:** Strong tested algorithm + partial correctness proofs.
- **Why:** Algorithmic framing is excellent, complete correctness proof remains hard.
