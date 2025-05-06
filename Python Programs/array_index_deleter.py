import numpy as np

user_input = input("Enter the array of numbers: ")
get_numbers = [int(numb) for numb in user_input.split()]

my_array = np.array(get_numbers)

pos = int(input("Enter the position of element to be deleted: "))

my_array = np.delete(my_array, pos)

# demo testing area

print(my_array)