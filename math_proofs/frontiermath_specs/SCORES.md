# FrontierMath 14-problem scoring for iterative proof/search loops

Scoring target: likelihood that continuous technique iteration (search + verifier + stronger methods) yields a definitive outcome (true/false witness, or clear formal limitation path).

## Ranking (highest to lower)

| Rank | Problem | Score (/10) | Why this score |
|---:|---|---:|---|
| 1 | Large Steiner Systems | 9.5 | Exact finite combinatorial constraints; certificates are machine-checkable. |
| 2 | Stretched LR Coefficients | 9.0 | Witness search + exact symbolic verifier. |
| 3 | Ramsey Numbers for Book Graphs | 8.5 | SAT/SMT-compatible with strong finite certificates. |
| 4 | A Ramsey-style Problem on Hypergraphs | 8.0 | Construction + forbidden-property checking works well in code. |
| 5 | Unknotting Number = 1 | 8.0 | Decision algorithm testbed rich; proof of correctness is the main barrier. |
| 6 | Prime Factorization (GNFS constant) | 7.5 | Highly programmable optimization loop; asymptotic guarantees are harder. |
| 7 | Degree vs Sensitivity for Boolean Functions | 7.0 | Excellent finite experiments, asymptotic exponent remains difficult. |
| 8 | Arithmetic Kakeya Conjecture | 6.5 | Computation gives evidence and constructions, but not full resolution. |
| 9 | Inverse Galois (M23) | 6.0 | Candidate verification strong; search/discovery is hard. |
| 10 | Symplectic Ball Packing | 5.5 | Numerical and symbolic checks help, but geometry proof depth is high. |
| 11 | Surface with a High Number of Singularities | 5.0 | Candidate models testable; theoretical certification burden remains. |
| 12 | Explicit Deformations of Algebras | 4.5 | CAS supports examples, but full structural proof is difficult. |
| 13 | Apéry-style Irrationality Proofs | 4.0 | Discovery is computable; complete irrationality proofs are delicate. |
| 14 | The 2-adic Absolute Galois Group | 3.0 | Computational sanity checks possible, full result mostly theory-driven. |

## Interpreting "unprovable by limitation"

Programming can help detect likely limitations by:
1. finding many failed search trajectories,
2. exposing verifier bottlenecks,
3. identifying where only non-computational lemmas remain.

But proving true unprovability generally requires meta-mathematical results, not just computation.
