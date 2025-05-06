lst = [int(x) for x in input("Enter list elements: ").split()]
if lst == sorted(lst):
    print("Ascending")
else:
    print("Not Ascending")