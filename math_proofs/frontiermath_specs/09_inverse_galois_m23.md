# Inverse Galois (M23 polynomial)

**Iterative proof likelihood score:** **6.2/10**  
Reason: candidate polynomial verification is exact once found.

## Programming-language expression

```python
ProblemSpec(
    name="Inverse Galois (M23 polynomial)",
    inputs="polynomial p(x) in Q[x]",
    claim="Find polynomial with Galois group M23.",
)
```

## Certificate and verifier

- Certificate: polynomial coefficients + resolvent data.
- Verifier goal: compute Galois group (or certify subgroup ladder) and confirm isomorphism to M23.

```python
def verify_09_inverse_galois_m23(instance, certificate) -> bool:
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
