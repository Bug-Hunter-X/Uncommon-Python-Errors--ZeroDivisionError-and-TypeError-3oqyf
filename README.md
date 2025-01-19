# Uncommon Python Errors

This repository demonstrates a simple Python function that can throw two types of errors that might be less frequently encountered than others such as IndexError or NameError:

1. **ZeroDivisionError**: Occurs when attempting to divide by zero.
2. **TypeError**: Occurs when performing an operation on incompatible data types (in this case, adding an integer to None).

The `bug.py` file contains the function with the errors. The `bugSolution.py` file provides a solution that handles these cases gracefully, preventing the errors from occurring.  The solution incorporates robust error handling techniques such as explicit checks for zero and None values.