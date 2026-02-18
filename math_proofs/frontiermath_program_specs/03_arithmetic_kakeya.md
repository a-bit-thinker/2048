# 03 — The Arithmetic Kakeya Conjecture

```python
Problem(
  name="Arithmetic Kakeya Conjecture",
  domain={"q": PrimePower, "n": Int>=2},
  claim="Improve upper bounds via explicit combinatorial constructions",
  certificate=["set/structure S", "computed bound certificate"],
  verifier="verify_kakeya_bound(S, q, n)",
  search=["finite-field construction", "additive-combinatorics heuristics"]
)
```

- **Loop-proofability score:** 55/100
- **Most likely near-term outcome:** Better empirical/computational bounds, partial true results.
- **Why:** Many checks are computational, but theorem-level breakthroughs require deep theory.
