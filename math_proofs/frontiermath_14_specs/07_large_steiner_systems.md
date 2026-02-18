# Large Steiner Systems

- **Problem ID**: 07
- **Loop-Proof Likelihood Score (0-10)**: **9**

## Natural-language target
Construct (n,q,r)-Steiner systems with n>q>r>5, r<10, n<200.

## Programming-language expression
```text
SPEC:
Universe V of size n; blocks B subset choose(V,q). Constraint: each r-subset appears in exactly one block.
```

## Certificate and verifier
- **Certificate format**: Certificate is full block list. Verifier counts coverage of all r-subsets exactly once.
- **Verifier**: Implement deterministic `verify_certificate(instance, certificate) -> bool`.

## Continuous-technique loop
1. Generate candidate constructions/proofs with search tooling.
2. Run verifier and property tests.
3. Keep best candidates, mutate strategy (SAT encoding, heuristics, symmetries, theorem lemmas).
4. Repeat until witness/counterexample/provable barrier appears.

## Why this score?
Excellent for looped search with exact verifier; concrete instances can be fully settled.
