# 06 — Surface with a High Number of Singularities

```python
Problem(
  name="Surface with many singularities",
  domain={"char": 3, "surface": DelPezzoKLT},
  claim="Construct example with >7 singular points",
  certificate=["explicit equations", "singularity classification report"],
  verifier="verify_klt_del_pezzo_and_count_singularities(surface)",
  search=["symbolic equation search", "invariant-guided optimization"]
)
```

- **Loop-proofability score:** 62/100
- **Most likely near-term outcome:** Either explicit witness (true) or stronger nonexistence evidence.
- **Why:** Concrete witness can be computationally verified once found.
