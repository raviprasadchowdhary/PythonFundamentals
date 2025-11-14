"""
A concise guide to Python's 'finally' clause in error handling.

This script covers:
- The purpose and usage of 'finally'
- Common operations and edge cases
- Best practices
- Key takeaways

Run this script to see outputs and learn how 'finally' works.
"""

# ---------------------------------------------------------------------
# What is 'finally'?
# ---------------------------------------------------------------------
# The 'finally' block in Python is used in try-except statements.
# Code inside 'finally' always runs, regardless of whether an exception occurred.

print("Section: Basic 'finally' usage")

try:
    print("Trying to divide by zero...")
    result = 10 / 0
except ZeroDivisionError:
    print("Caught ZeroDivisionError!")
finally:
    print("This always runs (finally block).")

print()  # Blank line for readability

# ---------------------------------------------------------------------
# 'finally' without 'except'
# ---------------------------------------------------------------------
# You can use 'finally' with just a 'try' block.
# Useful for cleanup actions (e.g., closing files).

print("Section: 'finally' without 'except'")

try:
    print("Trying to open a file...")
    f = open("nonexistent.txt")
finally:
    print("Cleaning up (finally block).")

print()  # Blank line for readability

# ---------------------------------------------------------------------
# 'finally' with return statements
# ---------------------------------------------------------------------
# If a 'try' or 'except' block contains a return statement,
# the 'finally' block still executes before returning.

print("Section: 'finally' with return statements")


def demo_return():
    try:
        print("In try block.")
        return "Returned from try"
    finally:
        print("Finally block runs before return.")


output = demo_return()
print(f"Function output: {output}")

print()  # Blank line for readability

# ---------------------------------------------------------------------
# Edge Case: Exception in 'finally'
# ---------------------------------------------------------------------
# If an exception occurs in 'finally', it can override previous exceptions.

print("Section: Exception in 'finally'")

try:
    print("Trying risky operation...")
    1 / 0
except ZeroDivisionError:
    print("Caught ZeroDivisionError!")
finally:
    print("Raising exception in finally...")
    raise ValueError("Exception from finally block")

# The script will stop here due to the unhandled ValueError.
# To continue, comment out the above 'finally' block or handle the exception.

print()  # Blank line for readability

# ---------------------------------------------------------------------
# Best Practices
# ---------------------------------------------------------------------
# Use 'finally' for cleanup actions (closing files, releasing resources).
# Avoid raising new exceptions in 'finally' unless necessary.
# Keep 'finally' blocks short and simple.

print("Section: Best Practices")

try:
    print("Opening file safely...")
    f = open(__file__, "r")
    data = f.read(10)
    print(f"Read data: {data}")
except Exception as e:
    print(f"Error: {e}")
finally:
    try:
        f.close()
        print("File closed in finally.")
    except Exception as e:
        print(f"Error closing file: {e}")

print()  # Blank line for readability

# ---------------------------------------------------------------------
# Summary & Key Takeaways
# ---------------------------------------------------------------------

print("Summary:")
print("- 'finally' always runs, even if exceptions occur or returns are used.")
print("- Use 'finally' for cleanup actions.")
print("- Exceptions in 'finally' can override previous exceptions.")
print("- Keep 'finally' blocks simple and focused on cleanup.")

# Variable type mapping (for reference)
print("\nVariable types:")
print(f"result: {type(0)}")
print(f"output: {type(output)}")
print(f"f: {type(f)}")
