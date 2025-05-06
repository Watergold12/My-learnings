# Grocery billing system

# Function to display the main menu
def display_main_menu():
    print("*" * 30)
    print("Main Menu:".center(30))
    print("*" * 30)
    print("1. Display Items List")
    print("2. Add item to cart")
    print("3. Remove item from cart")
    print("4. Display cart")
    print("5. Calculate total cost")
    print("6. Bill?")
    print("7. Save cart")
    print("8. Read the saved cart")
    print("9. Delete cart")
    print("10. Exit")

# Create a list
list_items = {
    "apple": 10,
    "orange": 8,
    "banana": 2,
    "kiwi": 15,
    "pineapple": 8,
    "grapes": 10,
    "pomegranate": 10,
    "dates": 25,
    "custard apple": 12,
}

# Function to display the items
def display_items_list(list_items):
    print("List of items: ")
    for item, cost in list_items.items():
        print(f"{item}: {cost}".upper())
    

# Function to add items into cart
def add_items_to_cart(cart, list_items):
    add_item = input("Enter the Fruit Name: ")
    if add_item.lower() in list_items:
        quantity = int(input(f"Enter the quantity of {add_item.upper()}: "))
        cart[add_item] = cart.get(add_item, 0) + quantity
        print(f"{quantity} {add_item.upper()}(s) added to cart.")
    else:
        print(f"{add_item.upper()} not available in the list.")

# Function to remove items from cart
def remove_items_from_cart(cart):
    item_remove = input("Enter Item name to be removed: ")
    if item_remove.lower() in cart:
        quantity = int(input(f"Enter quantity of {item_remove.upper()} to be removed: "))
        if cart[item_remove] >= quantity:
            cart[item_remove] -= quantity
            print(f"{quantity} {item_remove.upper()}(s) removed from cart.")
        else:
            print(f"Not enough {item_remove.upper()} in cart.")
    else:
        print(f"{item_remove.upper()} is not available in your cart.")

# Function to display cart
def display_cart(cart):
    print("Your cart: ")
    for item, quantity in cart.items():
        print(f"{item}: {quantity}".upper())

# Function to calculate the total cost
def calc_total_cost(cart, list_items):
    total_cost = 0
    for item, quantity in cart.items():
        total_cost += list_items[item] * quantity
    return total_cost

# Function to display Bill
def display_bill(cart, list_items):
    print("*" * 30)
    print("Your Bill".center(30))
    print("*" * 30)

    total_cost = 0
    for item, quantity in cart.items():
        cost = list_items[item] * quantity
        total_cost += cost
        print(f"{item}: {quantity} x ₹{list_items[item]} = ₹{cost:.2f}")

    print(f"Total Cost: ₹{total_cost:.2f}")
    print("*" * 30)

# Function to save the cart
def save_cart_to_file(cart):
    with open('cart.txt', 'w') as file:
        for item, quantity in cart.items():
            file.write(f"{item}: {quantity}\n")
    print("Cart data saved to 'cart.txt'.")

# Function to read saved cart
def read_saved_cart():
    try:
        with open('cart.txt', 'r') as file:
            for line in file:
                item, quantity = line.strip().split(': ')
                print(f"{item}: {quantity}")
    except FileNotFoundError:
        print("No saved cart data found.")

def delete_saved_cart():
    pass

# Writing a main Function
def main():
    cart = {}
    while True:
        display_main_menu()
        choice = input("Enter your choice (1-7): ")
        if choice == "1":
            display_items_list(list_items)
        elif choice == "2":
            add_items_to_cart(cart, list_items)
        elif choice == "3":
            remove_items_from_cart(cart)
        elif choice == "4":
            display_cart(cart)
        elif choice == "5":
            total_cost = calc_total_cost(cart, list_items)
            print(f"Total cost: ₹{total_cost:.2f}")
        elif choice == "6":
            display_bill(cart, list_items)
        elif choice == "7":
            save_cart_to_file(cart)
        elif choice == "8":
            read_saved_cart()
        elif choice == "9":
            pass
        elif choice == "10":
            print("Thank you for shopping with us!!")
            print("Have a nice day!!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()


# Demo testing area