"""
For & While Loops in Python: Educational Guide

This script introduces the basics of for and while loops in Python.
It covers syntax, common operations, edge cases, and best practices,
with examples and output for clarity.
"""

# ---------------------------------------------------------------------
# Section 1: For Loops
# ---------------------------------------------------------------------
# For loops are used to iterate over sequences (lists, strings, tuples, etc.).
# They execute a block of code for each item in the sequence.

print("For loop over a list:")
numbers = [1, 2, 3, 4]
for num in numbers:
    print(num)  # Output: 1 2 3 4

print("\nFor loop over a string:")
word = "loop"
for char in word:
    print(char)  # Output: l o o p

print("\nFor loop with range():")
for i in range(3):
    print(i)  # Output: 0 1 2

# Edge case: Empty sequence
print("\nFor loop over an empty list:")
empty_list = []
for item in empty_list:
    print(item)  # No output

# Best practice: Use descriptive variable names
print("\nFor loop with descriptive variable names:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# ---------------------------------------------------------------------
# Section 2: While Loops
# ---------------------------------------------------------------------
# While loops execute a block of code as long as a condition is True.

print("\nWhile loop with a counter:")
count = 0
while count < 3:
    print(count)
    count += 1  # Output: 0 1 2

# Edge case: Condition is False at start
print("\nWhile loop with False condition at start:")
flag = False
while flag:
    print("This will not print.")

# Best practice: Avoid infinite loops by ensuring the condition will eventually be False
print("\nWhile loop with break statement:")
n = 0
while True:
    print(n)
    n += 1
    if n == 2:
        break  # Output: 0 1

# ---------------------------------------------------------------------
# Section 3: Loop Control Statements
# ---------------------------------------------------------------------
# Use 'break' to exit a loop early, 'continue' to skip to the next iteration.

print("\nUsing continue in a for loop:")
for i in range(5):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)  # Output: 1 3

print("\nUsing else with loops:")
for i in range(3):
    print(i)
else:
    print("Loop finished!")  # Output: 0 1 2 Loop finished!

# ---------------------------------------------------------------------
# Section 4: Summary & Key Takeaways
# ---------------------------------------------------------------------
# Variable types used:
# numbers (list), word (str), i (int), empty_list (list), fruits (list), fruit (str), count (int), flag (bool), n (int)
#
# Key takeaways:
# - For loops iterate over sequences; while loops repeat based on conditions.
# - Use range() for numeric loops.
# - Always ensure while loop conditions will eventually be False.
# - Use break and continue for finer control.
# - else can be used with loops for post-loop actions.

print("\nEnd of guide: For & While loops in Python.")
