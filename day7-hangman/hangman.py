#building the hangman program

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

#random wordlist, choose the word and the length of the word and other variable to be set at the start
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
tries = 5

print("Welcome to Hangman, best of luck in trying to guess the word.")
print(stages[6])

display = []
for _ in range(word_length):
    display += "_"


#check to see if the letter is in the word
while not end_of_game:
    guess = input("Please guess a letter: ").lower()
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            print(display)
    if guess not in chosen_word:
        print(stages[tries])
        if tries == 0:
            end_of_game = True
            print("You Lose!")
        tries = (tries - 1)
    if "_" not in display:
        end_of_game = True
        print("You have won!")



