numb1 = input("Enter the first number: ")
numb2 = input("Enter the second number: ")
numb3 = input("Enter the third number: ")

large_numb = numb1

if numb2 > large_numb:
    large_numb = numb2
else:
    if numb3 > large_numb:
        large_numb = numb3
            
print(f"The largest number among the 3 numbers entered is {large_numb}.")