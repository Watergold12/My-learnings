"""Write a Python program that takes a list of words and returns a new list containing only the words that are longer than a specified length.

Here's the structure you can follow:

Define a function filter_long_words that takes a list of words and a length threshold as arguments.
Use a loop to iterate through the list and check the length of each word.
If a word is longer than the specified length, add it to a new list.
Return the new list."""


# def longer_word_detector():
#     longer_words = []

#     user_input = input("Enter a list of words: ")
#     length = int(input("Enter the length iof words to be sorted: "))
#     users_words = [word for word in user_input.split()]

#     for word in users_words:
#         if len(word) > length:
#             longer_words.append(word)
#     return longer_words

# perfect = longer_word_detector()
# print(perfect)


# improvised version of the above one
def longer_word_detector():
    longer_words = []

    user_input = input("Enter a list of words separated by spaces: ")
    length_threshold = int(input("Enter the minimum length of words to include: "))
    users_words = [word for word in user_input.split()]

    for word in users_words:
        if len(word) > length_threshold:
            longer_words.append(word)
    return longer_words

perfect = longer_word_detector()
print(perfect)  # This will print the list of words longer than the specified length
