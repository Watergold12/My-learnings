print("May I ask your name?")
name = input()

if name == "":
    print("Oh, I see! You must be a secret agent on a top-secret mission. Don’t worry, your secret is safe with me, Agent Anonymous! ")
else:
    print(f"Hello {name}")

color = input("What's your favorite color? ")

if color.lower() == "red":
    print("As red as a rose!!")
elif color.lower() == "orange":
    print("As orange as a pumpkin!!")
elif color.lower() == "yellow":
    print("As yellow as the sun!!")
elif color.lower() == "green":
    print("As green as grass!!")
elif color.lower() == "blue":
    print("As blue as the ocean!!")
elif color.lower() == "purple":
    print("As purple as a plum!!")
elif color.lower() == "pink":
    print("As pink as a flamingo!!")
elif color.lower() == "brown":
    print("As brown as chocolate!!")
elif color.lower() == "black":
    print("As black as coal!!")
elif color.lower() == "white":
    print("As white as snow!!")
elif color.lower() == "gray":
    print("As gray as a stormy sky!!")
elif color.lower() == "gold":
    print("As gold as a crown!!")
else:
    print("That's a unique color!")

number = input("May I ask your favorite number! ")
print(f"Your favorite number is {number}. That's a cool number!")

if int(number)%2 == 0:
    print("Your favorite number is even.")
else:
    print("Your favorite number is odd.")