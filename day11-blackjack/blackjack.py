#blackjack project

from random import choice

#choice of cards for the game
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#pull the initial cards fo the player and the users
my_card_1 = choice(cards)
my_card_2 = choice(cards)
dealer_card_1 = choice(cards)
dealer_card_2 = choice(cards)

def busted(total, who):
    if total > 21:
        print(f" {who} Busted")
        exit()

def blackjack(total):
    if total ==  21:
        print("Blackjack you have won")
        exit()

#Display the initial cards for the player and face up card for the dealer
print(f"Your cards are {my_card_1} and {my_card_2}")
print(f"The dealer's showing card is {dealer_card_1}")

#ask the player if they want another card
player_total = my_card_1 + my_card_2
blackjack(total=player_total)
my_choice = input("Do you want another card? yes or no: ")

#figure out if the player wants more cards, make sure the player doesn't bust
while my_choice == "yes":
    who = "Player"
    my_card = choice(cards)
    print(f"Your next card is {my_card}")
    player_total += my_card_3
    busted(total=player_total, who=who)
    my_choice = input("Do you want another card? yes or no: ")

#Dealer's turn
print(f"Dealer's second card is {dealer_card_2}")
dealer_total = (int(dealer_card_1) + int(dealer_card_2))
#make sure the dealer hits on 16 or below and monitor for busting
while dealer_total <= 16:
    who = "Dealer"
    dealer_draw = choice(cards)
    dealer_total += dealer_draw
    busted(total=dealer_total, who=who)

if dealer_total > player_total:
    print("The Dealer has won")
elif dealer_total == player_total:
    print("Push")
else:
    print("Good job you beat the Dealer!")

