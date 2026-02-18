# 02. A Ramsey-style Problem on Hypergraphs

## Problem (programming-language expression)
```python
# Construct largest k-uniform hypergraph on n vertices
# avoiding forbidden property P.
def max_hypergraph_size_without_property(n: int, k: int, property_P) -> int: ...
```

## Formalizable objects
- `k`-uniform hypergraph as set of `k`-tuples.
- Predicate `property_P(H)` (easy-to-check but difficult-to-force pattern).

## Verifier sketch
```python
def verify_hypergraph(H) -> bool:
    return is_k_uniform(H) and not property_P(H)
```

## Best loop style
ILP/SAT search + local search mutation + exact property checker.

## Proof-by-iteration score
**8.0 / 10** (construction + checking is code-native; general extremal proof still nontrivial).
