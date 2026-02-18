# Unknotting Number = 1

- **Problem ID**: 14
- **Loop-Proof Likelihood Score (0-10)**: **7**

## Natural-language target
Decide whether a knot has unknotting number exactly 1.

## Programming-language expression
```text
SPEC:
Input knot diagram D. Output bool unknotting_one(D). Specification: exists crossing change yielding unknot.
```

## Certificate and verifier
- **Certificate format**: Certificate for YES: crossing index + Reidemeister simplification trace to unknot. For NO: obstruction invariants.
- **Verifier**: Implement deterministic `verify_certificate(instance, certificate) -> bool`.

## Continuous-technique loop
1. Generate candidate constructions/proofs with search tooling.
2. Run verifier and property tests.
3. Keep best candidates, mutate strategy (SAT encoding, heuristics, symmetries, theorem lemmas).
4. Repeat until witness/counterexample/provable barrier appears.

## Why this score?
Algorithm behavior testable on corpora; full correctness proof remains substantial.
