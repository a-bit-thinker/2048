# Inverse Galois (M23)

- **Problem ID**: 09
- **Loop-Proof Likelihood Score (0-10)**: **6**

## Natural-language target
Find polynomial with Galois group M23.

## Programming-language expression
```text
SPEC:
Polynomial f(x) in Q[x]. Predicate gal_group(f)==M23 using resolvent/discriminant/local factorization tests.
```

## Certificate and verifier
- **Certificate format**: Certificate is polynomial coefficients + computed invariants + independent group checks.
- **Verifier**: Implement deterministic `verify_certificate(instance, certificate) -> bool`.

## Continuous-technique loop
1. Generate candidate constructions/proofs with search tooling.
2. Run verifier and property tests.
3. Keep best candidates, mutate strategy (SAT encoding, heuristics, symmetries, theorem lemmas).
4. Repeat until witness/counterexample/provable barrier appears.

## Why this score?
If found, verification is strong; failure to find is inconclusive.
