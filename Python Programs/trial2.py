# Don't mess up with these first 2 ine of codes!!
print("Welcome to the mind guessing game!!")

play = input("Are you ready? ")

# This is the main block, feel free to make changes
if (play == "Yes"): 
  print("Imagine a one digit number in your mind.")
  rep = input("Now multiply it with 2: ")
  if (rep == "Yes"): 
    rep2 = input("Now add 10 to it. ")
    if (rep2 == "Yes"):
      rep3 = input("Now Subtract 3 from it. ")
      if (rep3 == "Yes"):
        rep4 = input("Now multiply the number by 0. ")
        rep5 = input("Now Lemme guess the number. 0 Right? ")
        if rep5 == "Yes":
          print("Yay")
        else: 
          print("Don't you know maths, Idiot")
          print("Signing off buddy.")
else:
  print("Signing off buddy.")
  exit