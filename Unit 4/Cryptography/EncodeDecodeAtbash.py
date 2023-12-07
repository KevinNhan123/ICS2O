"""
Name: Kevin Nhan
Date: December 5th 2023
Description: Encodes or decodes atbash ciphers
"""

#Context of program
print("This program will encode or decode any atbash cipher.")
print("Tell the program if you are going to encode or decode and then enter a message.\n")

#Variables
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
reverseAlphabet = alphabet.copy()
reverseAlphabet.reverse()

message = 0
prompt = 0

newMessage = ""

#Asks user for prompt
prompt = input("Would you like to encode or decode a message? (E/D): ").upper()
while prompt != "E" and prompt != "D":
    prompt = input("Would you like to encode or decode a message? (E/D): ").upper()

message = input("\nPlease enter a message: ").lower()
while (not message.isalpha()):
    print("You did not enter a message (make sure there are no numbers or spaces)")
    message = input("Please enter a message: ").lower()

#Encodes or decodes the message
if prompt == "E":
    for letter in message:
        newMessage = newMessage + reverseAlphabet[alphabet.index(letter)]

if prompt == "D":
    for letter in message:
        newMessage = newMessage + alphabet[reverseAlphabet.index(letter)]

#Outputs results
print("\nYour message is:",newMessage)