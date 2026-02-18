# Apéry-style Irrationality Proofs

**Iterative proof likelihood score:** **4.6/10**  
Reason: experimental sequence discovery is possible; proof certificates are difficult.

## Programming-language expression

```python
ProblemSpec(
    name="Apéry-style Irrationality Proofs",
    inputs="constant c and candidate recurrence/series",
    claim="Adapt Apéry method to prove irrationality of c.",
)
```

## Certificate and verifier

- Certificate: sequence definitions + linear forms bounds.
- Verifier goal: check recurrence identities and inequality conditions for finite ranges; full asymptotic proof separate.

```python
def verify_12_apery_style_irrationality(instance, certificate) -> bool:
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
