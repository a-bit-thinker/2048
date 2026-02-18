# 10. Stretched Littlewood-Richardson Coefficients

## Problem (programming-language expression)
```python
# Find partitions λ, μ, ν such that stretched LR polynomial has a negative coefficient.
def find_negative_stretched_lr(max_size: int) -> "Witness|None": ...
```

## Formalizable objects
- Partitions and LR coefficients.
- Polynomial interpolation from sampled stretch factors.

## Verifier sketch
```python
def verify_witness(lam, mu, nu) -> bool:
    poly = stretched_lr_polynomial(lam, mu, nu)
    return any(c < 0 for c in poly.coefficients())
```

## Best loop style
Exact symbolic combinatorics + exhaustive/pruned partition search.

## Proof-by-iteration score
**9.0 / 10** (witness-style problem with exact symbolic verifier).
