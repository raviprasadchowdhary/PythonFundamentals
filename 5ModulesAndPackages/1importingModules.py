import math
from math import pi, ceil
import random as rnd
from math import factorial as fact
from math import *
import sys

"""
importingModules.py

A concise, educational guide to importing modules in Python.
Covers: basic imports, importing specific items, aliases, wildcard imports, module search path, best practices, and edge cases.
"""

# ---------------------------------------------------------------------
# 1. Basic Import
# Importing an entire module allows access to all its functions and variables via the module name.


print("math.sqrt(16) =", math.sqrt(16))  # Output: 4.0

# ---------------------------------------------------------------------
# 2. Importing Specific Items
# You can import only what you need from a module.


print("pi =", pi)            # Output: 3.141592653589793
print("ceil(2.3) =", ceil(2.3))  # Output: 3

# ---------------------------------------------------------------------
# 3. Importing with Aliases
# Use 'as' to give a module or item a shorter or more convenient name.


# Output: random integer between 1 and 10
print("rnd.randint(1, 10) =", rnd.randint(1, 10))


print("fact(5) =", fact(5))  # Output: 120

# ---------------------------------------------------------------------
# 4. Wildcard Import (Not Recommended)
# Imports all names from a module into the current namespace.
# Can cause name clashes and is discouraged.


print("sin(pi/2) =", sin(pi/2))  # Output: 1.0

# ---------------------------------------------------------------------
# 5. Module Search Path
# Python searches for modules in sys.path. You can view or modify it.


print("Module search path:", sys.path)

# ---------------------------------------------------------------------
# 6. Importing Custom Modules (Edge Case)
# If you have a local module (e.g., mymodule.py), you can import it if it's in the search path.
# For demonstration, we'll show how to handle ImportError.

try:
    # This will fail unless mymodule.py exists in the same directory.
    import mymodule
except ImportError:
    print("Custom module 'mymodule' not found (edge case demonstration).")

# ---------------------------------------------------------------------
# 7. Best Practices
# - Avoid wildcard imports.
# - Use aliases for clarity.
# - Import only what you need.
# - Place imports at the top of your file.

# ---------------------------------------------------------------------
# 8. Summary: Mapping Variable Names to Their Types

summary = {
    "math": type(math),
    "pi": type(pi),
    "rnd": type(rnd),
    "fact": type(fact),
    "sys": type(sys)
}

print("\nSummary: Variable names and their types")
for name, typ in summary.items():
    print(f"{name}: {typ}")

# ---------------------------------------------------------------------
# Key Takeaways
# - Use 'import module' for full access.
# - Use 'from module import name' for specific items.
# - Use aliases for convenience.
# - Avoid wildcard imports.
# - Understand the module search path for custom modules.
