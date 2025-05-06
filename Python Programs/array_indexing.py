import numpy as np

user_input = input("Enter the array of numbers: ")
get_numbers = [int(numb) for numb in user_input.split()]

my_array = np.array(get_numbers)

ele = int(input("Enter the number to be inserted: "))
pos = int(input("Enter the position to be inserted: "))

my_array = np.insert(my_array, pos, ele)

# demo testing area

print(my_array)