"""Core calculator operations for the Flask calculator app."""

from __future__ import annotations

import math

PI = 3.14


def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the difference between two numbers."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of two numbers."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return the quotient of two numbers.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def power(base: float, exponent: float) -> float:
    """Return base raised to the given exponent."""
    return base**exponent


def square_root(value: float) -> float:
    """Return the square root of a value.

    Raises:
        ValueError: If value is negative.
    """
    if value < 0:
        raise ValueError("Cannot take square root of a negative number.")
    return math.sqrt(value)


def percent(value: float) -> float:
    """Convert a number to its percentage decimal form."""
    return value / 100


def multiply_by_percent(base: float, percentage_value: float) -> float:
    """Return base multiplied by percentage_value as a percent (base * y%)."""
    return base * percent(percentage_value)


def sin_degrees(angle_degrees: float) -> float:
    """Return sine of an angle in degrees."""
    return math.sin(math.radians(angle_degrees))


def cos_degrees(angle_degrees: float) -> float:
    """Return cosine of an angle in degrees."""
    return math.cos(math.radians(angle_degrees))


def tan_degrees(angle_degrees: float) -> float:
    """Return tangent of an angle in degrees.

    Raises:
        ValueError: If tangent is undefined (cosine approximately zero).
    """
    cosine_value = cos_degrees(angle_degrees)
    if abs(cosine_value) < 1e-12:
        raise ValueError("Tangent is undefined for this angle (cosine is approximately zero).")
    return math.tan(math.radians(angle_degrees))


def circle_circumference(radius: float) -> float:
    """Return circumference of a circle with the given radius using PI = 3.14."""
    return 2 * PI * radius


def circle_area(radius: float) -> float:
    """Return area of a circle with the given radius using PI = 3.14."""
    return PI * (radius**2)
