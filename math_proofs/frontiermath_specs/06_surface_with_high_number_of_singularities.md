# 06. Surface with a High Number of Singularities

## Problem (programming-language expression)
```python
# Find polynomial equation over characteristic 3 producing KLT del Pezzo
# with > 7 singular points.
def search_surface_model(char_p: int = 3) -> "SurfaceEquation": ...
```

## Formalizable objects
- Polynomial surface equations.
- Singularity finder, KLT and del Pezzo condition testers.

## Verifier sketch
```python
def verify_surface(surface) -> bool:
    return is_del_pezzo(surface) and is_KLT(surface) and singularity_count(surface) > 7
```

## Best loop style
CAS-assisted search + singularity classification scripts.

## Proof-by-iteration score
**5.0 / 10** (candidate checking programmable; classification proof burden remains high).
