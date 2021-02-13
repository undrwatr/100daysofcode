# keep track of the number of right answers
# if user is right go again
# if user is wrong end game and present final score

import art
import random
from game_data import data

#opening artwork
print(art.logo)

#make total number of items an option in the data so that we could use variable amounts of data in the program and for the random#
total_questions = (len(data) - 1)
keepgoing = True
numberright = 0

#function to pull the choices
def getchoices():
    global numberright
    choicea = random.randint(0, total_questions)
    choiceb = random.randint(0, total_questions)
    print("Compare A: " + data[choicea]['name'] + " a " + data[choicea]['description'] + " from " + data[choicea]['country'])
    choiceafollower = data[choicea]['follower_count']
    #vs logo for game
    print(art.vs)
    print("Compare B: " + data[choiceb]['name'] + " a " + data[choiceb]['description'] + " from " + data[choiceb]['country'])
    choicebfollower = data[choiceb]['follower_count']
    selection = input("Who has more followers, A or B? ")
    if choicebfollower > choiceafollower and selection == "B":
        numberright += 1
    elif choiceafollower > choicebfollower and selection == "A":
        numberright += 1
    else:
        print(f"Thanks for playing, you got {numberright} correct")
        exit()

while keepgoing == True:    
    getchoices()
