#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function description:
    This function computes the factorial of a non-negative integer using recursion.

    Parameters:
    n (int): A non-negative integer for which the factorial is calculated.

    Returns:
    int: The factorial of the number n. If n is 0, the function returns 1.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Main program execution
f = factorial(int(sys.argv[1]))  # Call the factorial function with the command-line argument
print(f)  # Output the result of the factorial calculation

