"""
if, elif, else in Python: A Concise Educational Guide

This script demonstrates Python's conditional statements: if, elif, and else.
It covers their syntax, usage, common operations, edge cases, and best practices.
Run this script to see outputs and learn how control flow works in Python.
"""

# ---------------------------------------------------------------------
# Section 1: Basic 'if' Statement
# The 'if' statement executes code only if its condition is True.

x = 10
print("Section 1: Basic 'if' Statement")
if x > 5:
    print(f"x ({x}) is greater than 5")  # Output: x (10) is greater than 5

print()  # Blank line for readability

# ---------------------------------------------------------------------
# Section 2: 'if-else' Statement
# Use 'else' to provide an alternative block if the 'if' condition is False.

y = 3
print("Section 2: 'if-else' Statement")
if y > 5:
    print(f"y ({y}) is greater than 5")
else:
    # Output: y (3) is not greater than 5
    print(f"y ({y}) is not greater than 5")

print()

# ---------------------------------------------------------------------
# Section 3: 'if-elif-else' Chain
# 'elif' allows checking multiple conditions in sequence.

z = 5
print("Section 3: 'if-elif-else' Chain")
if z > 5:
    print("z is greater than 5")
elif z == 5:
    print("z is exactly 5")  # Output: z is exactly 5
else:
    print("z is less than 5")

print()

# ---------------------------------------------------------------------
# Section 4: Nested Conditionals
# You can nest 'if' statements for more complex logic.

age = 20
has_id = True
print("Section 4: Nested Conditionals")
if age >= 18:
    if has_id:
        print("Access granted")  # Output: Access granted
    else:
        print("ID required")
else:
    print("Access denied")

print()

# ---------------------------------------------------------------------
# Section 5: Common Operations and Edge Cases
# Demonstrates truthy/falsy values, empty containers, and best practices.

print("Section 5: Common Operations and Edge Cases")

# Truthy and falsy values
value = ""
if value:
    print("Value is truthy")
else:
    # Output: Value is falsy (empty string)
    print("Value is falsy (empty string)")

# Checking for None
data = None
if data is None:
    print("data is None")  # Output: data is None

# Avoiding assignment in condition (best practice)
flag = True
if flag == True:  # Explicit comparison is clearer
    print("Flag is True")  # Output: Flag is True

# Using 'elif' to avoid unnecessary checks
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")  # Output: Grade: B
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: D or below")

print()

# ---------------------------------------------------------------------
# Section 6: Summary and Key Takeaways

print("Section 6: Summary and Key Takeaways")
# Variable types mapping
variables = {
    "x": type(x).__name__,
    "y": type(y).__name__,
    "z": type(z).__name__,
    "age": type(age).__name__,
    "has_id": type(has_id).__name__,
    "value": type(value).__name__,
    "data": type(data).__name__,
    "flag": type(flag).__name__,
    "score": type(score).__name__,
}
print("Variable types:", variables)

# Key takeaways
print("""
Key Takeaways:
- Use 'if' for single condition checks.
- Use 'elif' for multiple, mutually exclusive conditions.
- Use 'else' for a default/fallback block.
- Pay attention to truthy/falsy values.
- Use explicit comparisons for clarity.
- Nest conditionals for complex logic, but keep nesting minimal for readability.
""")
