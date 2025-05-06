import re

user_input = input("Enter a string: ")

# Lowercase
text = user_input.lower()

# Remove non-alphanumeric characters except spaces
text = re.sub(r'[^a-z0-9\s]', '', text)

# Replace spaces with dashes
slug = "-".join(text.split())

print("Slugified string:", slug)
