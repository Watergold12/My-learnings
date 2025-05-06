user_input = input("Enter the list of numbers: ") # Gets the list entered by the user
get_numbers = [int(numb) for numb in user_input.split()] # takes the separate numbers and adds them into the get_numbers from the list

ele = int(input("Enter the number to find it's frequency: ")) # the number whose frequency will be found

freq = 0

for i in get_numbers:  # for every i in get numbers
    if i == ele:       # it loops through and finds the equal ele
        freq += 1      # and then adds 1 to the freq of ele

print(f"Frequency of {ele} is {freq}.")