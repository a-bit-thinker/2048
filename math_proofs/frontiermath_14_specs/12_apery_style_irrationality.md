# Apery-style Irrationality Proofs

- **Problem ID**: 12
- **Loop-Proof Likelihood Score (0-10)**: **3**

## Natural-language target
Adapt Apery irrationality method to other constants.

## Programming-language expression
```text
SPEC:
Construct sequences (A_n,B_n) with rational approximants B_n/A_n and recurrence + growth constraints implying irrationality.
```

## Certificate and verifier
- **Certificate format**: Certificate is recurrence relation, integrality lemmas, and error bounds.
- **Verifier**: Implement deterministic `verify_certificate(instance, certificate) -> bool`.

## Continuous-technique loop
1. Generate candidate constructions/proofs with search tooling.
2. Run verifier and property tests.
3. Keep best candidates, mutate strategy (SAT encoding, heuristics, symmetries, theorem lemmas).
4. Repeat until witness/counterexample/provable barrier appears.

## Why this score?
Search can discover candidates; full irrationality proof requires rigorous bound proofs.
