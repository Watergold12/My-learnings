import re
import string

user_input = input("Enter a string: ")

# Remove all non-ASCII characters (like emojis)
no_emojis = re.sub(r'[^\x00-\x7F]+', '', user_input)

# Continue cleaning
no_punct = no_emojis.translate(str.maketrans('', '', string.punctuation))
cleaned = "_".join(no_punct.split()).lower()

print("Cleaned string:", cleaned)
