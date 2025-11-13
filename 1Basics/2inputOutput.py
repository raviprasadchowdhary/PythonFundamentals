"""
inputOutput.py

A concise, educational guide to Python's input and output operations.
Covers: printing, formatting, reading input, type conversion, edge cases, and best practices.
"""

# ---------------------------------------------------------------------
# Output with print()
# ---------------------------------------------------------------------
# The print() function displays output to the console.

print("Hello, World!")  # Basic output

# Printing multiple values
print("The answer is", 42)

# Using separators and end parameters
print("A", "B", "C", sep="-", end=" END\n")

# ---------------------------------------------------------------------
# String Formatting
# ---------------------------------------------------------------------
# Format output using f-strings (recommended in Python 3.6+)

name = "Alice"
age = 30
print(f"{name} is {age} years old.")

# Old-style formatting (not recommended)
print("%s is %d years old." % (name, age))

# str.format() method
print("{} is {} years old.".format(name, age))

# ---------------------------------------------------------------------
# Input with input()
# ---------------------------------------------------------------------
# The input() function reads a line from the user as a string.

user_input = input("Enter something: ")
print("You entered:", user_input)

# ---------------------------------------------------------------------
# Type Conversion
# ---------------------------------------------------------------------
# input() always returns a string. Convert to other types as needed.

num_str = input("Enter a number: ")
try:
    num = int(num_str)
    print(f"Square of {num} is {num ** 2}")
except ValueError:
    print("Invalid input! Please enter a valid integer.")

# ---------------------------------------------------------------------
# Edge Cases and Best Practices
# ---------------------------------------------------------------------
# Handling empty input
empty = input("Press Enter without typing: ")
if empty == "":
    print("You entered an empty string.")

# Stripping whitespace
raw = input("Enter text with spaces: ")
clean = raw.strip()
print(f"Stripped input: '{clean}'")

# Prompting for specific types
while True:
    try:
        value = float(input("Enter a floating-point number: "))
        print(f"You entered: {value}")
        break
    except ValueError:
        print("Please enter a valid floating-point number.")

# ---------------------------------------------------------------------
# Summary: Variable Types
# ---------------------------------------------------------------------
variables = {
    "name": type(name),
    "age": type(age),
    "user_input": type(user_input),
    "num": type(num),
    "clean": type(clean),
    "value": type(value),
}
print("\nVariable types summary:")
for var, typ in variables.items():
    print(f"{var}: {typ.__name__}")

# ---------------------------------------------------------------------
# Key Takeaways
# ---------------------------------------------------------------------
print("""
Key Takeaways:
- Use print() for output; f-strings for formatting.
- input() always returns a string; convert types as needed.
- Handle exceptions and edge cases for robust code.
""")
