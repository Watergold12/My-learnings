# Initialize an empty list
number_list = []

# Function to add numbers to the list
def add_number(number):
    number_list.append(number)
    print(f"Number {number} added to the list.")

# Main program
while True:
    print("\n1. Add Number\n2. View List\n3. Exit")
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        try:
            number = float(input("Enter a number to add: "))  # Using float for flexibility (integer or float input)
            add_number(number)
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    elif choice == '2':
        if not number_list:
            print("The list is empty.")
        else:
            print("Number List:")
            for num in number_list:
                print(num)
    elif choice == '3':
        print("Exiting the program...")
        break
    else:
        print("Invalid choice! Please choose 1, 2, or 3.")
