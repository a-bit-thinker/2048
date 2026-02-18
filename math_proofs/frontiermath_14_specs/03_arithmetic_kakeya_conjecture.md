# The Arithmetic Kakeya Conjecture

- **Problem ID**: 03
- **Loop-Proof Likelihood Score (0-10)**: **5**

## Natural-language target
Improve best known upper bounds via combinatorial constructions.

## Programming-language expression
```text
SPEC:
Encode finite field F_q^n sets S and direction set D. Predicate kakeya_like(S,D) checks line-direction coverage constraints.
```

## Certificate and verifier
- **Certificate format**: Certificate is explicit set S with metadata proving constraints.
- **Verifier**: Implement deterministic `verify_certificate(instance, certificate) -> bool`.

## Continuous-technique loop
1. Generate candidate constructions/proofs with search tooling.
2. Run verifier and property tests.
3. Keep best candidates, mutate strategy (SAT encoding, heuristics, symmetries, theorem lemmas).
4. Repeat until witness/counterexample/provable barrier appears.

## Why this score?
Computational verification helps for candidates; full bound proof rarely computation-only.
