# 09. Inverse Galois (Mathieu group M23)

## Problem (programming-language expression)
```python
# Find polynomial f(x) in Q[x] with Gal(f/Q) ≅ M23.
def search_polynomial_with_galois_group_M23(bounds: dict) -> "Polynomial|None": ...
```

## Formalizable objects
- Rational polynomials and discriminants.
- Galois group computation/identification routines.

## Verifier sketch
```python
def verify_M23(polynomial) -> bool:
    return galois_group(polynomial) == "M23"
```

## Best loop style
Guided search (invariants + templates) + exact group computation for candidates.

## Proof-by-iteration score
**6.0 / 10** (if a candidate is found, verification is strong; search space is difficult).
