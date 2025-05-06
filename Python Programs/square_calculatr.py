# def square_numbers():
#     squared_list = []

#     user_input = input("Enter the list of numbers to be squared: ")
#     user_entry = [int(i) for i in user_input.split()]

#     for i in user_entry:
#         squared_list.append(i ** 2)
#     return squared_list

# square = square_numbers()
# print(square)


# improvised version of the above one
def square_numbers():
    user_input = input("Enter a list of numbers to be squared, separated by spaces: ")
    numbers = [int(num) for num in user_input.split()]
    
    squared_numbers = [num ** 2 for num in numbers]
    return squared_numbers

squared_list = square_numbers()
print(squared_list)
