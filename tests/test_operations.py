"""Unit tests for calculator operations."""

from __future__ import annotations

import unittest

import operations


class TestOperations(unittest.TestCase):
    """Test suite for operations module."""

    def test_add(self) -> None:
        self.assertEqual(operations.add(2, 3), 5)

    def test_subtract(self) -> None:
        self.assertEqual(operations.subtract(10, 4), 6)

    def test_multiply(self) -> None:
        self.assertEqual(operations.multiply(2.5, 4), 10)

    def test_divide(self) -> None:
        self.assertEqual(operations.divide(10, 2), 5)

    def test_divide_by_zero_raises(self) -> None:
        with self.assertRaises(ValueError):
            operations.divide(5, 0)

    def test_power(self) -> None:
        self.assertEqual(operations.power(2, 3), 8)

    def test_square_root(self) -> None:
        self.assertEqual(operations.square_root(25), 5)

    def test_square_root_negative_raises(self) -> None:
        with self.assertRaises(ValueError):
            operations.square_root(-1)

    def test_percent(self) -> None:
        self.assertEqual(operations.percent(50), 0.5)

    def test_multiply_by_percent(self) -> None:
        self.assertEqual(operations.multiply_by_percent(200, 10), 20)

    def test_trig_in_degrees(self) -> None:
        self.assertAlmostEqual(operations.sin_degrees(30), 0.5, places=7)
        self.assertAlmostEqual(operations.cos_degrees(60), 0.5, places=7)

    def test_tan_undefined_raises(self) -> None:
        with self.assertRaises(ValueError):
            operations.tan_degrees(90)

    def test_circle_values_use_exact_pi_constant(self) -> None:
        self.assertEqual(operations.PI, 3.14)
        self.assertEqual(operations.circle_area(2), 12.56)
        self.assertEqual(operations.circle_circumference(2), 12.56)


if __name__ == "__main__":
    unittest.main()
