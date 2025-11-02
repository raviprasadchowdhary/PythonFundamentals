# variables.py
# This script demonstrates various data types in Python,
# including primitive and complex types, along with type checking and type conversion.

# Primitive Data Types in Python: Integers, Floats, Strings, Booleans
age = 20  # Integer
height = 5.9  # Float
name = "Alice"  # String
is_student = True  # Boolean
print("Age:", age)
print("Height:", height)
print("Name:", name)
print("Is Student:", is_student)
print()  # Blank line for readability

# Complex Data Types in Python: Lists, Tuples, Dictionaries, Sets
# List
fruits = ["apple", "banana", "cherry"]
print("Fruits List:", fruits)

# Tuple
coordinates = (10.0, 20.0)
print("Coordinates Tuple:", coordinates)

# Dictionary
person = {"name": "Bob", "age": 25, "city": "New York"}
print("Person Dictionary:", person)

# Set
unique_numbers = {1, 2, 3, 4, 5}
print("Unique Numbers Set:", unique_numbers)


# Demonstrating Mutability
# Lists and Dictionaries are mutable
fruits.append("orange")
print("Updated Fruits List:", fruits)

person["age"] = 26
print("Updated Person Dictionary:", person)

# Tuples and Sets are immutable (Tuples) or unordered (Sets)
# Attempting to change a tuple will raise an error

# coordinates[0] = 15.0  # This will raise a TypeError
# Sets do not support indexing
print("Coordinates Tuple remains unchanged:", coordinates)
print("Unique Numbers Set remains unchanged:", unique_numbers)
print()  # Blank line for readability


# Type Checking
print("Type of age:", type(age))
print("Type of height:", type(height))
print("Type of name:", type(name))
print("Type of is_student:", type(is_student))
print("Type of fruits:", type(fruits))
print("Type of coordinates:", type(coordinates))
print("Type of person:", type(person))
print("Type of unique_numbers:", type(unique_numbers))
print()  # Blank line for readability

# Type Conversion
# Converting Integer to Float
age_float = float(age)
print("Age as Float:", age_float)
# Converting Float to Integer
height_int = int(height)
print("Height as Integer:", height_int)
# Converting String to Integer (if possible)
age_str = "30"
age_converted = int(age_str) if age_str.isdigit() else None
print("Converted Age from String:", age_converted)
# Converting List to Tuple
fruits_tuple = tuple(fruits)
print("Fruits as Tuple:", fruits_tuple)
# Converting Tuple to List
coordinates_list = list(coordinates)
print("Coordinates as List:", coordinates_list)
# Converting Dictionary Keys to List
person_keys = list(person.keys())
print("Person Keys as List:", person_keys)
# Converting Set to List
unique_numbers_list = list(unique_numbers)
print("Unique Numbers as List:", unique_numbers_list)
print()  # Blank line for readability

# Summary of Data Types
data_types_summary = {
    "age": type(age),
    "height": type(height),
    "name": type(name),
    "is_student": type(is_student),
    "fruits": type(fruits),
    "coordinates": type(coordinates),
    "person": type(person),
    "unique_numbers": type(unique_numbers)
}
print("Data Types Summary:")
for var_name, var_type in data_types_summary.items():
    print(f" - {var_name}: {var_type}")

print()  # Blank line for readability
# End of variables.py
