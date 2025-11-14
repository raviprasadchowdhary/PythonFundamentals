"""
except.py

A concise, educational guide to Python's 'except' statement in error handling.
Covers basic usage, multiple exceptions, catching all exceptions, accessing exception objects,
edge cases, and best practices.
"""

# ---------------------------------------------------------------------
# Basic Usage of 'except'
# The 'except' block handles exceptions raised in the 'try' block.

print("Basic Usage:")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Caught a ZeroDivisionError: division by zero.")

print()


# ---------------------------------------------------------------------
# Catching Multiple Exception Types
# You can handle different exceptions with multiple 'except' blocks.

print("Catching Multiple Exception Types:")
try:
    value = int("abc")  # Raises ValueError
    result = 10 / value
except ValueError:
    print("Caught a ValueError: invalid literal for int().")
except ZeroDivisionError:
    print("Caught a ZeroDivisionError: division by zero.")

print()


# ---------------------------------------------------------------------
# Catching Multiple Exceptions in One Block
# Use a tuple to catch several exceptions with the same handler.

print("Catching Multiple Exceptions in One Block:")
try:
    value = int("abc")
    result = 10 / value
except (ValueError, ZeroDivisionError) as e:
    print(f"Caught an exception: {type(e).__name__} - {e}")

print()


# ---------------------------------------------------------------------
# Catching All Exceptions (Not Recommended)
# Catching all exceptions can hide bugs; use with caution.

print("Catching All Exceptions:")
try:
    x = undefined_variable  # NameError
except Exception as e:
    print(f"Caught an exception: {type(e).__name__} - {e}")

print()


# ---------------------------------------------------------------------
# Accessing Exception Objects
# Use 'as' to access the exception object for details.

print("Accessing Exception Objects:")
try:
    lst = [1, 2, 3]
    print(lst[5])  # IndexError
except IndexError as error:
    print(f"Caught IndexError: {error}")

print()


# ---------------------------------------------------------------------
# Edge Case: No Exception Raised
# If no exception occurs, the 'except' block is skipped.

print("No Exception Raised:")
try:
    print("No error here!")
except Exception:
    print("This will not be printed.")

print()


# ---------------------------------------------------------------------
# Best Practice: Specific Exceptions First
# Always catch specific exceptions before general ones.

print("Best Practice: Specific Exceptions First:")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Handle division by zero specifically.")
except Exception:
    print("Handle any other exception.")

print()


# ---------------------------------------------------------------------
# Summary: Key Takeaways

print("Summary:")
print("- Use 'except' to handle errors and prevent crashes.")
print("- Catch specific exceptions for clarity and safety.")
print("- Access exception details with 'as'.")
print("- Avoid catching all exceptions unless necessary.")
print("- Multiple 'except' blocks can handle different errors.")
print("- The 'except' block runs only if an exception occurs in 'try'.")
