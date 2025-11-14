"""
customExceptions.py

A concise, educational guide to Python custom exceptions.
Covers:
- Why and how to define custom exceptions
- Raising and handling custom exceptions
- Best practices and edge cases
"""

# ---------------------------------------------------------------------
# What are Custom Exceptions?
# ---------------------------------------------------------------------
# Custom exceptions allow you to define error types specific to your application.
# They help make error handling clearer and more meaningful.


class MyCustomError(Exception):
    """Basic custom exception."""
    pass


print("Defined MyCustomError as a custom exception.\n")

# ---------------------------------------------------------------------
# Custom Exceptions with Additional Information
# ---------------------------------------------------------------------
# You can add more context by overriding __init__ and __str__.


class ValidationError(Exception):
    def __init__(self, message, code):
        super().__init__(message)
        self.code = code

    def __str__(self):
        return f"ValidationError [{self.code}]: {self.args[0]}"


print("Defined ValidationError with extra info.\n")

# ---------------------------------------------------------------------
# Raising Custom Exceptions
# ---------------------------------------------------------------------
# Use 'raise' to trigger your custom exception.


def check_positive(value):
    """Raises MyCustomError if value is not positive."""
    if value <= 0:
        raise MyCustomError("Value must be positive.")


try:
    check_positive(-5)
except MyCustomError as e:
    print(f"Caught exception: {e}")

print()

# ---------------------------------------------------------------------
# Handling Custom Exceptions
# ---------------------------------------------------------------------
# Use try-except blocks to handle custom exceptions.


def validate_age(age):
    """Raises ValidationError if age is not in valid range."""
    if not (0 < age < 120):
        raise ValidationError("Invalid age", code=1001)
    return True


try:
    validate_age(150)
except ValidationError as ve:
    print(f"Caught exception: {ve}")

print()

# ---------------------------------------------------------------------
# Edge Cases: Inheritance and Catching Multiple Exceptions
# ---------------------------------------------------------------------
# Custom exceptions can inherit from built-in exceptions or other custom ones.


class MinorValidationError(ValidationError):
    pass


try:
    raise MinorValidationError("Minor issue", code=1002)
except ValidationError as ve:
    print(f"Caught as ValidationError: {ve}")

print()

# ---------------------------------------------------------------------
# Best Practices
# ---------------------------------------------------------------------
# - Name custom exceptions with 'Error' suffix.
# - Inherit from Exception (not BaseException).
# - Document exception purpose.
# - Use specific exceptions for clarity.


class DatabaseConnectionError(Exception):
    """Raised when database connection fails."""
    pass


try:
    raise DatabaseConnectionError("Could not connect to DB.")
except DatabaseConnectionError as dbe:
    print(f"Best practice example: {dbe}")

print()

# ---------------------------------------------------------------------
# Summary: Key Takeaways
# ---------------------------------------------------------------------
# - Custom exceptions clarify error handling.
# - Use inheritance for exception hierarchies.
# - Add context via attributes.
# - Always catch exceptions at appropriate levels.

# Variable type mapping (for reference)
summary = {
    "MyCustomError": type(MyCustomError),
    "ValidationError": type(ValidationError),
    "MinorValidationError": type(MinorValidationError),
    "DatabaseConnectionError": type(DatabaseConnectionError),
}

print("Summary of custom exception classes and their types:")
for name, typ in summary.items():
    print(f"{name}: {typ}")

print("\nEnd of customExceptions.py educational guide.")
