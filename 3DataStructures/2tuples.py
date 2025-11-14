"""
Tuples in Python: A Concise Educational Guide

This script introduces Python tuples, covering their creation, properties, common operations,
edge cases, and best practices. Each section includes explanations and example code with outputs.
"""

# ---------------------------------------------------------------------
# What is a Tuple?
# Tuples are immutable, ordered collections of items. They can store mixed data types.

example_tuple = (1, "apple", 3.14)
print("Example tuple:", example_tuple)

print()


# ---------------------------------------------------------------------
# Creating Tuples
# Tuples can be created with parentheses, or without (comma is key).

tuple_with_parentheses = (10, 20, 30)
tuple_without_parentheses = 10, 20, 30
single_element_tuple = (42,)  # Note the comma!
not_a_tuple = (42)  # This is just an integer

print("Tuple with parentheses:", tuple_with_parentheses)
print("Tuple without parentheses:", tuple_without_parentheses)
print("Single element tuple:", single_element_tuple)
print("Not a tuple (just an int):", not_a_tuple, type(not_a_tuple))

print()


# ---------------------------------------------------------------------
# Accessing Tuple Elements
# Use indexing and slicing, similar to lists.

sample = ('a', 'b', 'c', 'd', 'e')
print("First element:", sample[0])
print("Last element:", sample[-1])
print("Slice [1:4]:", sample[1:4])

print()


# ---------------------------------------------------------------------
# Tuple Immutability
# Tuples cannot be changed after creation.

immutable = (1, 2, 3)
try:
    immutable[0] = 99
except TypeError as e:
    print("Immutability demo:", e)

print()


# ---------------------------------------------------------------------
# Common Tuple Operations
# Length, concatenation, repetition, membership.

t1 = (1, 2)
t2 = (3, 4)
print("Length:", len(t1))
print("Concatenation:", t1 + t2)
print("Repetition:", t1 * 3)
print("Membership (2 in t1):", 2 in t1)

print()


# ---------------------------------------------------------------------
# Tuple Packing and Unpacking
# Assign multiple values at once, or extract them.

packed = ("Alice", 25, "Engineer")
name, age, profession = packed
print("Unpacked values:", name, age, profession)

print()


# ---------------------------------------------------------------------
# Edge Cases
# Empty tuple, nested tuples, tuples with mutable elements.

empty = ()
nested = ((1, 2), (3, 4))
mutable_inside = ([1, 2], [3, 4])  # Lists inside tuple

print("Empty tuple:", empty)
print("Nested tuple:", nested)
print("Tuple with mutable elements:", mutable_inside)
mutable_inside[0].append(99)
print("After mutation:", mutable_inside)  # The list inside tuple can change

print()


# ---------------------------------------------------------------------
# Best Practices
# Use tuples for fixed collections, unpacking, and as dictionary keys.

coordinate = (10, 20)
locations = {coordinate: "Home"}
print("Tuple as dict key:", locations)

print()


# ---------------------------------------------------------------------
# Summary: Variable Types and Key Takeaways

variables = {
    "example_tuple": type(example_tuple),
    "single_element_tuple": type(single_element_tuple),
    "not_a_tuple": type(not_a_tuple),
    "empty": type(empty),
    "nested": type(nested),
    "mutable_inside": type(mutable_inside),
}

print("Variable types summary:")
for var, typ in variables.items():
    print(f"{var}: {typ}")

print("\nKey Takeaways:")
print("- Tuples are immutable and ordered.")
print("- Use a comma for single-element tuples.")
print("- Tuples can store mixed types and be nested.")
print("- Mutable objects inside tuples can change.")
print("- Useful for fixed collections and unpacking.")
