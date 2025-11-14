import math

"""
Python Guide: Defining and Calling Functions

This script introduces the basics of defining and calling functions in Python.
It covers function syntax, parameters, return values, default arguments, variable scope,
edge cases, and best practices. Example outputs are shown using print statements.
"""

# ---------------------------------------------------------------------
# 1. Defining a Simple Function
# Functions are defined using the 'def' keyword, followed by the function name and parentheses.


def greet():
    """Prints a greeting message."""
    print("Hello, welcome to Python functions!")


greet()  # Calling the function

print()  # Blank line for readability

# ---------------------------------------------------------------------
# 2. Function with Parameters
# Functions can accept parameters to work with dynamic data.


def add(a, b):
    """Returns the sum of two numbers."""
    return a + b


result = add(3, 5)
print("Sum of 3 and 5:", result)

print()

# ---------------------------------------------------------------------
# 3. Function with Default Arguments
# Default values can be provided for parameters.


def power(base, exponent=2):
    """Returns base raised to the power of exponent (default is 2)."""
    return base ** exponent


print("2 squared:", power(2))
print("2 cubed:", power(2, 3))

print()

# ---------------------------------------------------------------------
# 4. Function with Multiple Return Values
# Functions can return multiple values as a tuple.


def min_max(numbers):
    """Returns the minimum and maximum of a list."""
    return min(numbers), max(numbers)


nums = [4, 7, 1, 9]
minimum, maximum = min_max(nums)
print("Numbers:", nums)
print("Minimum:", minimum)
print("Maximum:", maximum)

print()

# ---------------------------------------------------------------------
# 5. Edge Case: No Return Statement
# If a function does not explicitly return a value, it returns None.


def do_nothing():
    pass


print("do_nothing() returns:", do_nothing())

print()

# ---------------------------------------------------------------------
# 6. Variable Scope
# Variables defined inside a function are local to that function.


def show_scope():
    local_var = "I'm local"
    print(local_var)


show_scope()
# print(local_var)  # Uncommenting this line would cause an error (NameError)

print()

# ---------------------------------------------------------------------
# 7. Best Practices
# - Use descriptive function and parameter names.
# - Add docstrings to explain function purpose.
# - Keep functions focused on a single task.


def calculate_area(radius):
    """Calculates the area of a circle given its radius."""
    return math.pi * radius ** 2


print("Area of circle with radius 3:", calculate_area(3))

print()

# ---------------------------------------------------------------------
# 8. Summary: Variable Names and Types

summary = {
    "greet": "function",
    "add": "function",
    "result": type(result).__name__,
    "power": "function",
    "min_max": "function",
    "nums": type(nums).__name__,
    "minimum": type(minimum).__name__,
    "maximum": type(maximum).__name__,
    "do_nothing": "function",
    "show_scope": "function",
    "calculate_area": "function",
}

print("Summary of variable names and their types:")
for name, typ in summary.items():
    print(f"{name}: {typ}")

print("\nKey Takeaways:")
print("- Define functions with 'def' and call them by name.")
print("- Use parameters and return values for flexibility.")
print("- Default arguments and multiple returns add power.")
print("- Scope keeps variables organized and safe.")
print("- Docstrings and clear names improve readability.")
