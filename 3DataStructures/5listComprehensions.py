"""
List Comprehensions in Python: A Concise Educational Guide

This script introduces Python list comprehensions, covering:
- Basic syntax
- Filtering
- Nested comprehensions
- Common operations
- Edge cases
- Best practices
- Key takeaways

Run this script to see examples and outputs for each concept.
"""

# ---------------------------------------------------------------------
# 1. Basic List Comprehension
# Create a new list by applying an expression to each item in an iterable.

numbers = [1, 2, 3, 4, 5]
squares = [n ** 2 for n in numbers]
print("Basic: Squares of numbers:", squares)  # [1, 4, 9, 16, 25]


# ---------------------------------------------------------------------
# 2. List Comprehension with Filtering (if condition)
# Only include items that meet a condition.

even_squares = [n ** 2 for n in numbers if n % 2 == 0]
print("Filtering: Squares of even numbers:", even_squares)  # [4, 16]


# ---------------------------------------------------------------------
# 3. Nested List Comprehensions
# Flatten a 2D list (matrix) into a 1D list.

matrix = [[1, 2], [3, 4], [5, 6]]
flattened = [item for row in matrix for item in row]
print("Nested: Flattened matrix:", flattened)  # [1, 2, 3, 4, 5, 6]


# ---------------------------------------------------------------------
# 4. Applying Functions and Expressions
# Use functions or more complex expressions inside comprehensions.

def cube(x):
    return x ** 3


cubes = [cube(n) for n in numbers]
print("Functions: Cubes of numbers:", cubes)  # [1, 8, 27, 64, 125]


# ---------------------------------------------------------------------
# 5. Edge Cases
# Empty input, None values, and type conversion.

empty = []
empty_result = [x * 2 for x in empty]
print("Edge Case: Empty input:", empty_result)  # []

mixed = [1, None, 2, None, 3]
filtered = [x for x in mixed if x is not None]
print("Edge Case: Filter None values:", filtered)  # [1, 2, 3]

str_numbers = ['1', '2', 'three', '4']
int_numbers = [int(x) for x in str_numbers if x.isdigit()]
print("Edge Case: Convert strings to ints:", int_numbers)  # [1, 2, 4]


# ---------------------------------------------------------------------
# 6. Best Practices
# - Keep comprehensions readable.
# - Avoid deeply nested comprehensions.
# - Use comprehensions for simple transformations.

# Example: Use descriptive variable names
words = ["apple", "banana", "cherry"]
word_lengths = [len(word) for word in words]
print("Best Practice: Word lengths:", word_lengths)  # [5, 6, 6]


# ---------------------------------------------------------------------
# 7. Key Takeaways & Summary

# Mapping variable names to types
summary = {
    "numbers": type(numbers),
    "squares": type(squares),
    "even_squares": type(even_squares),
    "flattened": type(flattened),
    "cubes": type(cubes),
    "empty_result": type(empty_result),
    "filtered": type(filtered),
    "int_numbers": type(int_numbers),
    "word_lengths": type(word_lengths),
}

print("\nSummary: Variable types in this script:")
for name, typ in summary.items():
    print(f"{name}: {typ.__name__}")

print("\nKey Takeaways:")
print("- List comprehensions are concise and readable for simple list transformations.")
print("- Use filtering to include only desired elements.")
print("- Avoid complex or deeply nested comprehensions for maintainability.")
print("- Always consider edge cases (empty lists, None values, type conversions).")
