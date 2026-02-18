# 13 — Prime Factorization (GNFS constant improvement)

```python
Problem(
  name="Prime Factorization / GNFS constant",
  domain={"N": Semiprime, "algorithm": GNFSVariant},
  claim="Improve constant factor in exponent of GNFS runtime",
  certificate=["algorithm design", "asymptotic analysis", "benchmark suite"],
  verifier="reproduce_complexity_derivation_and_benchmarks(algorithm)",
  search=["parameter tuning", "pipeline redesign", "hardware-aware profiling"]
)
```

- **Loop-proofability score:** 61/100
- **Most likely near-term outcome:** Engineering speedups; asymptotic proof improvements are harder.
- **Why:** Benchmarks are easy to automate, theoretical constant proofs are subtle.
