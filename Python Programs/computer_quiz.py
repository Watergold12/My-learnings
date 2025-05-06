
# Play quiz
print("Welcome to Computer Quiz!!")
print("Instructions: ")
print("1.) There are 10 questions in total. ")
print("2.) For each correct question you will be rewarded 1 point. ")
print("3.) For each incorrect question you will be rewarded -0.2 point. ")
print("4.) At the end your score will be displayed. ")
print("All the Best!! ")

playing = input("Are you playing? ")

# .lower() is to make sure all the entered input to be lowercase
if playing.lower() != "yes":
    quit()

print("Okay, Let's Play :) ")
score = 0

answer = input("1.) What does CPU stand for? ") # 1st question
if answer.lower() == "central processing unit":
    print('Correct!!')
    score += 1 # Increases score by 1
else:
    print('Incorrect!!')
    score -= 0.2 # Decreases score by 0.2

answer = input("2.) What is a capital of Italy? ") # 2nd question
if answer.lower() == "rome":
    print('Correct!!')
    score += 1
else:
    print('Incorrect!!')
    score -= 0.2

answer = input("3.) What is the longest river in the world? ") # 3rd question
if answer.lower() == "nile":
    print('Correct!!')
    score += 1
else:
    print('Incorrect!!')
    score -= 0.2

answer = input("4.) What is the name for the day after thanksgiving? ") # 4th question
if answer.lower() == "black friday":
    print('Correct!!')
    score += 1
else:
    print('Incorrect!!')
    score -= 0.2

answer = input("5.) Which Game of Thrones house does Daenerys belong to? ") # 5th question
if answer.lower() == "targaryen":
    print('Correct!!')
    score += 1
else:
    print('Incorrect!!')
    score -= 0.2

answer = input("6.) Who wrote the book “Chitty-Chitty-Bang-Bang: The Magical Car?” ") # 6th question
if answer.lower() == "ian fleming":
    print('Correct!!')
    score += 1
else:
    print('Incorrect!!')
    score -= 0.2

answer = input("7.) In which part of your body would you find the cruciate ligament? ") # 7th question
if answer.lower() == "knee joint":
    print('Correct!!')
    score += 1
else:
    print('Incorrect!!')
    score -= 0.2

answer = input("8.) What is the name of the main antagonist in the Shakespeare play “Othello”? ") # 8th question
if answer.lower() == "lago":
    print('Correct!!')
    score += 1
else:
    print('Incorrect!!')
    score -= 0.2

answer = input("9.) When was the movie “Titanic” released? ") # 9th question
if answer.lower() == "1997":
    print('Correct!!')
    score += 1
else:
    print('Incorrect!!')
    score -= 0.2

answer = input("10.) What element is denoted by the chemical symbol Sn in the periodic table? ") # 10th question
if answer.lower() == "tin":
    print('Correct!!')
    score += 1
else:
    print('Incorrect!!')
    score -= 0.2

print("Your score :", score) # displays points of the player scored
print("Your percentage is " + str((score / 10) * 100) + "%.") # displays percentage of the score taken