# Surface with a High Number of Singularities

- **Problem ID**: 06
- **Loop-Proof Likelihood Score (0-10)**: **4**

## Natural-language target
Construct KLT del Pezzo surface in characteristic 3 with >7 singular points.

## Programming-language expression
```text
SPEC:
Surface X defined by polynomial equations over F_3. Predicate is_klt_del_pezzo(X) and singular_count(X)>7.
```

## Certificate and verifier
- **Certificate format**: Certificate is explicit equations + local invariant computations.
- **Verifier**: Implement deterministic `verify_certificate(instance, certificate) -> bool`.

## Continuous-technique loop
1. Generate candidate constructions/proofs with search tooling.
2. Run verifier and property tests.
3. Keep best candidates, mutate strategy (SAT encoding, heuristics, symmetries, theorem lemmas).
4. Repeat until witness/counterexample/provable barrier appears.

## Why this score?
Candidate verification possible but rigorous classification arguments remain difficult.
