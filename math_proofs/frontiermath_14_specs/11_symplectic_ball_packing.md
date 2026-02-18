# Symplectic Ball Packing

- **Problem ID**: 11
- **Loop-Proof Likelihood Score (0-10)**: **5**

## Natural-language target
Find explicit near-full-volume symplectic embeddings.

## Programming-language expression
```text
SPEC:
Map phi: disjoint union of balls -> target ball with symplectic Jacobian constraints and volume deficit <= epsilon.
```

## Certificate and verifier
- **Certificate format**: Certificate is explicit embedding formulas plus symbolic/numeric constraint checks.
- **Verifier**: Implement deterministic `verify_certificate(instance, certificate) -> bool`.

## Continuous-technique loop
1. Generate candidate constructions/proofs with search tooling.
2. Run verifier and property tests.
3. Keep best candidates, mutate strategy (SAT encoding, heuristics, symmetries, theorem lemmas).
4. Repeat until witness/counterexample/provable barrier appears.

## Why this score?
Numerical evidence useful; full geometric proof usually needs analytic arguments.
