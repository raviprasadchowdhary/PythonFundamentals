"""
Dictionaries in Python: A Concise Educational Guide

This script introduces Python dictionaries, covering creation, access, modification,
common operations, edge cases, and best practices. Each concept is explained with
comments and demonstrated with example code and outputs.
"""

# ---------------------------------------------------------------------
# 1. What is a Dictionary?
# Dictionaries are mutable, unordered collections of key-value pairs.
# Keys must be unique and immutable (e.g., strings, numbers, tuples).
# Values can be any type.

my_dict = {'name': 'Alice', 'age': 30, 'is_student': False}
print("Dictionary:", my_dict)

print()


# ---------------------------------------------------------------------
# 2. Creating Dictionaries
# You can create dictionaries using curly braces or the dict() constructor.

empty_dict = {}
person = dict(name='Bob', age=25)
print("Empty dictionary:", empty_dict)
print("Person dictionary:", person)

print()


# ---------------------------------------------------------------------
# 3. Accessing Values
# Use square brackets or the get() method to access values by key.

print("Name:", my_dict['name'])           # Direct access
print("Age (using get):", my_dict.get('age'))  # Safe access

# Edge case: Accessing a non-existent key raises KeyError
# print(my_dict['height'])  # Uncomment to see KeyError

print("Height (using get, default):", my_dict.get('height', 'Unknown'))

print()


# ---------------------------------------------------------------------
# 4. Adding and Updating Entries
# Assign a value to a key to add or update entries.

my_dict['height'] = 165         # Add new key-value pair
my_dict['age'] = 31             # Update existing value
print("Updated dictionary:", my_dict)

print()


# ---------------------------------------------------------------------
# 5. Removing Entries
# Use pop(), popitem(), or del to remove items.

removed_age = my_dict.pop('age')        # Removes by key, returns value
print("Removed age:", removed_age)
print("After pop:", my_dict)

# Removes and returns last inserted item (Python 3.7+)
last_item = my_dict.popitem()
print("Removed last item:", last_item)
print("After popitem:", my_dict)

del my_dict['name']                     # Removes by key, no return value
print("After del:", my_dict)

print()


# ---------------------------------------------------------------------
# 6. Iterating Over Dictionaries
# You can iterate over keys, values, or key-value pairs.

sample = {'a': 1, 'b': 2, 'c': 3}
print("Keys:")
for key in sample:
    print(key)

print("Values:")
for value in sample.values():
    print(value)

print("Items:")
for key, value in sample.items():
    print(f"{key}: {value}")

print()


# ---------------------------------------------------------------------
# 7. Dictionary Methods and Operations
# Useful methods: keys(), values(), items(), update(), clear(), copy()

d = {'x': 10, 'y': 20}
print("Keys:", list(d.keys()))
print("Values:", list(d.values()))
print("Items:", list(d.items()))

d.update({'z': 30})      # Adds/updates entries from another dict
print("After update:", d)

d_copy = d.copy()        # Shallow copy
print("Copy of dictionary:", d_copy)

d.clear()                # Removes all items
print("After clear:", d)

print()


# ---------------------------------------------------------------------
# 8. Edge Cases and Best Practices
# - Keys must be immutable types (e.g., str, int, tuple).
# - Avoid using mutable types (e.g., lists) as keys.
# - Use get() to avoid KeyError when accessing keys.
# - Dictionary comprehensions for concise creation.

# Edge case: Using a list as a key (will raise TypeError)
# bad_dict = {[1, 2]: "value"}  # Uncomment to see TypeError

# Dictionary comprehension example
squares = {n: n**2 for n in range(5)}
print("Squares dictionary (comprehension):", squares)

print()


# ---------------------------------------------------------------------
# 9. Summary and Key Takeaways

# Mapping variable names to their types
summary = {
    'my_dict': type(my_dict),
    'empty_dict': type(empty_dict),
    'person': type(person),
    'sample': type(sample),
    'd': type(d),
    'squares': type(squares)
}
print("Variable types summary:", summary)

print("\nKey Takeaways:")
print("- Dictionaries store key-value pairs.")
print("- Keys must be unique and immutable.")
print("- Use get() for safe access.")
print("- Dictionary comprehensions are powerful for creating dictionaries.")
print("- Many useful methods: keys(), values(), items(), update(), pop(), clear(), copy().")
