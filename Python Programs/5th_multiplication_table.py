def multi_table():
    i = 1
    x = int(input("Enter the number to generate the multiplication table: "))
    while i <= 10:
        print(f"{x} * {i} =", x * i )  # I have used f-string to minimize typing
        i = i + 1

multi_table()