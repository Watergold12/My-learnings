import random

elements = ["rock", "paper", "scissor"]

# create a function for looking into which side won
def option(player_choice, computer_choice):
    player_choice = player_choice.lower()  # Convert to lowercase

    if player_choice == computer_choice:
        print("Draw, Better luck next time!!")

    elif player_choice == "rock"and computer_choice == "paper":
        print("Player lost!!")
        print("Computer Won!!")

    elif player_choice == "paper" and computer_choice == "scissor":
        print("Player lost!!")
        print("Computer Won!!")

    elif player_choice == "scissor" and computer_choice == "stone":
        print("Player lost!!")
        print("Computer Won!!")
    
    elif player_choice == "rock" and computer_choice == "scissor":
        print("Player Won!!")
        print("Computer lost!!")

    elif player_choice == "paper" and computer_choice == "stone":
        print("Player Won!!")
        print("Computer lost!!")

    elif player_choice == "scissor" and computer_choice == "paper":
        print("Player Won!!")
        print("Computer lost!!")

    else:
        print("Invalid input! Please choose 'Rock', 'Paper', or 'Scissor': ")

player_choice = input("Enter your choice (Rock/Paper/Scissor): ")
computer_choice = random.choice(elements)
option(player_choice, computer_choice)