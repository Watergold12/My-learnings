import string

user_input = input("Enter a string: ")
no_punct = user_input.translate(str.maketrans('', '', string.punctuation))
cleaned = "_".join(no_punct.split()).lower()

print("Cleaned string:", cleaned)
