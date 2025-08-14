"""
Author: Uziel E. Santos Rodriguez
Description: On this project will determine whether the number introduced by the user is Prime or not.
Date: 2025/08/14

"""
# This function will return True if the number is prime and False if the number is not prime
def is_prime(n: int)->bool:

    # If the number is less than 2 (1,0,-1,-2). They are not prime numbers
    if  n < 2:
        return False

    # On this step we test all posible from 2 to n-1. If one of them give us reminder 0, is not prime
    for i in range (2,n):

        if n % i == 0:
            return False

    return True

def main():
    # Ask the user for the number
    number= int(input("Enter an integer: "))

    # Display of the results to the user
    print(f"{number} is {'Prime' if is_prime(number) else 'not prime'}")

if __name__ == "__main__":
    main()

