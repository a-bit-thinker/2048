# 04. Degree vs Sensitivity for Boolean Functions

## Problem (programming-language expression)
```python
# Improve exponent c in degree(f) <= poly(sensitivity(f)).
def search_boolean_function_counterexamples(n: int) -> list[dict]: ...
```

## Formalizable objects
- Boolean function truth table `f: {0,1}^n -> {0,1}`.
- Sensitivity and polynomial degree exact computations.

## Verifier sketch
```python
def verify_stats(f) -> tuple[int,int]:
    return algebraic_degree(f), sensitivity(f)
```

## Best loop style
Exhaustive search for small `n`, genetic/heuristic search for larger `n`, symbolic ANF tools.

## Proof-by-iteration score
**7.0 / 10** (excellent finite experiments; asymptotic exponent proof needs new arguments).
