# Ramsey Numbers for Book Graphs

- **Problem ID**: 01
- **Loop-Proof Likelihood Score (0-10)**: **8**

## Natural-language target
Find tight lower bounds on off-diagonal Ramsey numbers for book graphs.

## Programming-language expression
```text
SPEC:
Define graph G=(V,E). Predicate has_book(G,k) checks whether G contains book graph B_k. Goal: maximize n where exists edge-coloring c: E(K_n)->{red,blue} such that red avoids B_a and blue avoids B_b.
```

## Certificate and verifier
- **Certificate format**: Certificate is a coloring table for K_n. Verifier checks all candidate k-book subgraphs in both colors.
- **Verifier**: Implement deterministic `verify_certificate(instance, certificate) -> bool`.

## Continuous-technique loop
1. Generate candidate constructions/proofs with search tooling.
2. Run verifier and property tests.
3. Keep best candidates, mutate strategy (SAT encoding, heuristics, symmetries, theorem lemmas).
4. Repeat until witness/counterexample/provable barrier appears.

## Why this score?
Finite instances are exactly checkable; asymptotic tight lower bounds still hard.
