# def reverse_strings():

#     user_input = input("Enter a list of words to be reversed: ")
#     strings = [s for s in user_input.split()]

#     # Reverse the strings in the list
#     reversed_list = [s[::-1] for s in strings]
#     return reversed_list

# st = reverse_strings()
# print(st)


# def reverse_strings():
#     # Prompt the user to enter a list of words to be reversed
#     user_input = input("Enter a list of words to be reversed, separated by spaces: ")
    
#     # Split the input into individual words
#     strings = [s for s in user_input.split()]
    
#     # Reverse each string and store in a new list
#     reversed_list = [s[::-1] for s in strings]
    
#     # Return the list of reversed strings
#     return reversed_list

# # Call the function and print the result
# st = reverse_strings()
# print(st)


# improvised version of the above two
def reverse_strings(strings):
    # Create a new list to store reversed strings
    reversed_strings = [string[::-1] for string in strings]
    
    # Return the list of reversed strings
    return reversed_strings

# Prompt the user to enter a list of strings separated by spaces
user_input = input("Enter a list of strings separated by spaces: ")
string_list = user_input.split()

# Print the list of reversed strings
print(reverse_strings(string_list))  # Output will depend on user input
