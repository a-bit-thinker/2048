# A Ramsey-style Problem on Hypergraphs

**Iterative proof likelihood score:** **8.4/10**  
Reason: hypergraph constraints are machine-checkable and searchable.

## Programming-language expression

```python
ProblemSpec(
    name="A Ramsey-style Problem on Hypergraphs",
    inputs="uniformity r, vertex count n, hypergraph H",
    claim="Maximize size of hypergraph family avoiding a specific forbidden property.",
)
```

## Certificate and verifier

- Certificate: incidence list of hyperedges.
- Verifier goal: validate uniformity, size, and forbidden-property absence.

```python
def verify_02_ramsey_hypergraphs(instance, certificate) -> bool:
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
