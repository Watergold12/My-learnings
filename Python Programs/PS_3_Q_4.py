user_input = input("Enter a string: ")

# This splits the string into words (removing *any* amount of whitespace), then joins with single space
cleaned = " ".join(user_input.split())

print("Cleaned string:", cleaned)
