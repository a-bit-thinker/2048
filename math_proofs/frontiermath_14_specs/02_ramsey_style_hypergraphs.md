# A Ramsey-style Problem on Hypergraphs

- **Problem ID**: 02
- **Loop-Proof Likelihood Score (0-10)**: **8**

## Natural-language target
Construct largest hypergraphs avoiding a specific forbidden property.

## Programming-language expression
```text
SPEC:
Represent r-uniform hypergraph H=(V,E). Predicate forbidden(H) returns True if forbidden structure exists.
```

## Certificate and verifier
- **Certificate format**: Certificate is edge set E. Verifier runs exact forbidden-substructure detector.
- **Verifier**: Implement deterministic `verify_certificate(instance, certificate) -> bool`.

## Continuous-technique loop
1. Generate candidate constructions/proofs with search tooling.
2. Run verifier and property tests.
3. Keep best candidates, mutate strategy (SAT encoding, heuristics, symmetries, theorem lemmas).
4. Repeat until witness/counterexample/provable barrier appears.

## Why this score?
Great for constructive search; general extremal theorem likely needs theory.
