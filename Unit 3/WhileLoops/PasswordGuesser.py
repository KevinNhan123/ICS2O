"""
Name: Kevin Nhan
Date: October 12 2023
Description: Password Guesser
"""

#Varibles
password = 1234567890

guess = 0

#Loop
print("This program will ask the user to the guess the password.")

while guess != password:
    guess = int(input("\nPlease guess the password (hint: it is a number only password!): "))

print("\nCongratulations!! You guessed the password!")
