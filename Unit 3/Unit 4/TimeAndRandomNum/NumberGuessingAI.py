"""
Name: Kevin Nhan
Date: November 2 2023
Description: The user picks a random number and the program will guess the number
"""
#Libraries
import random

#Variables
numRange = 0
randomNum = 0

guess = 0

lowRange = 0
highRange = 0

attempts = 0
guessedNums = []

#Asks user for a range for the bot to start guessing from
randomNum = int(input("Please enter a random number: "))

lowRange = int(input("Please enter the starting guess range: "))
while lowRange > randomNum: #Makes sure that the lowRange is not greater than the random number
    lowRange = int(input("Please enter a starting guess range that is less than the random number: "))
    
highRange = int(input("Please enter the upper guess range: "))
while highRange < randomNum: #Makes sure that the highRange is not lower than the random number
    highRange = int(input("Please enter a upper guess range that is greater than the random number: "))

#Loop
while guess != randomNum:
    attempts += 1
    guess = random.randint(lowRange,highRange)
    while guess > randomNum: #If the guess is greater than the random number, it will set the high range to the guess and find a new random number
        highRange = guess
        guess = random.randint(lowRange,highRange)
    
    if guess < randomNum: #If the guess is lower than the random number, it will set the low range to the guess and find a new random number
        lowRange = guess+1
        guess = random.randint(lowRange,highRange)
    
    guessedNums.append(guess)

#Outputs result
print("\nHere is your random number:", guess,"\nTo guess your number, I took",attempts,"attempt(s)")
print("\nHere are the numbers I guessed:")
print(guessedNums)