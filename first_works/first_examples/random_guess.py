# write a program that prompt a user to guss a random number and if the user gets it correct print; correctly and
# if the user gets it wrong print wrong and iterate for 5 times then break.


import random


def mainMenu():
    number = random.randint(0, 100)
    guess_times = 0
    while guess_times < 5:
        user_guess = int(input("Guess a number between 0 and 100: "))
        if user_guess > 100:
            print("Out of range...")
            break
        elif user_guess == number:
            print("correctly guessed, wel-done, the secret number is: ", number)
            break
        elif user_guess < number:
            print("Too low")
        elif user_guess > number:
            print("Too high dude")
        guess_times += 1

    else:
        print("You failed, time out")
        print("The correct number is: ", number)


mainMenu()
print("""


            press 1 to play ------


            press 2 to cancel ----


""")
user_input = print(int(input(mainMenu())))
print(int(input(mainMenu())))
