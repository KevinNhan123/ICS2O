"""
Name: Kevin Nhan
Date: October 16th 2023
Description: Password guessing game but with only 10 tries
"""

#Constants and Variables
PASSWORD = "KEVIN123"

totalTriesAllowed = 0
amtOfTries = 1 #Offset by 1 so that if user guesses first try, it wont output it as guessing it in zero tries

guess = 0

counter = 0
#Loop
print("Guess my password! You only have 10 tries...\n")

totalTriesAllowed = 11
guess = input("Enter your guess: ")

while amtOfTries < totalTriesAllowed and guess.upper() != PASSWORD:
    amtOfTries = amtOfTries + 1
    guess = input("\nEnter your guess: ")

#If the user ran out of tries and guessed it incorrectly
counter = 0
while guess.upper() != PASSWORD and counter == 0:
    print("You are out of tries! Your guess:",guess,"is not correct!")
    counter = counter + 1

#If the user guessed it correctly within the allowed amount of tries
counter = 0
while guess.upper() == PASSWORD and counter == 0:
    print("\nCongrats!! Your guess,", guess, "is correct!! You guessed my password in this many tries:",amtOfTries,"!")
    counter = counter + 1

#NOTE: if statements would be better instead of these two loops
