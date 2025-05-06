import re

text = "Dear Harry, This python course is nice. Thank you so much"
punctuations = [".", ",", "!", "?"]
result = ""

for char in text:
    result += char
    if char in punctuations:
        result += "\n"  # or "\t", or "\n\t" based on what you want

print(result)



text = "Dear Harry, This python course is nice. Thank you so much"

# Add \n after each punctuation (.,!,?)
new_text = re.sub(r'([.,!?])', r'\1\n', text)

print(new_text)
