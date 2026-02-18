# 01 — Ramsey Numbers for Book Graphs

```python
Problem(
  name="Ramsey Numbers for Book Graphs",
  domain={"n": Int>=2, "m": Int>=2},
  claim="Find tight lower bound L(n,m) for off-diagonal book-graph Ramsey number R(B_n, B_m)",
  certificate=["2-coloring of complete graph K_t", "proof no monochromatic B_n/B_m exists"],
  verifier="check_coloring_avoids_book_graph(coloring, n, m)",
  search=["SAT/SMT encoding", "local search", "symmetry breaking"]
)
```

- **Loop-proofability score:** 78/100
- **Most likely near-term outcome:** Prove better bounds (true statements) for new parameter ranges.
- **Why:** Candidate constructions can be machine-checked exactly; global tightness still hard.
