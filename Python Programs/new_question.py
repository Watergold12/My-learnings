# Write a Python program that takes a sentence as input and returns a dictionary where each word is a key, and the value is the number of times that word appears in the sentence.

# Here's the structure you can follow:

# ->Define a function word_count that takes a sentence as an argument.
# ->Split the sentence into words.
# ->Use a dictionary to count the occurrences of each word.
# ->Return the dictionary containing the word counts.

def word_count(sentence):
    # Split the sentence into words
    words = sentence.split()
    
    # Initialize an empty dictionary to store word counts
    word_counts = {}
    
    # Iterate through each word in the list
    for word in words:
        # Convert word to lowercase to make the counting case-insensitive
        word = word.lower()
        # Increment the count for the word in the dictionary
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    
    # Return the dictionary containing the word counts
    return word_counts

# Example usage
sentence = input("Enter the sentence here: ")
print(word_count(sentence))
