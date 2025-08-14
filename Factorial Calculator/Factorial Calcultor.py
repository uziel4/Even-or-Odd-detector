"""
Author: Uziel E. Santos Rodriguez
Description:Calculates the factorial of the selected number.
Date:2025/08/14
"""
# This function calculate the factorial of a determined number with no recursion
def factorial (n: int)-> int:
    # Here we determine if the number is negative. If negative we raise a value error
    if n < 0:
        raise ValueError("Factorial is undefined for negative numbers")
    result = 1

    # For loop that calculates the factorial
    for j in range (2, n + 1):
        result *= j
    return result
# This function calculates the factorial of the determined number using Recursion.
# This function can cause problems if we choose big numbers.
def recursive_factorial (n: int) -> int:

    # Here we determine if the number is negative. If negative we raise a value error
    if n < 0:
        raise ValueError("Factorial is undefined for negative numbers")
    if n in (0,1):
        return 1
    return  n * recursive_factorial(n-1)

# Main function
def main():
    try:
        n = int(input("Enter a non negative number: "))
        print("Recursive Version:")
        print(f"{n}! = {recursive_factorial(n)}")
        print("No Recursion version: ")
        print(f"{n}! = {factorial(n)}")
    except ValueError as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    main()





