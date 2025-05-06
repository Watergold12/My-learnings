"""Write a Python function called count_vowels that takes a
   string as input and returns the total count of vowels 
   (both uppercase and lowercase) in the string. Ignore 
   any other characters (such as spaces, punctuation, or numbers)."""

"""count_vowels("Hello, World!")  # Should return 3 (o, o, and o)
   count_vowels("Python is amazing")  # Should return 5 (o, i, a, i, and a)
   count_vowels("12345")  # Should return 0 (no vowels)"""

# def vowel_counting(string):
#     no_of_vowels = 0
#     vowel = "aeiouAEIOU"

#     for string in vowel:
#         no_of_vowels += 1

#     print(f"There are {no_of_vowels} vowels.")

# vowel_counting("hello world")
"""The above attempt was slight mistake!!"""

def vowel_counting(input_string):
    no_of_vowels = 0
    vowels = "aeiouAEIOU"  # A string containing all vowels (both lowercase and uppercase)

    for char in input_string:
        if char in vowels:
            no_of_vowels += 1

    return no_of_vowels

# Example usage
input_str = input("Enter the sentence to be evaluated: ")
result = vowel_counting(input_str)
print(f"There are {result} vowels in '{input_str}'.")