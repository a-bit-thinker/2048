# The 2-adic Absolute Galois Group

**Iterative proof likelihood score:** **3.7/10**  
Reason: computational experiments weakly constrain full profinite presentation.

## Programming-language expression

```python
ProblemSpec(
    name="The 2-adic Absolute Galois Group",
    inputs="candidate profinite presentation <Gens|Rels>",
    claim="Give correct presentation of Gal(Q_2^sep/Q_2).",
)
```

## Certificate and verifier

- Certificate: generator/relation system plus derived invariants.
- Verifier goal: check consistency against known finite quotients/invariants; not complete for full theorem.

```python
def verify_08_2adic_absolute_galois_group(instance, certificate) -> bool:
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
