import unittest

from math_proofs.fermat_little_theorem import (
    explain_number,
    fermat_little_theorem_holds,
    find_composite_counterexample,
    is_prime,
)


class FermatLittleTheoremTests(unittest.TestCase):
    def test_is_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(97))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(100))

    def test_fermat_holds_for_prime(self):
        self.assertTrue(fermat_little_theorem_holds(5))
        self.assertTrue(fermat_little_theorem_holds(13))

    def test_counterexample_for_composite(self):
        witness = find_composite_counterexample(15)
        self.assertIsNotNone(witness)

    def test_carmichael_behavior(self):
        # 561 is the smallest Carmichael number.
        witness = find_composite_counterexample(561)
        self.assertIsNone(witness)

    def test_explain_number_contains_context(self):
        prime_msg = explain_number(7)
        composite_msg = explain_number(15)
        self.assertIn("prime", prime_msg.lower())
        self.assertIn("composite", composite_msg.lower())


if __name__ == "__main__":
    unittest.main()
