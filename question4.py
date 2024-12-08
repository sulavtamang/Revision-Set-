"""
4. Write a Python program to take a tuple of numbers as input from the
 user and print all the numbers in the tuple.
"""

def display_elements(numbers):
    for number in numbers:
        print(number, end = ",")
    


input_numbers = tuple(map(int, input("Enter the integers separated by comma: ").split(",")))
# print(input_numbers)
print(f"\n*****DISPLAYING ALL THE NUMBERS IN THE TUPLE: {input_numbers}:")
display_elements(input_numbers)
