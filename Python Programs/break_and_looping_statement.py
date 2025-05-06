
while True:
    plant = input("Guess my favorite plant!! ")

    if plant == "Spathiphyllum":
        print("Yes - Spathiphyllum is the best plant ever!")
        break
    elif plant == "spathiphyllum":
        print("No, I want a big Spathiphyllum!")
    else:
        print(f"Spathiphyllum! Not {plant}")