# 01. Ramsey Numbers for Book Graphs

## Problem (programming-language expression)
```python
# Find largest N such that there exists a 2-coloring of edges of K_N
# avoiding red book graph B_red and blue book graph B_blue.
def exists_coloring_without_books(N: int, red_params: tuple[int,int], blue_params: tuple[int,int]) -> bool: ...
```

## Formalizable objects
- Complete graph `K_N`
- Edge-coloring `c: E(K_N) -> {0,1}`
- Forbidden patterns as subgraph-isomorphism predicates for book graphs.

## Verifier sketch
```python
def verify_certificate(cert_coloring) -> bool:
    return no_red_book(cert_coloring) and no_blue_book(cert_coloring)
```

## Best loop style
SAT/SMT encoding with incremental `N` and UNSAT certificates.

## Proof-by-iteration score
**8.5 / 10** (very algorithmic with strong certificates, but tight asymptotic lower bounds still hard).
