"""
1. Write a Python program to take two numbers as input from the user and
 print their sum, difference, product, and division. Ensure the program
 handles division by zero gracefully.

"""

def sum_generator(num1 = 1, num2 = 1):
    return num1 + num2

def difference_generator(num1 = 1, num2 = 1):
    return num1 - num2

def product_generator(num1 = 1, num2 = 1):
    return num1 * num2

def division(num1 = 1, num2 = 1):
    return num1 / num2


try:
    first_number = int(input("Enter the first integer: "))
    second_number = int(input("Enter the second integer: "))

    sum_result = sum_generator(first_number, second_number)
    diff_result = difference_generator(first_number, second_number)
    product_result = product_generator(first_number, second_number)
    divsion_result = division(first_number, second_number)

    #printing the results 
    print(f"\nSum: {sum_result}")
    print(f"\nDifference: {diff_result}")
    print(f"\nProduct: {product_result}")
    print(f"\nDivision: {divsion_result}")

except ValueError:
    print("\nPlease enter valid integers!!")

except ZeroDivisionError:
    print("\nThe divisor must be non-zero integer.")

finally:
    print("\nThank you!!")