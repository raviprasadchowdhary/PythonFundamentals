"""
Python Operators Guide

This script provides a concise overview of Python's operators, including:
- Arithmetic
- Comparison
- Logical
- Assignment
- Bitwise
- Membership
- Identity

Each section includes explanations, examples, edge cases, and best practices.
Run this script to see outputs and learn how operators work in Python.
"""

# ---------------------------------------------------------------------
# Arithmetic Operators
# Used for mathematical operations: +, -, *, /, //, %, **
# Edge cases: division by zero, integer vs float division

print("Arithmetic Operators:")
a = 10
b = 3

print("a + b =", a + b)      # Addition
print("a - b =", a - b)      # Subtraction
print("a * b =", a * b)      # Multiplication
print("a / b =", a / b)      # Division (float result)
print("a // b =", a // b)    # Floor division (integer result)
print("a % b =", a % b)      # Modulus (remainder)
print("a ** b =", a ** b)    # Exponentiation

# Edge case: division by zero
try:
    print("a / 0 =", a / 0)
except ZeroDivisionError:
    print("a / 0 = Error (division by zero)")

print()

# ---------------------------------------------------------------------
# Comparison Operators
# Used to compare values: ==, !=, >, <, >=, <=

print("Comparison Operators:")
x = 5
y = 7

print("x == y:", x == y)     # Equal to
print("x != y:", x != y)     # Not equal to
print("x > y:", x > y)       # Greater than
print("x < y:", x < y)       # Less than
print("x >= y:", x >= y)     # Greater than or equal to
print("x <= y:", x <= y)     # Less than or equal to

print()

# ---------------------------------------------------------------------
# Logical Operators
# Used to combine conditional statements: and, or, not

print("Logical Operators:")
p = True
q = False

print("p and q:", p and q)   # Logical AND
print("p or q:", p or q)     # Logical OR
print("not p:", not p)       # Logical NOT

# Best practice: Use parentheses for clarity in complex expressions
print("not (p and q):", not (p and q))

print()

# ---------------------------------------------------------------------
# Assignment Operators
# Used to assign values and perform operations: =, +=, -=, *=, /=, //=, %=, **=

print("Assignment Operators:")
n = 5
print("Initial n:", n)
n += 2
print("n after n += 2:", n)
n *= 3
print("n after n *= 3:", n)
n //= 4
print("n after n //= 4:", n)
n **= 2
print("n after n **= 2:", n)

print()

# ---------------------------------------------------------------------
# Bitwise Operators
# Operate on binary representations: &, |, ^, ~, <<, >>

print("Bitwise Operators:")
m = 6      # 0b110
k = 3      # 0b011

print("m & k:", m & k)       # AND
print("m | k:", m | k)       # OR
print("m ^ k:", m ^ k)       # XOR
print("~m:", ~m)             # NOT
print("m << 1:", m << 1)     # Left shift
print("m >> 1:", m >> 1)     # Right shift

print()

# ---------------------------------------------------------------------
# Membership Operators
# Test for membership in a sequence: in, not in

print("Membership Operators:")
lst = [1, 2, 3, 4]
print("2 in lst:", 2 in lst)
print("5 not in lst:", 5 not in lst)

print()

# ---------------------------------------------------------------------
# Identity Operators
# Test if two variables refer to the same object: is, is not

print("Identity Operators:")
a1 = [1, 2]
a2 = [1, 2]
a3 = a1

print("a1 is a2:", a1 is a2)         # False (different objects)
print("a1 is a3:", a1 is a3)         # True (same object)
print("a1 == a2:", a1 == a2)         # True (same contents)

print()

# ---------------------------------------------------------------------
# Summary Section
# Mapping variable names to their types and listing key takeaways

print("Summary:")
variables = {
    'a': type(a),
    'b': type(b),
    'x': type(x),
    'p': type(p),
    'lst': type(lst),
    'a1': type(a1),
}
for name, t in variables.items():
    print(f"{name}: {t}")

print("\nKey Takeaways:")
print("- Operators are fundamental for manipulating data in Python.")
print("- Always handle edge cases (e.g., division by zero).")
print("- Use parentheses for clarity in complex logical expressions.")
print("- 'is' checks identity, '==' checks equality.")
print("- Membership and identity operators are useful for collections and object references.")
