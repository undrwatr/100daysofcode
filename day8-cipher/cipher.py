#Caeser Cipher program

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#ascii art
import art
print(art.logo)

runprogram = True

def caesar(text, shift, direction):
  cipher = ""
  if direction == "decode":
    for x in text:
      start_index = alphabet.index(x)
      end_index = ((start_index) - (shift))
      if end_index < 0:
        end_index = (end_index + 26)
      cipher += (alphabet[end_index])
    print("Your plain text is:")
  else:
    for x in text:
      start_index = alphabet.index(x)
      end_index = ((start_index) + (shift))
      if end_index >= 26:
        end_index = (end_index - 26)
      cipher += (alphabet[end_index])
    print("Your cipher text is:") 
  print(cipher)



while runprogram == True:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(text, shift, direction)
  goagain = input("Would you like to go again? type yes or no \n ")
  if goagain == "yes":
    runprogram = True
  else:
    runprogram = False




#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 

#TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#Try running the program and entering a shift number of 45.
#Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
#Hint: Think about how you can use the modulus (%).