# bit size system

def main_menu():
    print("*" * 30)
    print("Library Record System")
    print("*" * 30)
    print("1. Add book")
    print("2. Update book")
    print("3. Search book")
    print("4. Save record")
    print("5. Delete record")
    print("6. Exit")

book_record = {}

def add_book():
    title = input(print("Enter the Book name: "))
    author = input(print("Enter the Author name: "))
    genre = input(print("Enter the Genre: "))
    desc = input(print("Enter the Description: "))
    quant = input(int(print("Enter the Quantity: ")))

    if title in book_record:
        quant = quant + quant
    else:
        pass

def update_book():
    pass

def main():
    add_book()

if __name__ == "__main__":
    main()