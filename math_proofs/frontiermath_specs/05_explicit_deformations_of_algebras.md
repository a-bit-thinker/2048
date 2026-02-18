# 05. Explicit Deformations of Algebras

## Problem (programming-language expression)
```python
# Produce explicit deformation family A_t from curvilinear algebra to monomial algebra.
def construct_deformation(base_algebra) -> "DeformationFamily": ...
```

## Formalizable objects
- Algebra presentations via generators/relations.
- Flatness constraints and specialization maps.

## Verifier sketch
```python
def verify_deformation(family) -> bool:
    return checks_flatness(family) and endpoint_conditions(family)
```

## Best loop style
Computer algebra systems (Sage/Macaulay2/Singular) for symbolic checks.

## Proof-by-iteration score
**4.5 / 10** (computation helps examples, but deep structural proofs dominate).
