print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#left or right
choice1 = input("You come to a fork in the road, you can go left or right. Type "'left'" or "'right'":\n")
if choice1 == "right":
    print("You hit a wall and have died")
    exit()
else:
    choice2 = input("You have made it to a stream, will you swim across or wait? Type "'swim'" or "'wait'":\n")

if choice2 == "swim":
    print("You can't swim and have drowned")
    exit()
else:
    choice3 = input("You have come to three doors, red, yellow, and blue. Choose one. Type "'red'", "'yellow'", or "'blue'": \n")

if choice3 == "red":
    print("You have burned up in a fire")
    exit()
elif choice3 == "yellow":
    print("You were teleported to the sun, so sad")
    exit()
else:
    print("Congratulations you have won!!!!!")