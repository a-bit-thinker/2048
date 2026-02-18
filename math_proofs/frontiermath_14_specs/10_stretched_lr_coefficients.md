# Stretched Littlewood-Richardson Coefficients

- **Problem ID**: 10
- **Loop-Proof Likelihood Score (0-10)**: **9**

## Natural-language target
Find partitions with stretched LR polynomial having a negative coefficient.

## Programming-language expression
```text
SPEC:
For partitions lambda,mu,nu define P(t)=c_{t lambda, t mu}^{t nu}. Goal: find coefficient a_i<0 in P(t).
```

## Certificate and verifier
- **Certificate format**: Certificate is (lambda,mu,nu), explicit polynomial P(t), and coefficient index i.
- **Verifier**: Implement deterministic `verify_certificate(instance, certificate) -> bool`.

## Continuous-technique loop
1. Generate candidate constructions/proofs with search tooling.
2. Run verifier and property tests.
3. Keep best candidates, mutate strategy (SAT encoding, heuristics, symmetries, theorem lemmas).
4. Repeat until witness/counterexample/provable barrier appears.

## Why this score?
Concrete witnesses are highly machine-verifiable with exact arithmetic.
