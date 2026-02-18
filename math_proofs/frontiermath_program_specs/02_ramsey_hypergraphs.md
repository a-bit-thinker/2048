# 02 — A Ramsey-style Problem on Hypergraphs

```python
Problem(
  name="A Ramsey-style Problem on Hypergraphs",
  domain={"n": Int, "k": Int, "r": Int},
  claim="Construct largest hypergraph avoiding target property P",
  certificate=["hypergraph edge set", "proof P is absent"],
  verifier="verify_property_absence(H, P)",
  search=["ILP", "SAT", "stochastic construction", "isomorphism pruning"]
)
```

- **Loop-proofability score:** 82/100
- **Most likely near-term outcome:** New best constructions + verified lower bounds.
- **Why:** Construction + verifier structure is ideal for iterative coding loops.
