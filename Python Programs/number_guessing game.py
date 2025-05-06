import random

number = random.randrange(1, 100)

print("*" * 30)
print("Welcome to the game!!".center(30))
print("*" * 30)

print("Guess the number correct and you win!!")

while True:
  numb2 = int(input("Let's start with your guess: "))

  if numb2 == number:
    print("Yay!! you guessed it correct!!")
    break  # Exit the loop if the guess is correct
  elif numb2 > number:
    print("You are ahead of the number!!")
  elif numb2 < number:
    print("You are behind of the number!!")