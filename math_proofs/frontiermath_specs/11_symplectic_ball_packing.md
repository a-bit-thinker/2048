# 11. Symplectic Ball Packing

## Problem (programming-language expression)
```python
# Construct explicit symplectic embeddings of many balls into one target ball
# with volume loss <= epsilon.
def construct_symplectic_packing(epsilon: float) -> "EmbeddingData": ...
```

## Formalizable objects
- Hamiltonian maps / embedding parameterizations.
- Volume and non-overlap constraints.

## Verifier sketch
```python
def verify_embedding(data, epsilon) -> bool:
    return approx_symplectic_condition(data) and occupied_volume(data) >= 1 - epsilon
```

## Best loop style
Numerical optimization + symbolic validation where possible.

## Proof-by-iteration score
**5.5 / 10** (great for experimental geometry, complete proof usually needs theory).
