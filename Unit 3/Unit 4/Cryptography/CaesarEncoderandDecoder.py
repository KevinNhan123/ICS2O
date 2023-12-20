"""
Name: Kevin Nhan
Date: December 4th 2023
Description: This program will encode or decode messages using a caesar cipher
"""

# Context of program
print("This program will encode or decode messages using a Caesar Cipher.")
print("It will prompt you for a choice between encoding a message or decoding one with a key.")
print("Have fun.\n")

# Constants and Variables
ENCODE = "E"
DECODE = "D"

prompt = 0 # Decides whether the user wishes to encode or decode a message
message = 0
key = 0

newMessage = 0

# Functions
def encodedMessage(message, key):
    newMessage = ""
    location = 0
    
    for letter in message:
        location = chr(ord(letter) + key)
        if ord(location) > 122: # The max decimal place is 122 (z)
            location = chr(ord(location) - 26)
        elif ord(location) < 97: # The minimum decimal place is 97 (a)
            location = chr(ord(location) + 26)
            
        newMessage = newMessage + location
    return newMessage

def decodedMessage(message, key):
    newMessage = ""
    location = 0
    
    for letter in message:
        location = chr(ord(letter) - key)
        if ord(location) > 122: # The max decimal place is 122 (z)
            location = chr(ord(location) - 26)
        elif ord(location) < 97: # The minimum decimal place is 97 (a)
            location = chr(ord(location) + 26)
            
        newMessage = newMessage + location
    return newMessage

# Asks user whether they would like to decode and encode a message
prompt = input("Do you want to encode or decode a message (E/D): ").upper()
while prompt != ENCODE and prompt != DECODE:
    print("Please enter E or D.")
    prompt = input("Do you want to encode or decode a message (E/D): ").upper()
    
# Asks user for the message
message = input("Please enter a message: ")

# Asks user for the key
key = input("Please enter the key (the shift): ")
while (not key.isnumeric()):
    print("You did not enter a number.")
    key = input("Please enter the key (the shift): ")
key = int(key)

# Encodes or decodes the message
if prompt == ENCODE:
    newMessage = encodedMessage(message, key)
elif prompt == DECODE:
    newMessage = decodedMessage(message, key)

print("\nThe new message is:", newMessage)