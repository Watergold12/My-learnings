# Draw a Tree!!

#      *
#     ***
#    *****
#   *******
#  ********* 9
#      *

# height = 5
# 5 * 2 - 1 = 9


n = int(input("Enter the height of the tree in numbers: "))

def tree(height):
    # your code goes here
    length = height * 2 - 1
    stars = 1
    for i in range(1, height + 1):
        print(("*" * stars).center(length))
        stars += 2
    if n >= 9:
        print("*".center(length))
        print("*".center(length))
        print("*".center(length))
    else:
        if n >= 5:
            print("*".center(length))
            print("*".center(length))
        else: 
            print("*".center(length))

tree(n)