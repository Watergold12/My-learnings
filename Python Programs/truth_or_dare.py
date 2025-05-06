import random

def truth_or_dare():
    choice = input("Choose 'truth' or 'dare': ").lower()

    if choice == 'truth':
        truth_questions = [
            "Have you ever lied to a friend? If so, about what?",
            "What is your biggest fear?",
            "What is your most embarrassing moment?",
            "Have you ever cheated on a test?",
            "What is your guilty pleasure?"
        ]
        question = random.choice(truth_questions)
        print("Your truth question is:", question)
    elif choice == 'dare':
        dare_tasks = [
            "Do 10 push-ups.",
            "Sing a song in front of everyone.",
            "Tell a funny joke.",
            "Act like your favorite animal for one minute.",
            "Send a text message to a random contact saying 'I love pickles!'"
        ]
        task = random.choice(dare_tasks)
        print("Your dare task is:", task)
    else:
        print("Invalid choice! Please choose 'truth' or 'dare'.")

truth_or_dare()
