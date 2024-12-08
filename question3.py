"""
3. Write a Python program to take a list of numbers as input from the user
 and print the largest number in the list.
"""


def largest_number_finder(numbers):
    largest_number = 0

    for number in numbers:
        if number > largest_number:
            largest_number = number
    
    return largest_number


input_numbers = list(map(int, input("Enter the integers in the list separated by comma: ").split(",")))

largest_int = largest_number_finder(input_numbers)

print(f"\nThe largest number among the numbers {", ".join(map(str, input_numbers))} is {largest_int}.")