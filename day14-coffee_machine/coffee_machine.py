
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
currentwater = (resources['water'])
currentmilk = (resources['milk'])
currentcoffee = (resources['milk'])



moneyinmachine = 0
machinerunning = True

def askformoney(choice):
    global moneyinmachine
    print("Please insert coins")
    quarter = int(input("How many quarters? "))
    dime = int(input("How many dimes? "))
    nickel = int(input("How many nickels? "))
    penny = int(input("how many pennies? "))
    totalmoney = ((quarter * .25) + (dime * .10) + (nickel * .05) + (penny))
    cost = (MENU[choice]['cost'])
    if cost < totalmoney:
        refund = (totalmoney - cost)
        print("here is your $" + str(refund) + " change")
        moneyinmachine += cost
    else:
        print("Insufficient funds your money has been returned")

def checkresources(choice):
    global currentmilk
    global currentwater
    global currentcoffee
    water = (MENU[choice]['ingredients']['water'])
    milk = (MENU[choice]['ingredients']['milk'])
    coffee = (MENU[choice]['ingredients']['coffee'])
    if currentwater < water or currentmilk < milk or currentcoffee < coffee:
        print("Not enough resources")
        exit()
    else:
        currentwater -= water
        currentmilk -= milk
        currentcoffee -= coffee

while machinerunning == True:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "latte":
        checkresources(choice)
        askformoney(choice)
        print("Here is your" + (choice) + ". Enjoy!.")
    elif choice == "espresso":
        checkresources(choice)
        askformoney(choice)
        print("Here is your" + (choice) + ". Enjoy!.")
    elif choice == "cappuccino":
        checkresources(choice)
        askformoney(choice)
        print("Here is your" + (choice) + ". Enjoy!.")
    elif choice == "report":
        print("Resources left in the machine")
        print("Water " + str(currentwater))
        print("Milk " + str(currentmilk))
        print("Coffee " + str(currentcoffee))
        print("Money $" + str(moneyinmachine))
        exit()
    elif choice == "off":
        print("The Coffee Machine is turned off now")
        exit()

