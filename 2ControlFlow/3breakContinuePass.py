"""
Breaking, Continuing, and Passing in Loops - Educational Guide

This script demonstrates how to use `break`, `continue`, and `pass` statements in Python loops.
It covers their purposes, usage, common operations, edge cases, and best practices.
"""

# ---------------------------------------------------------------------
# BREAK STATEMENT
# ---------------------------------------------------------------------
# The `break` statement immediately exits the enclosing loop.
# Commonly used to stop processing when a condition is met.

print("Break Example: Stop at first even number")
for num in range(1, 6):
    print(f"Checking {num}")
    if num % 2 == 0:
        print(f"First even number found: {num}")
        break
print("Loop ended with break.\n")

# Edge Case: Break in nested loops only exits the innermost loop.
print("Break Example: Nested loops")
for i in range(2):
    for j in range(3):
        if j == 1:
            print(f"Breaking inner loop at i={i}, j={j}")
            break
        print(f"i={i}, j={j}")
print("Nested loop ended.\n")

# Best Practice: Use break to avoid unnecessary iterations.


# ---------------------------------------------------------------------
# CONTINUE STATEMENT
# ---------------------------------------------------------------------
# The `continue` statement skips the rest of the current loop iteration.
# Useful for skipping unwanted values.

print("Continue Example: Print only odd numbers")
for num in range(1, 6):
    if num % 2 == 0:
        continue  # Skip even numbers
    print(f"Odd number: {num}")
print("Loop ended with continue.\n")

# Edge Case: Continue at the end of the loop has no effect.
print("Continue Example: Continue at end")
for num in range(3):
    print(f"Number before continue: {num}")
    continue
    print("This line will never execute.")
print("Loop ended.\n")

# Best Practice: Use continue to keep code readable by avoiding deeply nested ifs.


# ---------------------------------------------------------------------
# PASS STATEMENT
# ---------------------------------------------------------------------
# The `pass` statement does nothing; it's a placeholder.
# Useful for stubbing out code or empty loop bodies.

print("Pass Example: Placeholder in loop")
for num in range(3):
    if num == 1:
        pass  # Placeholder for future code
    print(f"Number: {num}")
print("Loop ended with pass.\n")

# Edge Case: Pass does not affect loop flow.
# Best Practice: Use pass for code that will be implemented later.


# ---------------------------------------------------------------------
# SUMMARY & KEY TAKEAWAYS
# ---------------------------------------------------------------------
# - break: Exits the loop immediately.
# - continue: Skips to the next iteration.
# - pass: Does nothing; useful as a placeholder.
# - Use break/continue for readable, efficient loops.
# - Use pass for code stubs or empty blocks.

print("Summary:")
keywords = {
    "break": "Exits loop",
    "continue": "Skips iteration",
    "pass": "No operation"
}
for k, v in keywords.items():
    print(f"{k}: {v}")
