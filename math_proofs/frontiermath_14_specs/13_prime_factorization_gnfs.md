# Prime Factorization

- **Problem ID**: 13
- **Loop-Proof Likelihood Score (0-10)**: **6**

## Natural-language target
Improve constant factor in GNFS exponent.

## Programming-language expression
```text
SPEC:
Implement variant GNFS pipeline. Objective: minimize fitted constant c in runtime model exp((c+o(1))(log N)^(1/3)(log log N)^(2/3)).
```

## Certificate and verifier
- **Certificate format**: Certificate is benchmark suite, parameter schedule, and statistical fit report.
- **Verifier**: Implement deterministic `verify_certificate(instance, certificate) -> bool`.

## Continuous-technique loop
1. Generate candidate constructions/proofs with search tooling.
2. Run verifier and property tests.
3. Keep best candidates, mutate strategy (SAT encoding, heuristics, symmetries, theorem lemmas).
4. Repeat until witness/counterexample/provable barrier appears.

## Why this score?
Engineering gains verifiable experimentally; asymptotic proof of c-improvement is harder.
