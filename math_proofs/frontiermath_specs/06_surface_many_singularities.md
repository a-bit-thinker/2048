# Surface with a High Number of Singularities

**Iterative proof likelihood score:** **4.9/10**  
Reason: CAS can verify candidate singularities but existence proof is subtle.

## Programming-language expression

```python
ProblemSpec(
    name="Surface with a High Number of Singularities",
    inputs="surface equation over char 3 field",
    claim="Exhibit KLT del Pezzo surface with >7 singular points.",
)
```

## Certificate and verifier

- Certificate: explicit polynomial defining surface + singularity list.
- Verifier goal: differentiate, locate singular points, and check count plus local criteria.

```python
def verify_06_surface_many_singularities(instance, certificate) -> bool:
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
