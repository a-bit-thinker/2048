# Degree vs Sensitivity for Boolean Functions

- **Problem ID**: 04
- **Loop-Proof Likelihood Score (0-10)**: **7**

## Natural-language target
Improve exponent in upper bounds relating boolean degree and sensitivity.

## Programming-language expression
```text
SPEC:
Boolean function f:{0,1}^n->{0,1}. Compute deg(f) and s(f). Objective: maximize ratio deg(f)/s(f)^alpha for tested n.
```

## Certificate and verifier
- **Certificate format**: Certificate is truth table or ANF coefficients. Verifier recomputes degree and sensitivity exactly.
- **Verifier**: Implement deterministic `verify_certificate(instance, certificate) -> bool`.

## Continuous-technique loop
1. Generate candidate constructions/proofs with search tooling.
2. Run verifier and property tests.
3. Keep best candidates, mutate strategy (SAT encoding, heuristics, symmetries, theorem lemmas).
4. Repeat until witness/counterexample/provable barrier appears.

## Why this score?
Strong finite verification, but asymptotic exponent improvement needs proof arguments.
