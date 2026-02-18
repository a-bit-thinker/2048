# Prime Factorization (GNFS constant)

**Iterative proof likelihood score:** **7.1/10**  
Reason: algorithmic optimization loop is strong though asymptotic proof is hard.

## Programming-language expression

```python
ProblemSpec(
    name="Prime Factorization (GNFS constant)",
    inputs="integer size N, GNFS pipeline parameters",
    claim="Improve constant in exponent for GNFS complexity.",
)
```

## Certificate and verifier

- Certificate: algorithmic variant + complexity derivation + benchmark traces.
- Verifier goal: reproduce runtime model and empirical scaling on benchmark suite.

```python
def verify_13_prime_factorization_constant(instance, certificate) -> bool:
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
