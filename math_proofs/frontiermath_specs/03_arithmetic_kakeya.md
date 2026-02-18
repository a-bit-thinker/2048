# The Arithmetic Kakeya Conjecture

**Iterative proof likelihood score:** **6.8/10**  
Reason: construction search and bound computation are programmable, full proof is hard.

## Programming-language expression

```python
ProblemSpec(
    name="The Arithmetic Kakeya Conjecture",
    inputs="finite field/ring parameters q, dimension d, set S",
    claim="Improve upper bounds by constructing combinatorial objects satisfying direction-cover constraints.",
)
```

## Certificate and verifier

- Certificate: explicit set family and directional coverage map.
- Verifier goal: check coverage conditions and computed bound value.

```python
def verify_03_arithmetic_kakeya(instance, certificate) -> bool:
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
