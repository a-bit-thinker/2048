# Ramsey Numbers for Book Graphs

**Iterative proof likelihood score:** **8.3/10**  
Reason: finite graph encodings + SAT certificates are strong.

## Programming-language expression

```python
ProblemSpec(
    name="Ramsey Numbers for Book Graphs",
    inputs="n, k, l, graph G on n vertices",
    claim="Find tight lower bound for off-diagonal Ramsey numbers of book graphs by constructing colorings avoiding target monochromatic books.",
)
```

## Certificate and verifier

- Certificate: edge-coloring assignment for complete graph.
- Verifier goal: check absence/presence of forbidden monochromatic book subgraphs and bound tightness for tested n.

```python
def verify_01_ramsey_book_graphs(instance, certificate) -> bool:
    """Deterministically validate the candidate against exact constraints."""
```

## Loop strategy

1. Search/generate candidate objects.
2. Run deterministic verifier.
3. Archive best bound/witness + failing counterexamples.
4. Mutate technique (SAT/SMT/ILP/symbolic/CAS/heuristic).
5. Repeat.

## True / false / unprovable status guidance

- A found **counterexample** disproves universal claim in tested formalization.
- A found **certificate** proves an existential instance (for the encoded constraints).
- For full theorem-level statements, pair this loop with formal proofs (Lean/Coq/Isabelle).
- "Unprovable" cannot be concluded from loop failure alone.
