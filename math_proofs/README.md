# Fermat's Little Theorem in code + proof-testing workflow

This folder gives you a practical bridge from natural-language math to executable checks.

## 1) Describe the theorem in a machine-checkable way

Natural language:

> If `p` is prime and `gcd(a, p) = 1`, then `a^(p-1) ≡ 1 (mod p)`.

Programming form (predicate):

```python
is_prime(p) and gcd(a, p) == 1  =>  pow(a, p - 1, p) == 1
```

This is exactly what `fermat_little_theorem_holds` checks.

## 2) Separate "verification by testing" from "formal proof"

- **Testing/computation**: finite checks for many values and search for counterexamples.
- **Formal proof**: proof assistants (Lean/Coq/Isabelle) where every step is type-checked.

Use testing as backpressure in loops. Use proof assistants for final theorem-level certainty.

## 3) Use this in a Ralph/Codex loop

A simple loop idea inspired by the Ralph method:

```bash
while :; do
  codex <<'PROMPT'
Goal: Improve math_proofs/ until all tests pass and docs are clearer.
Constraints:
- Keep theorem statement precise.
- Distinguish probabilistic/computational checks from formal proof.
- Add examples for Carmichael numbers.
Then run:
- python -m unittest math_proofs/test_fermat_little_theorem.py
PROMPT

done
```

## 4) How to test whether your "proof" is really a proof

### A. Computational checks (quick and useful)

1. Validate the theorem for many primes.
2. Search counterexamples for composite numbers.
3. Include adversarial cases (e.g., Carmichael numbers like `561`) so you don't overclaim.

### B. Formal checks (for actual proof confidence)

If you want theorem-level certainty:

1. Encode theorem in Lean/Coq.
2. Require all proof steps to compile.
3. Keep this repository script as sanity tests, but treat the prover artifact as the source of truth.

## 5) Suggested prompt format for unknown conjectures

When you try a new conjecture, use this structure:

1. **Domain**: exact input set and variable constraints.
2. **Claim**: logical form (`forall`, `exists`, implications).
3. **Executable predicate**: boolean function for finite checks.
4. **Disproof strategy**: search space + witness printer.
5. **Proof strategy**: mapping to known lemmas/theorems.
6. **Backpressure gates**: tests, edge cases, proof compile step.

That keeps Codex loops productive and reduces hallucinated "proofs".


## 6) FrontierMath open problems triage

See `math_proofs/frontiermath_open_problems_assessment.md` for a per-problem analysis of which open problems are most suitable for programming-language encoding and computational verification loops.

## 7) Full 14-problem programming specs

See `math_proofs/frontiermath_specs/` for 14 per-problem programming-language formalizations and `math_proofs/frontiermath_specs/SCORES.md` for a ranked likelihood score.
