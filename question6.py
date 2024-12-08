"""
6. Write a Python program that takes a string as input and counts how
 many times the letter a appears in it.
"""



def char_counter(word, letter):
    return word.count(letter)


input_string = input("Enter a string: ")
letter = input("Enter which letter you want to count: ")

char_number = char_counter(input_string, letter)
print(f"\nThe letter \"{letter}\" appears {char_number} times in the string \"{input_string}\".")