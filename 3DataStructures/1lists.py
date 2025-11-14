"""
Python Lists: A Concise Educational Guide

This script introduces Python lists, covering creation, indexing, slicing, modification,
common operations, edge cases, and best practices. Each concept is explained with comments
and demonstrated with example code and outputs.
"""

# ---------------------------------------------------------------------
# 1. List Creation
# Lists are ordered, mutable collections that can hold items of any type.

numbers = [1, 2, 3, 4, 5]
mixed = [1, "two", 3.0, [4, 5]]
empty = []

print("numbers:", numbers)
print("mixed:", mixed)
print("empty:", empty)
print()

# ---------------------------------------------------------------------
# 2. Indexing and Slicing
# Access elements by index (zero-based). Slicing extracts sublists.

print("First element:", numbers[0])
print("Last element:", numbers[-1])
print("Slice [1:4]:", numbers[1:4])
print()

# Edge case: Index out of range raises an error
try:
    print(numbers[10])
except IndexError as e:
    print("IndexError:", e)
print()

# ---------------------------------------------------------------------
# 3. Modifying Lists
# Lists are mutable: you can change, add, or remove elements.

numbers[2] = 99
print("After modification:", numbers)

numbers.append(6)
print("After append:", numbers)

numbers.insert(1, 42)
print("After insert at index 1:", numbers)

removed = numbers.pop()
print("After pop (removes last):", numbers, "| Popped value:", removed)

del numbers[0]
print("After deleting first element:", numbers)
print()

# ---------------------------------------------------------------------
# 4. Common Operations
# Useful built-in functions and methods for lists.

length = len(numbers)
print("Length of numbers:", length)

exists = 42 in numbers
print("Is 42 in numbers?", exists)

count_99 = numbers.count(99)
print("Count of 99:", count_99)

numbers.extend([7, 8])
print("After extend:", numbers)

numbers.sort()
print("After sort:", numbers)
print()

# ---------------------------------------------------------------------
# 5. Edge Cases and Best Practices
# Lists can contain duplicates and mixed types, but mixing types may reduce code clarity.

duplicates = [1, 1, 2, 2]
print("List with duplicates:", duplicates)

mixed_types = [1, "two", 3.0]
print("List with mixed types:", mixed_types)

# Best practice: Prefer lists of consistent types for maintainability.
# Avoid modifying lists while iterating over them.

# Edge case: Removing items while iterating
sample = [1, 2, 3, 4]
for item in sample[:]:  # Iterate over a copy to avoid issues
    if item % 2 == 0:
        sample.remove(item)
print("After removing even numbers safely:", sample)
print()

# ---------------------------------------------------------------------
# 6. Summary and Key Takeaways

print("Summary:")
print("numbers:", numbers, "| type:", type(numbers))
print("mixed:", mixed, "| type:", type(mixed))
print("empty:", empty, "| type:", type(empty))
print()
print("Key takeaways:")
print("- Lists are ordered, mutable collections.")
print("- Use indexing and slicing to access elements.")
print("- Modify lists with append, insert, pop, del, extend, and sort.")
print("- Be cautious with edge cases (e.g., index out of range, modifying during iteration).")
print("- Prefer lists of consistent types for readability and maintainability.")
