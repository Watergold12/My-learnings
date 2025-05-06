def even_number_lister():
    only_even_numbers = []

    user_input = input("Enter the list of numbers: ")
    get_numbers = [int(numb) for numb in user_input.split()]

    for numb in get_numbers:
        if numb % 2 == 0:
            only_even_numbers.append(numb)
    return only_even_numbers
    
even_number = even_number_lister()

print(even_number)