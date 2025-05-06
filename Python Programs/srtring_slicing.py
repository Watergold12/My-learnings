def ask():
    st = input("Enter the string to be sliced: ") 

    a = int(input(f"Enter start point of slicing (0 to {len(st)}):"))
    b = int(input(f"Enter end point of slicing (2 to {len(st)}):"))

    if b < 2:
        print("The slicing end point must start from at-least 2!!")
        return st, None, None
    
    return st, a, b

def show(st, a, b):
    print(st[a:b])

st, a, b = ask()
show(st, a, b)