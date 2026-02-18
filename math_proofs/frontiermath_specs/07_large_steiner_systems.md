# Large Steiner Systems

**Iterative proof likelihood score:** **9.0/10**  
Reason: exact combinatorial construction and verification align perfectly with code.

## Programming-language expression

```python
ProblemSpec(
    name="Large Steiner Systems",
    inputs="integers n,q,r with n>q>r>5, r<10, n<200",
    claim="Construct an (n,q,r)-Steiner system meeting incidence uniqueness conditions.",
)
```

## Certificate and verifier

- Certificate: block collection B, each block size q.
- Verifier goal: every r-subset appears in exactly one block; parameter constraints hold.

```python
def verify_07_large_steiner_systems(instance, certificate) -> bool:
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
