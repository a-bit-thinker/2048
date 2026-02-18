"""Utilities to model and test Fermat's Little Theorem.

Fermat's Little Theorem (FLT):
If p is prime and gcd(a, p) = 1, then a^(p-1) ≡ 1 (mod p).
Equivalent form for prime p: a^p ≡ a (mod p) for all integers a.
"""

from __future__ import annotations

from math import gcd, isqrt


def is_prime(n: int) -> bool:
    """Return True if n is prime using deterministic trial division."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i <= isqrt(n):
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def fermat_little_theorem_holds(p: int, sample_limit: int | None = None) -> bool:
    """Check the FLT congruence a^(p-1) ≡ 1 (mod p) for all coprime a in range.

    If sample_limit is None, checks all a in [1, p-1].
    Otherwise, checks min(p-1, sample_limit) values.
    """
    if not is_prime(p):
        raise ValueError(f"p must be prime, got {p}")

    upper = p - 1 if sample_limit is None else min(p - 1, sample_limit)
    for a in range(1, upper + 1):
        if gcd(a, p) != 1:
            continue
        if pow(a, p - 1, p) != 1:
            return False
    return True


def find_composite_counterexample(n: int) -> tuple[int, int] | None:
    """Return (a, residue) showing failure of a^(n-1) ≡ 1 (mod n), else None.

    For a composite n, this often finds a witness quickly.
    Carmichael numbers are the notable case where no witness exists for coprime a.
    """
    if n <= 1 or is_prime(n):
        raise ValueError(f"n must be composite and > 1, got {n}")

    for a in range(2, n):
        if gcd(a, n) != 1:
            continue
        residue = pow(a, n - 1, n)
        if residue != 1:
            return a, residue
    return None


def explain_number(n: int) -> str:
    """Return a human-readable explanation of FLT behavior for n."""
    if is_prime(n):
        return (
            f"{n} is prime. FLT predicts a^({n}-1) ≡ 1 (mod {n}) for all a coprime to {n}. "
            f"Verified: {fermat_little_theorem_holds(n)}."
        )

    witness = find_composite_counterexample(n)
    if witness is None:
        return (
            f"{n} is composite, but no coprime witness was found. "
            "This suggests n may behave like a Carmichael number for the tested predicate."
        )

    a, residue = witness
    return (
        f"{n} is composite. Counterexample found: a={a}, "
        f"a^(n-1) mod n = {residue} (expected 1 if FLT-style condition held)."
    )


if __name__ == "__main__":
    # Minimal CLI-style demo examples:
    examples = [7, 15, 341, 561]
    for value in examples:
        print(explain_number(value))
