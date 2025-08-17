

"""
Author: Uziel E. Santos Rodriguez
Description: This code project will calculate the Greatest Common Divisor (GCD) of two numbers using Python.
Date: 2025/17/08
"""

def gcd(a, b):
    # Convert both numbers to absolute values to handle negatives
    a, b = abs(a), abs(b)
    # While b is not zero, continue with Euclid's algorithm
    while b:
        # Update a and b: a takes the value of b, b takes the remainder of a divided by b
        a, b = b, a % b
    # When b is zero, a is the greatest common divisor
    return a

if __name__ == "__main__":
    # Example usage
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    
    # Calculate GCD
    result = gcd(num1, num2)
    
    # Print the result
    print(f"The GCD of {num1} and {num2} is: {result}")
    
    