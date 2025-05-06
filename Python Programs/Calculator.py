# Calculator
def calculator():
    print("*" * 50)
    print("Welcome to the calculator".center(50))
    print("*" * 50)
    print("")
    print("Operations performed: Addition, Subtraction, Multiplication or Division")
    print("")
    op = input("Please select the operation you want to perform (add, sub, multi, div): ")

    if op.lower() == "addition" or op.lower() == "add":
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        print(f"The sum of the two numbers is: {num1 + num2}.")
    elif op.lower() == "subtraction" or op.lower() == "sub":
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        print(f"The difference of the two numbers is: {num1 - num2}.")
    elif op.lower() == "multiplication" or op.lower() == "multi":
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        print(f"The product of the two numbers is: {num1 * num2}.")
    elif op.lower() == "division" or op.lower() == "div":
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        print(f"The quotient of the two numbers is: {num1 / num2}.")
    elif op.lower() == "exit":
        print("Invalid operation. Please try again.")
        exit()

# demo testing
calculator()