# FrontierMath open problems: programmability + proof-testing assessment

Source: Epoch AI `FrontierMath: Open Problems` page (14 listed problems, captured 2026-02-18 via Playwright text extraction).

## Quick answer

All 14 can be **described** in programming language, but only a subset can be **fully proof-tested by computation alone**.

- **Best fit for programming + computational verification loops** (search / construction / witness-checking):
  - Ramsey Numbers for Book Graphs
  - A Ramsey-style Problem on Hypergraphs
  - The Arithmetic Kakeya Conjecture
  - Degree vs Sensitivity for Boolean Functions
  - Large Steiner Systems
  - Stretched Littlewood-Richardson Coefficients
  - Symplectic Ball Packing (numerical/computational side only)
  - Prime Factorization (algorithm-benchmark side)
  - Unknotting Number = 1 (algorithmic decision side)

- **Can be programmed, but "proof by testing" is weak unless paired with formal proof**:
  - Explicit Deformations of Algebras
  - Surface with a High Number of Singularities
  - The 2-adic Absolute Galois Group
  - Inverse Galois
  - Apéry-style Irrationality Proofs

## Per-problem assessment

Legend:
- **Specifiable** = can encode statement/objects in software.
- **Computational verifier** = can automatically check candidate outputs/witnesses.
- **Computation-only proof?** = can testing alone settle the math claim in general.

| Problem | Specifiable | Computational verifier | Computation-only proof? | Notes |
|---|---|---|---|---|
| Ramsey Numbers for Book Graphs | Yes | Yes (graph witness/counterexample checker) | Usually no (general tight bound) | Good for SAT/SMT + exhaustive small-n search. |
| A Ramsey-style Problem on Hypergraphs | Yes | Yes | Usually no | Great for constructive search pipelines. |
| Arithmetic Kakeya Conjecture | Yes | Partial | No | Can test constructions and bounds numerically. |
| Degree vs Sensitivity for Boolean Functions | Yes | Yes for finite n | No (asymptotic improvement) | Exhaustive search for small n useful. |
| Explicit Deformations of Algebras | Yes | Partial | No | Symbolic algebra software can verify examples. |
| Surface with High # Singularities | Yes | Partial | No | CAS can validate candidate surfaces locally. |
| Large Steiner Systems | Yes | Yes | Sometimes for concrete n,q,r instances | Construction + verifier is very programmable. |
| 2-adic Absolute Galois Group | Yes | Partial | No | Needs deep formal/algebraic argument beyond tests. |
| Inverse Galois (M23 polynomial) | Yes | Yes for candidate polynomial checks | No (search may fail inconclusively) | Verifying a found polynomial is programmable. |
| Stretched LR Coefficients | Yes | Yes | Often yes for concrete witness | Search for explicit negative coefficient witnesses is good fit. |
| Symplectic Ball Packing | Yes | Partial (numeric/symbolic checks) | No | Geometry proof likely needs theory beyond numerics. |
| Apéry-style Irrationality Proofs | Yes | Partial | No | Heuristic discovery programmable, proof needs rigor. |
| Prime Factorization (GNFS constant) | Yes | Yes (benchmarking/runtime model) | No (for asymptotic constant claim) | Strong engineering loop possible. |
| Unknotting Number = 1 | Yes | Yes for proposed algorithm output | No (correctness proof required) | Algorithm can be tested extensively, then proven. |

## Recommended targets (if your goal is "program + test proof")

If you want immediate progress with strong automated checking, start with:

1. **Large Steiner Systems** (construction + exact verifier).
2. **Stretched LR Coefficients** (witness search + exact symbolic check).
3. **Ramsey/Hypergraph problems** (SAT/ILP search with certificate verifiers).
4. **Unknotting Number = 1** (algorithm prototypes + property-based tests).

## A practical loop template for unknown math problems

Use this structure in `PROMPT.md`:

1. **Formal claim**: quantifiers + domains + assumptions.
2. **Object encoding**: exact data structures.
3. **Certificate format**: what counts as a witness/counterexample.
4. **Verifier**: deterministic function `verify(claim, certificate) -> bool`.
5. **Search**: SAT/SMT/ILP/heuristic generator for certificates.
6. **Backpressure**:
   - unit tests for verifier,
   - randomized adversarial tests,
   - known edge-case corpus,
   - formal proof task (Lean/Coq) for theorem-level statements.

This gives you "Ralph loop" productivity without confusing empirical success for proof.


## Program-language specs (14 files)

The 14 problem statements are now encoded one-per-file in `math_proofs/frontiermath_program_specs/`.

### Score ranking (highest loop-proofability first)

1. Large Steiner Systems — **90**
2. Stretched Littlewood-Richardson Coefficients — **88**
3. A Ramsey-style Problem on Hypergraphs — **82**
4. Ramsey Numbers for Book Graphs — **78**
5. Unknotting Number = 1 — **74**
6. Degree vs Sensitivity for Boolean Functions — **73**
7. Inverse Galois (M23) — **67**
8. Surface with a High Number of Singularities — **62**
9. Prime Factorization (GNFS constant) — **61**
10. Arithmetic Kakeya Conjecture — **55**
11. Symplectic Ball Packing — **46**
12. Explicit Deformations of Algebras — **40**
13. Apéry-style Irrationality Proofs — **33**
14. The 2-adic Absolute Galois Group — **25**

Interpretation: high score means a coding loop can generate/check certificates quickly; low score means formal abstraction dominates and requires deep theorem proving beyond iterative computational checks.
