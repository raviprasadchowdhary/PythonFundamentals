"""
argumentsAndReturnValues.py

A concise, educational guide to Python function arguments and return values.
Covers: positional arguments, keyword arguments, default values, variable-length arguments (*args, **kwargs), return values, edge cases, and best practices.
"""

# ---------------------------------------------------------------------
# 1. Positional Arguments
# Positional arguments are passed to functions in order.


def add(a, b):
    """Returns the sum of a and b."""
    return a + b


print("Positional Arguments Example:", add(2, 3))  # Output: 5

# ---------------------------------------------------------------------
# 2. Keyword Arguments
# Arguments can be passed by name, regardless of order.


def greet(name, greeting):
    """Greets a person with a given greeting."""
    return f"{greeting}, {name}!"


print("Keyword Arguments Example:", greet(
    name="Alice", greeting="Hello"))  # Output: Hello, Alice!

# ---------------------------------------------------------------------
# 3. Default Argument Values
# Functions can have default values for arguments.


def power(base, exponent=2):
    """Raises base to the power of exponent (default is 2)."""
    return base ** exponent


print("Default Argument Example:", power(5))         # Output: 25
print("Default Argument Example:", power(2, 3))      # Output: 8

# ---------------------------------------------------------------------
# 4. Variable-Length Arguments (*args and **kwargs)
# *args collects extra positional arguments as a tuple.
# **kwargs collects extra keyword arguments as a dictionary.


def summarize(*args, **kwargs):
    """Prints positional and keyword arguments."""
    print("Positional args:", args)
    print("Keyword args:", kwargs)


summarize(1, 2, 3, a=4, b=5)
# Output:
# Positional args: (1, 2, 3)
# Keyword args: {'a': 4, 'b': 5}

# ---------------------------------------------------------------------
# 5. Return Values
# Functions can return values using 'return'. Multiple values are returned as a tuple.


def divide_and_remainder(a, b):
    """Returns quotient and remainder of a divided by b."""
    return a // b, a % b


quotient, remainder = divide_and_remainder(10, 3)
print("Return Values Example:", quotient, remainder)  # Output: 3 1

# ---------------------------------------------------------------------
# 6. Edge Cases
# - Missing required arguments raises TypeError.
# - Returning without a value returns None.
# - Mutable default arguments can lead to bugs.


def no_return():
    """Function with no return statement."""
    pass


print("No Return Example:", no_return())  # Output: None


def append_to_list(value, my_list=None):
    """Avoids mutable default argument pitfall."""
    if my_list is None:
        my_list = []
    my_list.append(value)
    return my_list


print("Mutable Default Example:", append_to_list(1))  # Output: [1]
print("Mutable Default Example:", append_to_list(2))  # Output: [2]

# ---------------------------------------------------------------------
# 7. Best Practices
# - Use descriptive argument names.
# - Document argument types and return values.
# - Avoid mutable default arguments.
# - Use keyword arguments for clarity.

# ---------------------------------------------------------------------
# 8. Summary

# Variable names and their types (from above):
# a, b, base, exponent, name, greeting: int or str
# args: tuple
# kwargs: dict
# quotient, remainder: int
# my_list: list

# Key Takeaways:
# - Arguments can be positional, keyword, or variable-length.
# - Default values simplify function calls.
# - Functions return values using 'return'.
# - Avoid mutable default arguments.
# - Use print statements to verify outputs.

# End of script.
