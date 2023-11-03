"""
Name: Kevin Nhan
Date: November 2 2023
Description: A bot will guess a phone number
"""

#Libraries
import random

#Variables
phoneNumber = 0

attempts = 0
guess = 0

#Loop
print("This program will guess any 7 digit number you enter.\n")

phoneNumber = int(input("Please enter a 7 digit number: "))
while phoneNumber > 9999999 or phoneNumber <1000000: #Checks if user entered something lower or higher than 7 digits
    phoneNumber = int(input("Actually enter a 7 digit number: "))

while guess != phoneNumber: #This loop will not end until the program guesses the number
    guess = random.randint(1000000,9999999)
    if guess != phoneNumber:
        attempts += 1

#Outputs result
        
print("\nThe phone number was",guess,"It took this many attempts to guess:",attempts)
