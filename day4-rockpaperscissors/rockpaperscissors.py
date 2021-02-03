#play rock paper scissors against the computer

import random

choices = ["paper", "rock", "scissors"]

computer_choice = random.choice(choices)

print("Welcome to the Rock Paper Scissors duel")

human_choice = input("Please choose your weapon: rock, paper, or scissors \n")

# ascii art for the computer choice
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#print the users choice
print("You chose " + human_choice)
if human_choice == "rock":
    print(rock)
elif human_choice == "paper":
    print(paper)
else:
    print(scissors)

#print the computers choice
print("The Computer chose " + str(computer_choice))
if computer_choice == "rock":
    print(rock)
elif computer_choice == "paper":
    print(paper)
else:
    print(scissors)

#The different options and the logic to go through them
if computer_choice == human_choice:
    print("it's a tie")
elif computer_choice == "rock" and human_choice == "scissors":
    print("The computer won")
elif computer_choice == "paper" and human_choice == "scissors":
    print("You won")
elif computer_choice == "scissors" and human_choice == "paper":
    print("The computer won")
elif computer_choice == "scissors" and human_choice == "rock":
    print("You won")
elif computer_choice == "rock" and human_choice == "paper":
    print("You won")
elif computer_choice == "paper" and human_choice == "rock":
    print("The Computer won")




