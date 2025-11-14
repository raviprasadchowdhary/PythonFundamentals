"""
Python Sets: A Concise Educational Guide

This script introduces Python sets, covering creation, common operations,
edge cases, and best practices. Each concept is explained with comments
and demonstrated with example code and outputs.
"""

# ---------------------------------------------------------------------
# What is a Set?
# Sets are unordered collections of unique, immutable elements.
# They are useful for membership tests, removing duplicates, and set operations.

my_set = {1, 2, 3, 4}
print("Initial set:", my_set)

# ---------------------------------------------------------------------
# Creating Sets
# Sets can be created using curly braces {} or the set() constructor.

set_from_braces = {1, 2, 3}
set_from_constructor = set([3, 4, 5])
empty_set = set()  # Note: {} creates an empty dict, not a set

print("Set from braces:", set_from_braces)
print("Set from constructor:", set_from_constructor)
print("Empty set:", empty_set)

# ---------------------------------------------------------------------
# Adding and Removing Elements
# Use add() to add a single element, update() for multiple elements.
# Use remove() to delete an element (raises KeyError if not found).
# Use discard() to delete an element (no error if not found).

my_set.add(5)
print("After add(5):", my_set)

my_set.update([6, 7])
print("After update([6, 7]):", my_set)

my_set.remove(1)
print("After remove(1):", my_set)

my_set.discard(100)  # No error even though 100 is not present
print("After discard(100):", my_set)

# ---------------------------------------------------------------------
# Set Operations
# Sets support mathematical operations: union, intersection, difference, symmetric difference.

a = {1, 2, 3}
b = {3, 4, 5}

print("a:", a)
print("b:", b)
print("Union (a | b):", a | b)
print("Intersection (a & b):", a & b)
print("Difference (a - b):", a - b)
print("Symmetric Difference (a ^ b):", a ^ b)

# ---------------------------------------------------------------------
# Membership Testing
# Use 'in' and 'not in' to check for element presence.

print("Is 2 in a?", 2 in a)
print("Is 10 not in b?", 10 not in b)

# ---------------------------------------------------------------------
# Iterating Over Sets
# Sets are iterable, but unordered.

for element in a:
    print("Element in set a:", element)

# ---------------------------------------------------------------------
# Edge Cases
# Sets cannot contain mutable elements (e.g., lists, dicts).
# Attempting to add a list will raise a TypeError.

try:
    a.add([10, 20])
except TypeError as e:
    print("Error adding list to set:", e)

# ---------------------------------------------------------------------
# Best Practices
# Use sets for fast membership tests and removing duplicates.
# Use frozenset for immutable sets.

list_with_duplicates = [1, 2, 2, 3, 3, 3]
unique_elements = set(list_with_duplicates)
print("Unique elements from list:", unique_elements)

immutable_set = frozenset([1, 2, 3])
print("Immutable set (frozenset):", immutable_set)

# ---------------------------------------------------------------------
# Summary and Key Takeaways

print("\nSummary:")
print("my_set type:", type(my_set))
print("a type:", type(a))
print("immutable_set type:", type(immutable_set))
print("Key takeaways:")
print("- Sets store unique, unordered elements.")
print("- Use sets for membership tests and removing duplicates.")
print("- Sets do not support indexing or slicing.")
print("- Elements must be immutable (e.g., int, str, tuple).")
print("- Use frozenset for immutable sets.")
