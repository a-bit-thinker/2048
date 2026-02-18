# Unknotting Number = 1

**Iterative proof likelihood score:** **7.8/10**  
Reason: decision procedures and counterexample tests are programmable.

## Programming-language expression

```python
ProblemSpec(
    name="Unknotting Number = 1",
    inputs="knot diagram D",
    claim="Decide whether unknotting number u(K)=1.",
)
```

## Certificate and verifier

- Certificate: crossing-change witness or obstruction certificate.
- Verifier goal: validate witness transforms knot to unknot, or verify obstruction invariants.

```python
def verify_14_unknotting_number_one(instance, certificate) -> bool:
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
