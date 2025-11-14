import math
import datetime
import os

"""
Standard Libraries Educational Guide

This script introduces Python's standard libraries, focusing on math, datetime, and os.
It demonstrates common operations, edge cases, and best practices, with outputs for clarity.
"""

# ---------------------------------------------------------------------
# Math Library: Mathematical Operations
# ---------------------------------------------------------------------
# The math module provides mathematical functions like sqrt, pow, factorial, and constants.


print("Math Library Examples:")

# Basic operations
print("Square root of 16:", math.sqrt(16))
print("2 raised to the power 3:", math.pow(2, 3))
print("Factorial of 5:", math.factorial(5))
print("Value of pi:", math.pi)

# Edge case: sqrt of negative number raises ValueError
try:
    print("Square root of -1:", math.sqrt(-1))
except ValueError as e:
    print("Error (sqrt of -1):", e)

# Best practice: Use math.isclose for floating-point comparisons
a = 0.1 + 0.2
b = 0.3
print("Is 0.1 + 0.2 close to 0.3?", math.isclose(a, b))

print()  # Blank line for readability

# ---------------------------------------------------------------------
# Datetime Library: Date and Time Manipulation
# ---------------------------------------------------------------------
# The datetime module helps work with dates, times, and timedeltas.


print("Datetime Library Examples:")

# Current date and time
now = datetime.datetime.now()
print("Current date and time:", now)

# Creating specific dates
birthday = datetime.date(1990, 5, 17)
print("Birthday:", birthday)

# Time difference (timedelta)
delta = datetime.timedelta(days=7)
future_date = now + delta
print("Date 7 days from now:", future_date)

# Edge case: Invalid date raises ValueError
try:
    invalid_date = datetime.date(2024, 2, 30)
except ValueError as e:
    print("Error (invalid date):", e)

# Best practice: Use isoformat for standardized date strings
print("Current date in ISO format:", now.date().isoformat())

print()  # Blank line for readability

# ---------------------------------------------------------------------
# OS Library: Operating System Interactions
# ---------------------------------------------------------------------
# The os module allows interaction with the operating system, such as file and directory management.


print("OS Library Examples:")

# Get current working directory
cwd = os.getcwd()
print("Current working directory:", cwd)

# List files in current directory
print("Files in current directory:", os.listdir(cwd))

# Edge case: Listing files in a non-existent directory
try:
    print("Files in non-existent directory:", os.listdir("non_existent_dir"))
except FileNotFoundError as e:
    print("Error (listing non-existent directory):", e)

# Best practice: Use os.path for path manipulations
file_path = os.path.join(cwd, "example.txt")
print("Joined file path:", file_path)
print("Does 'example.txt' exist?", os.path.exists(file_path))

print()  # Blank line for readability

# ---------------------------------------------------------------------
# Summary Section
# ---------------------------------------------------------------------
# Mapping variable names to their types and listing key takeaways.

print("Summary:")
variables = {
    "now": type(now),
    "birthday": type(birthday),
    "delta": type(delta),
    "cwd": type(cwd),
    "file_path": type(file_path),
}
for name, typ in variables.items():
    print(f"{name}: {typ}")

print("\nKey Takeaways:")
print("- Use standard libraries for reliable, efficient solutions.")
print("- Handle edge cases with try/except blocks.")
print("- Prefer best practices like math.isclose and os.path for accuracy and portability.")
