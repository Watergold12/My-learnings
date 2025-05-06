# the life calculator

# Make a function for the speaker asking his or her birthyear and the zodiac
def speaker():
    print("*" * 40)
    print("Welcome to the Life Calculator".center(40))
    print("*" * 40)
    birth_year = input("Please enter your birthyear in the format of yyyy: ")
    zodiac = input("Please enter your zodiac sign: ")
    your_current_life = input("How are you feeling in the recent times? Happy or Sad or Disappointed or Excited: ")
    return birth_year, zodiac, your_current_life

# Next, Write down some steps to degrade as much as you can even though that person is happy
def calculating_area(birth_year, zodiac, your_current_life):
    if birth_year == 2006 and zodiac == "Aries" and your_current_life == "Happy":
        print("You are going to have a major fall in the future! Don't worry child you will regret worrying about the fall since you are already dead")
    elif birth_year == 2006 and zodiac == "Aries" and your_current_life == "Sad":
        print("Your life is saved for now")

# Next continue the previous steps for a couple of time and tell everything was a joke

# That's how this calculator should work

# Demo testing
speaker()
calculating_area()

# Creator: the_great_vesper aka Vishal