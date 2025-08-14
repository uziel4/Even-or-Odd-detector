"""
Author: Uziel E. Santos Rodriguez

Description: This program will determine if an int number is Even or is it Odd. I utilized (%) module to determine whether the number is divisible by 2.
If the number is divisible by 2 is even else is Odd.

Date:2025/08/14

"""
#This function is responsable for determining whether the number is odd or even.
def even_or_odd(number):
    # This "if" will return even if the number is divisible by 2 else it will return Odd
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Main function
def main():
    # Here we will ask the user to enter the number desired to determine whether is even or odd and stored in the variable a called "num"
    num = int(input("Enter a number: "))
    # Here we will print the result in the display of the user.
    print(f"{num} is: {even_or_odd(num)}")





if __name__ == "__main__":
    main()
