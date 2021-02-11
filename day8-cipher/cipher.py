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

