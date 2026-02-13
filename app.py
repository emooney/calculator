"""Flask web application for a calculator with standard, scientific, and circle operations."""

from __future__ import annotations

import logging
from typing import Any

from flask import Flask, render_template, request

import operations

app = Flask(__name__)
logger = logging.getLogger(__name__)


def parse_float(raw_value: str, field_name: str) -> float:
    """Parse a float from a string field and raise a user-friendly ValueError on failure."""
    try:
        return float(raw_value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"Please enter a valid number for '{field_name}'.") from exc


@app.route("/", methods=["GET", "POST"])
def index() -> str:
    """Render calculator interface and process form submissions."""
    result: str | None = None
    error: str | None = None
    active_section = "standard"

    form_data: dict[str, Any] = {
        "standard_a": "",
        "standard_b": "",
        "standard_operation": "add",
        "scientific_value": "",
        "scientific_operation": "sqrt",
        "circle_radius": "",
        "circle_operation": "area",
    }

    if request.method == "POST":
        active_section = request.form.get("section", "standard")
        form_data.update({key: request.form.get(key, "") for key in form_data})

        try:
            if active_section == "standard":
                result = handle_standard(form_data)
            elif active_section == "scientific":
                result = handle_scientific(form_data)
            elif active_section == "circle":
                result = handle_circle(form_data)
            else:
                error = "Unknown calculator section."
        except ValueError as exc:
            error = str(exc)
        except Exception:  # pylint: disable=broad-except
            logger.exception("Unexpected error while processing calculator input")
            error = "Something went wrong while processing your request. Please try again."

    return render_template(
        "index.html",
        result=result,
        error=error,
        active_section=active_section,
        form_data=form_data,
    )


def handle_standard(form_data: dict[str, Any]) -> str:
    """Handle standard calculator operations."""
    a = parse_float(form_data["standard_a"], "First number")
    b = parse_float(form_data["standard_b"], "Second number")
    operation = form_data["standard_operation"]

    if operation == "add":
        value = operations.add(a, b)
    elif operation == "subtract":
        value = operations.subtract(a, b)
    elif operation == "multiply":
        value = operations.multiply(a, b)
    elif operation == "divide":
        value = operations.divide(a, b)
    elif operation == "power":
        value = operations.power(a, b)
    elif operation == "percent_of":
        value = operations.multiply_by_percent(a, b)
    else:
        raise ValueError("Please select a valid standard operation.")

    return f"Result: {value}"


def handle_scientific(form_data: dict[str, Any]) -> str:
    """Handle scientific calculator operations."""
    value = parse_float(form_data["scientific_value"], "Scientific value")
    operation = form_data["scientific_operation"]

    if operation == "sqrt":
        computed = operations.square_root(value)
    elif operation == "sin":
        computed = operations.sin_degrees(value)
    elif operation == "cos":
        computed = operations.cos_degrees(value)
    elif operation == "tan":
        computed = operations.tan_degrees(value)
    elif operation == "percent":
        computed = operations.percent(value)
    else:
        raise ValueError("Please select a valid scientific operation.")

    return f"Result: {computed}"


def handle_circle(form_data: dict[str, Any]) -> str:
    """Handle circle area and circumference calculations."""
    radius = parse_float(form_data["circle_radius"], "Radius")
    if radius < 0:
        raise ValueError("Radius cannot be negative.")

    operation = form_data["circle_operation"]
    if operation == "area":
        value = operations.circle_area(radius)
    elif operation == "circumference":
        value = operations.circle_circumference(radius)
    else:
        raise ValueError("Please select a valid circle operation.")

    return f"Result: {value} (using PI = {operations.PI})"


if __name__ == "__main__":
    app.run(debug=True)
