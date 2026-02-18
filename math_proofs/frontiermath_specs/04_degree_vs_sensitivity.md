# Degree vs Sensitivity for Boolean Functions

**Iterative proof likelihood score:** **7.4/10**  
Reason: boolean-function exhaustive search works for finite n.

## Programming-language expression

```python
ProblemSpec(
    name="Degree vs Sensitivity for Boolean Functions",
    inputs="boolean function f:{0,1}^n->{0,1}",
    claim="Improve exponent in upper bound relating polynomial degree to sensitivity.",
)
```

## Certificate and verifier

- Certificate: truth table plus computed metrics (deg(f), s(f)).
- Verifier goal: recompute degree/sensitivity exactly and confirm inequality improvement on searched regime.

```python
def verify_04_degree_vs_sensitivity(instance, certificate) -> bool:
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
