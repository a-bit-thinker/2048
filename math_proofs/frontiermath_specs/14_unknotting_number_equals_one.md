# 14. Unknotting Number = 1

## Problem (programming-language expression)
```python
# Decide whether a knot has unknotting number exactly 1.
def decide_unknotting_number_one(knot_diagram: "Diagram") -> bool: ...
```

## Formalizable objects
- Knot diagrams / Gauss codes.
- Crossing-change operations.
- Equivalence checking to unknot via invariants + normalization.

## Verifier sketch
```python
def verify_decision(knot, answer) -> bool:
    if answer:
        return exists_single_crossing_change_to_unknot(knot)
    return proven_no_single_change_works(knot)
```

## Best loop style
Algorithm design + exhaustive tests on knot tables + certificate traces.

## Proof-by-iteration score
**8.0 / 10** (algorithmic core is strong; full correctness proof still essential).
