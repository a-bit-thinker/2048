# 12. Apéry-style Irrationality Proofs

## Problem (programming-language expression)
```python
# Discover recurrences / rational approximants giving irrationality proofs
# similar to Apéry's method.
def search_apery_style_scheme(target_constant: str) -> "ProofScheme|None": ...
```

## Formalizable objects
- Integer sequences, recurrences, linear forms.
- Growth and approximation-rate inequalities.

## Verifier sketch
```python
def verify_scheme_candidate(scheme) -> bool:
    return checks_integrality(scheme) and checks_error_decay(scheme)
```

## Best loop style
Experimental mathematics + symbolic summation + later formalization.

## Proof-by-iteration score
**4.0 / 10** (excellent hypothesis generator, but final proof is delicate).
