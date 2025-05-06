"""def number_count(sequence):
    # Split the sequence into numbers
    numbs = sequence.split()
    
    # Initialize an empty dictionary to store number counts
    numb_counts = {}
    
    # Iterate through each number in the list
    for numb in numbs:
        # Giving a new variable for reference
        numbs = numb
        # Increment the count for the number in the dictionary
        if numbs in numb_counts:
            numb_counts[numbs] += 1
        else:
            numb_counts[numbs] = 1
    
    # Return the dictionary containing the number counts
    return numb_counts

sequence = input("Enter the sentence here: ")
print(number_count(sequence))
"""

# Better version of the above problem
def number_count(sequence):
    # Convert the sequence to a list of integers
    numbs = list(map(int, sequence.split()))
    
    # Initialize an empty dictionary to store number counts
    numb_counts = {}
    
    # Iterate through each number in the list
    for numb in numbs:
        # Increment the count for the number in the dictionary
        if numb in numb_counts:
            numb_counts[numb] += 1
        else:
            numb_counts[numb] = 1
    
    # Return the dictionary containing the number counts
    return numb_counts

# Taking input from the user
sequence = input("Enter a sequence of numbers separated by spaces: ")
print(number_count(sequence))
