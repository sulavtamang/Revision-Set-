"""
5. Write a Python program to define a dictionary with three keys (name,
 age, city) and assign any values to them, then print the dictionary.
"""


def display_dict(key_value):
    for key, value in key_value.items():
        print(f"{key.upper()} : {value}")



full_name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter the name of the city you live in: ")

user_info = {}
user_info.update({"name" : full_name, "age" : age, "city" : city})

#calling the function to display the dictionary
print("\n***** Displaying the user details *****")
display_dict(user_info)