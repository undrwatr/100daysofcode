#Silent Auction program

#imports
from replit import clear
from art import logo
bidding = True


#print the pretty logo
print(logo)

#initialize dictionary
totalbids = []
bids = {}

print("Welcome to the Silent Auction")
while bidding == True:
    name = input("Please tell me your name: ")
    bids[name] = int(input("what is your bid? "))
    keepgoing = input("Would you like to continue taking bids? ")
    if keepgoing == "yes":
        bidding = True
        clear()
    else:
        bidding = False

highest_bid = 0
winner = ""

for bidder in bids:
    print(bids[bidder])
    print(bidder)
    bid_amount = bids[bidder]   
    if bid_amount > highest_bid:
        highest_bid = bid_amount
        winner = bidder

print(f"The winner is {winner} with a bid of ${highest_bid}")