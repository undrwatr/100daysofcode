#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
#Randomized letters

#create the list to hold the values
keying_material = []
#create the list with all of the data in it
for x in range(nr_letters):
    keying_material.append(random.choice(letters))
for x in range(nr_symbols):
    keying_material.append(random.choice(symbols))
for x in range(nr_numbers):
    keying_material.append(random.choice(numbers))

#shuffle the list that I just created
random.shuffle(keying_material)

#initialize a string varaible and then populate it with the information
generated_password = ""
for ele in keying_material:
    generated_password += ele

#print out the password
print("Your password is: " + "\n" + generated_password)