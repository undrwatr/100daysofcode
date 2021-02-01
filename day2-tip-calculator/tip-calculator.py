#program to figure out the tip from an amount.
print("Welcome to the Tip Calculator")

#Please enter the amount
total = input("What is the total amount of the bill? $ ")
tip = input("What percentage tip would you like to give? ")
people = input("How many people here at lunch? ")

#Do the math of figuring out the tip based on the percentage entered above
totalwtip = ((float(total) * (float('1.' + str(tip)))) / float(people))

#print the total each person should pay
print("Each person should pay $" + str(round(totalwtip, 2)))



