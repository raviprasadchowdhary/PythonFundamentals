"""
lambdaFunctions.py

A concise, educational guide to Python lambda functions.
Covers: syntax, usage, common operations, edge cases, and best practices.
"""

# ---------------------------------------------------------------------
# Introduction to Lambda Functions
# ---------------------------------------------------------------------
# Lambda functions are small anonymous functions defined with the 'lambda' keyword.
# Syntax: lambda arguments: expression


def add(x, y): return x + y


print("add(2, 3):", add(2, 3))  # Output: 5

# ---------------------------------------------------------------------
# Lambda Functions vs Regular Functions
# ---------------------------------------------------------------------
# Lambda functions are limited to a single expression.
# Regular functions can have multiple statements.


def add_func(x, y):
    return x + y


print("add_func(2, 3):", add_func(2, 3))  # Output: 5

# ---------------------------------------------------------------------
# Using Lambda with Built-in Functions (map, filter, sorted)
# ---------------------------------------------------------------------
# Lambdas are often used with functions like map, filter, and sorted.

numbers = [1, 2, 3, 4, 5]

squared = list(map(lambda x: x ** 2, numbers))
print("Squared numbers:", squared)  # Output: [1, 4, 9, 16, 25]

evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", evens)  # Output: [2, 4]

words = ['apple', 'banana', 'cherry', 'date']
sorted_words = sorted(words, key=lambda w: len(w))
# Output: ['date', 'apple', 'banana', 'cherry']
print("Words sorted by length:", sorted_words)

# ---------------------------------------------------------------------
# Lambda Functions in List Comprehensions
# ---------------------------------------------------------------------
# Lambdas can be used inside list comprehensions for concise operations.

triple = [(lambda x: x * 3)(n) for n in numbers]
print("Triple each number:", triple)  # Output: [3, 6, 9, 12, 15]

# ---------------------------------------------------------------------
# Edge Cases and Limitations
# ---------------------------------------------------------------------
# 1. Lambdas can't contain statements (e.g., assignments, print).
# 2. Only expressions are allowed.
# 3. Readability can suffer if overused.

# Example of invalid lambda (will cause SyntaxError if uncommented):
# invalid = lambda x: print(x)  # Not allowed

# ---------------------------------------------------------------------
# Best Practices
# ---------------------------------------------------------------------
# - Use lambdas for simple, short functions.
# - Prefer regular functions for complex logic.
# - Name lambdas only if reused; otherwise, use inline.

# Example: Inline lambda in map
# Output: [2, 3, 4, 5, 6]
print("Incremented numbers:", list(map(lambda x: x + 1, numbers)))

# Example: Named lambda for reuse


def multiply(a, b): return a * b


print("multiply(4, 5):", multiply(4, 5))  # Output: 20

# ---------------------------------------------------------------------
# Summary and Key Takeaways
# ---------------------------------------------------------------------
# Variable types:
#   add: function
#   add_func: function
#   squared: list
#   evens: list
#   sorted_words: list
#   triple: list
#   multiply: function

# Key Takeaways:
# - Lambda functions are concise, anonymous, and limited to single expressions.
# - Useful with functions like map, filter, and sorted.
# - Avoid complex logic in lambdas for readability.
# - Prefer regular functions for multi-line or reusable logic.
