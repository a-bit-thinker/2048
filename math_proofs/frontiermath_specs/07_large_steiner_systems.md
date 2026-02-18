# 07. Large Steiner Systems

## Problem (programming-language expression)
```python
# Construct (n, q, r)-Steiner system with n > q > r > 5, r < 10, n < 200.
def construct_steiner_system(n: int, q: int, r: int) -> list[set[int]]: ...
```

## Formalizable objects
- Blocks of size `q` on `n` points.
- Exact coverage constraint: each `r`-subset appears in exactly one block.

## Verifier sketch
```python
def verify_steiner(blocks, n, q, r) -> bool:
    return all(len(B)==q for B in blocks) and exact_r_subset_coverage(blocks, n, r)
```

## Best loop style
SAT/ILP + symmetry breaking + exact verifier with certificate export.

## Proof-by-iteration score
**9.5 / 10** (best target: concrete construction claims can be fully machine-verified).
