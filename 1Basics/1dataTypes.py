# dataTypes.py
"""
dataTypes.py
A beginner-friendly script demonstrating basic Python data types and simple operations.
This script covers:
- Primitive data types: int, float, str, bool
- Lists: creation, indexing, slicing, and common list methods
- Tuples: immutable sequences
- Dictionaries: key-value pairs
- Sets: unique, unordered collections
- Mutability: which types can be changed after creation
- Type checking: using the type() function
- Type conversion: converting between data types
Each section includes print statements and comments to help you understand how these data types work in Python.
Sections:
-----------
1. Primitive Data Types
    - Shows how to create and print integers, floats, strings, and booleans.
2. Lists
    - Demonstrates list creation, indexing, slicing, and common list operations like append, insert, pop, remove, extend, and list comprehensions.
3. Tuples
    - Shows how to create and access immutable tuples.
4. Dictionaries
    - Demonstrates how to create and print dictionaries (key-value pairs).
5. Sets
    - Shows how to create and print sets (collections of unique items).
6. Mutability
    - Explains which data types can be changed (mutable) and which cannot (immutable).
7. Type Checking
    - Uses the type() function to display the type of each variable.
8. Type Conversion
    - Demonstrates converting between different data types (e.g., int to float, list to tuple).
9. Summary
    - Prints a summary of the types of all main variables.
Additional inline comments are provided throughout the code to explain each step and operation, making it easier for beginners to follow along and understand the concepts.
"""
# A beginner-friendly script showing basic Python data types and simple operations.

# -------------------------------
# Primitive Data Types
# -------------------------------
age = 20                # Integer (whole number)
height = 5.9            # Float (decimal number)
name = "Alice"          # String (text)
is_student = True       # Boolean (True or False)

print("Age:", age)
print("Height:", height)
print("Name:", name)
print("Is Student:", is_student)
print()  # Blank line

# -------------------------------
# Lists
# -------------------------------
fruits = ['apple', 'banana', 'cherry']  # List of strings
print("Fruits List:", fruits)
print("First fruit:", fruits[0])        # Indexing (starts at 0)
print("Last fruit:", fruits[-1])        # Negative index for last item
print("First two fruits:", fruits[:2])  # Slicing

# List operations
fruits_demo = fruits.copy()             # Make a copy to keep original safe
fruits_demo.append('date')              # Add to end
fruits_demo.insert(1, 'blueberry')      # Insert at position 1
popped_item = fruits_demo.pop()         # Remove last item
fruits_demo.remove('apple')             # Remove by value
fruits_demo.extend(['elderberry', 'fig'])  # Add multiple items

print("Demo after changes:", fruits_demo)
print("Popped item:", popped_item)
print("Sorted demo:", sorted(fruits_demo))  # New sorted list

# List comprehension (make a new list with all uppercase)
fruits_upper = [f.upper() for f in fruits]
print("Uppercase fruits:", fruits_upper)
print()

# -------------------------------
# Tuples
# -------------------------------
coordinates = (10.0, 20.0)              # Tuple (cannot change)
print("Coordinates:", coordinates)
print("X value:", coordinates[0])
print("Y value:", coordinates[1])
print()

# -------------------------------
# Dictionaries
# -------------------------------
person = {"name": "Bob", "age": 25, "city": "New York"}
print("Person:", person)
print()

# -------------------------------
# Sets
# -------------------------------
unique_numbers = {1, 2, 3, 4, 5}        # Set (unique, unordered)
print("Unique Numbers:", unique_numbers)
print()

# -------------------------------
# Mutability
# -------------------------------
fruits.append("orange")                 # Lists can change
print("Updated Fruits:", fruits)

person["age"] = 26                      # Dictionaries can change
print("Updated Person:", person)

# Tuples cannot change
print("Coordinates (unchanged):", coordinates)
print("Unique Numbers (unchanged):", unique_numbers)
print()

# -------------------------------
# Type Checking
# -------------------------------
print("Type of age:", type(age))
print("Type of height:", type(height))
print("Type of name:", type(name))
print("Type of is_student:", type(is_student))
print("Type of fruits:", type(fruits))
print("Type of coordinates:", type(coordinates))
print("Type of person:", type(person))
print("Type of unique_numbers:", type(unique_numbers))
print()

# -------------------------------
# Type Conversion
# -------------------------------
age_float = float(age)                   # int to float
print("Age as Float:", age_float)

height_int = int(height)                 # float to int (truncates)
print("Height as Integer:", height_int)

age_str = "30"
if age_str.isdigit():
    age_converted = int(age_str)         # str to int (if possible)
else:
    age_converted = None
print("Converted Age from String:", age_converted)

fruits_tuple = tuple(fruits)             # list to tuple
print("Fruits as Tuple:", fruits_tuple)

coordinates_list = list(coordinates)     # tuple to list
print("Coordinates as List:", coordinates_list)

person_keys = list(person.keys())        # dict keys to list
print("Person Keys as List:", person_keys)

unique_numbers_list = list(unique_numbers)  # set to list
print("Unique Numbers as List:", unique_numbers_list)
print()

# -------------------------------
# Summary
# -------------------------------
print("Data Types Summary:")
print(" - age:", type(age))
print(" - height:", type(height))
print(" - name:", type(name))
print(" - is_student:", type(is_student))
print(" - fruits:", type(fruits))
print(" - coordinates:", type(coordinates))
print(" - person:", type(person))
print(" - unique_numbers:", type(unique_numbers))
print()
