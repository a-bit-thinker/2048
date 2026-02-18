# FrontierMath 14 problems as programming-language specifications

This directory expresses each FrontierMath open problem as a software-oriented spec:

- `inputs` and domain constraints,
- `claim` in logic-like form,
- `certificate` structure,
- `verifier` signature,
- and a score for iterative proof search.

## Scoring rubric: "iterative proof likelihood"

Score from **1 to 10** for how likely a Ralph/Codex loop can make meaningful progress through repeated technique changes.

- **9-10**: Strong for computational search + exact certificate checking.
- **6-8**: Can do substantial computational progress, but full proof likely needs deep theory.
- **3-5**: Programming helps with experiments/examples; theorem-level proof still mostly human/formal-method heavy.
- **1-2**: Computation has limited leverage on full claim.

## Ranked list (most promising first)

1. `07_large_steiner_systems.md` — **9.0**
2. `10_stretched_lr_coefficients.md` — **8.8**
3. `02_ramsey_hypergraphs.md` — **8.4**
4. `01_ramsey_book_graphs.md` — **8.3**
5. `14_unknotting_number_one.md` — **7.8**
6. `04_degree_vs_sensitivity.md` — **7.4**
7. `13_prime_factorization_constant.md` — **7.1**
8. `03_arithmetic_kakeya.md` — **6.8**
9. `09_inverse_galois_m23.md` — **6.2**
10. `11_symplectic_ball_packing.md` — **5.6**
11. `05_explicit_deformations_algebras.md` — **5.2**
12. `06_surface_many_singularities.md` — **4.9**
13. `12_apery_style_irrationality.md` — **4.6**
14. `08_2adic_absolute_galois_group.md` — **3.7**

## About "unprovable"

A loop can search for proofs/disproofs and detect practical limitations, but **cannot generally decide unprovability** for arbitrary statements. Any "unprovable" conclusion should be treated as a meta-mathematical theorem requiring a separate formal framework.
