# 03. The Arithmetic Kakeya Conjecture

## Problem (programming-language expression)
```python
# Given finite field/domain size q and dimensions, build sets minimizing size
# while containing required arithmetic/projection structures.
def construct_kakeya_set(q: int, d: int) -> set[tuple[int,...]]: ...
```

## Formalizable objects
- Finite-field vectors.
- Kakeya-like incidence constraints.
- Upper-bound objective on set size.

## Verifier sketch
```python
def verify_kakeya_constraints(S, q, d) -> bool:
    return contains_required_lines_or_progressions(S, q, d)
```

## Best loop style
Heuristic search + symbolic finite-field verification + bound tracking.

## Proof-by-iteration score
**6.5 / 10** (computational evidence is strong; general bound improvements need theory).
