# 13. Prime Factorization (GNFS constant improvement)

## Problem (programming-language expression)
```python
# Improve constant factor in GNFS exponent by algorithmic innovation.
def optimize_gnfs_pipeline(instance_set: list[int]) -> "AlgorithmVariant": ...
```

## Formalizable objects
- GNFS parameter schedule.
- Runtime/cost model and empirical benchmark suite.

## Verifier sketch
```python
def verify_improvement(variant, baseline, instances) -> bool:
    return complexity_model_gain(variant, baseline) and benchmark_gain(variant, baseline, instances)
```

## Best loop style
Engineering loop: profiling, parameter search, asymptotic model fitting.

## Proof-by-iteration score
**7.5 / 10** (highly programmable for empirical + model evidence, asymptotic proof still hard).
