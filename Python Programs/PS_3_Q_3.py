user_input = input("Enter a string: ")

count = user_input.count("  ")

print("Double spaces found:", count)


# Bonus
positions = [i for i in range(len(user_input) - 1) if user_input[i:i+2] == "  "]
print("Found double spaces at positions:", positions)
