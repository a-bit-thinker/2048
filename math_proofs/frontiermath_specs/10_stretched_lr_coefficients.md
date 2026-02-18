# Stretched Littlewood-Richardson Coefficients

**Iterative proof likelihood score:** **8.8/10**  
Reason: search + exact symbolic coefficient extraction is very automatable.

## Programming-language expression

```python
ProblemSpec(
    name="Stretched Littlewood-Richardson Coefficients",
    inputs="partitions lambda, mu, nu; stretch t",
    claim="Find partitions where stretched LR polynomial has a negative coefficient.",
)
```

## Certificate and verifier

- Certificate: specific partitions and polynomial expansion.
- Verifier goal: recompute stretched LR polynomial exactly and detect negative coefficient.

```python
def verify_10_stretched_lr_coefficients(instance, certificate) -> bool:
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
