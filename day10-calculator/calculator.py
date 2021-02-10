#calculator program
from art import logo

print(logo)
goagain = True


def calculator(number1, operation, number2):
    if operation == "+":
        result = number1 + number2
    elif operation == "-":
        result = number1 - number2
    elif operation == "*":
        result = number1 * number2
    else:
        result = number1 / number2
    print("Your result is:")
    print(result)

while goagain == True:
    number1 = int(input("What's the first number:"))
    operation = input("Pick an operation \n+\n-\n*\n/\n")
    number2 = int(input("What's the second number:"))
    calculator(number1, operation, number2)
    doitagain = input("Would you like to do something else? ")
    if doitagain == "yes":
        goagain = True
    else:
        goagain = False
        print("Thanks for using the calculator")