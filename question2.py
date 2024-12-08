"""
2. Write a Python program that takes a string input from the user, converts
 it to lowercase, and prints both the original string and the lowercase
 version.

"""


def word_to_lowercase(word):
    word_in_lowercase = word.lower()

    return word, word_in_lowercase


input_string = input("Enter a word you want to convert to lowercase: ")

original_string, lower_string = word_to_lowercase(input_string)

print("\n----DISPLAYING THE ORIGINAL AND LOWERED STRING-----")
print(f"\nOriginla String: {original_string}")
print(f"Word In Lowercase: {lower_string}")