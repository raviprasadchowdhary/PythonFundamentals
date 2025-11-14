"""
try Statement Educational Guide

This script introduces Python's `try` statement for error handling.
It covers basic usage, handling multiple exceptions, using `else` and `finally` clauses,
common operations, edge cases, and best practices. Outputs are printed for clarity.
"""

# ---------------------------------------------------------------------
# Basic try-except Usage
# ---------------------------------------------------------------------
# The try block lets you test code for errors.
# The except block lets you handle the error gracefully.

print("Basic try-except example:")

try:
    result = 10 / 2
    print("Result:", result)
except ZeroDivisionError:
    print("Cannot divide by zero.")

print()  # Blank line for readability

# ---------------------------------------------------------------------
# Handling Specific Exceptions
# ---------------------------------------------------------------------
# You can catch specific exceptions to handle different error types.

print("Handling specific exceptions:")

try:
    value = int("abc")  # This will raise a ValueError
except ValueError:
    print("ValueError: Could not convert string to integer.")

print()

# ---------------------------------------------------------------------
# Catching Multiple Exceptions
# ---------------------------------------------------------------------
# Use a tuple to catch multiple exception types.

print("Catching multiple exceptions:")

try:
    x = int("abc")
    y = 10 / 0
except (ValueError, ZeroDivisionError) as e:
    print("Caught exception:", type(e).__name__)

print()

# ---------------------------------------------------------------------
# Using else with try-except
# ---------------------------------------------------------------------
# The else block runs if no exceptions were raised.

print("Using else with try-except:")

try:
    num = int("123")
except ValueError:
    print("Conversion failed.")
else:
    print("Conversion succeeded:", num)

print()

# ---------------------------------------------------------------------
# Using finally with try-except
# ---------------------------------------------------------------------
# The finally block always runs, whether an exception occurred or not.

print("Using finally with try-except:")

try:
    print("Trying something risky...")
    risky = 1 / 1
except ZeroDivisionError:
    print("Oops, division by zero!")
finally:
    print("This always runs.")

print()

# ---------------------------------------------------------------------
# Edge Case: No Exception Raised
# ---------------------------------------------------------------------
# If no exception occurs, except block is skipped.

print("Edge case: No exception raised:")

try:
    print("No error here.")
except Exception:
    print("This won't be printed.")

print()

# ---------------------------------------------------------------------
# Best Practice: Catch Only Expected Exceptions
# ---------------------------------------------------------------------
# Avoid catching all exceptions unless necessary.

print("Best practice: Catch only expected exceptions:")

try:
    print("Attempting risky operation...")
    risky = 10 / 0
except ZeroDivisionError:
    print("Handled ZeroDivisionError.")
# Avoid: except: (bad practice, catches all exceptions)

print()

# ---------------------------------------------------------------------
# Summary: Variable Types and Key Takeaways
# ---------------------------------------------------------------------

print("Summary:")
print("result:", type(result))
print("value: Not assigned due to exception")
print("num:", type(num))
print("risky:", type(risky))
print()
print("Key takeaways:")
print("- Use try-except to handle errors gracefully.")
print("- Catch specific exceptions for clarity.")
print("- Use else for code that runs if no error occurs.")
print("- Use finally for cleanup actions.")
print("- Avoid catching all exceptions unless absolutely necessary.")
