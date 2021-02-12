#Number Guessing Game Objectives:

from art import logo
from random import randrange
answer = False
guess = randrange(1, 100)

print(logo)

#figure out the # of guesses a user will get
difficulty = input("Would you like to play easy or hard? ")
if difficulty == "hard":
    guesses = 5
else:
    guesses = 10

player_guess = int(input("Please guess a number from 1 to 100: "))

#fucntion to look at the guessing from the user
def guessing(player_guess, guess, guesses):
    print(guesses)
    if player_guess < guess:
        print("higher")
    elif player_guess > guess:
        print("lower")
    else:
        print("good job you guessed it")
        answer = True
        print(f"The computer chose {guess}")
        exit()

#run through and count the number of tries and then log the user out if they fail
while answer == False:
    guesses = guesses -1
    if guesses == 0:
        print("Your are out of guesses")
        exit()
    guessing(player_guess=player_guess, guess=guess, guesses=guesses)
    player_guess = int(input("Please guess a number from 1 to 100: "))
