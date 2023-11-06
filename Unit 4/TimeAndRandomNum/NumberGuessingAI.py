"""
Name: Kevin Nhan
Date: November 2 2023
Description: The user picks a random number and the program will guess the number
"""
#Libraries
import random, math

#Variables
numRange = 0
randomNum = 0

amtOfDigits = 0

guess = 0
highGuess = 0
lowGuess = 0

offset =  0
amtOfDigits = 0 

attempts = 0

#Asks user to choose a random number
print("This program will guess the number the user enters.\n")
randomNum = int(input("Please enter a random number: "))
while randomNum < 0 or randomNum > 9999999: #Checks if the user entered something lower than 0 or higher than 9999999
    randomNum = int(input("Please enter a random number: "))

#Sets the number range so the program knows where to start guessing
amtOfDigits = int(math.log10(randomNum)) + 1

numRange = int("1"+("0"*(amtOfDigits)))
offset = numRange / 100

#Loop
guess = random.randint(0, numRange)

while guess != randomNum:
    if guess > randomNum: #If guess is greater than the random number
        highGuess = guess
        guess = random.randint(lowGuess,numRange)
        while guess > highGuess: #Will make sure the guess is lower than the previous guess
            guess = random.randint(lowGuess,numRange)
            numRange -= int(numRange / offset)
            if lowGuess > numRange:
                numRange = lowGuess
            print(guess,lowGuess,numRange)
        attempts += 1 #Only will add an attempt after the loop
    elif guess < randomNum:
        lowGuess = guess
        numRange += int(offset)
        guess = random.randint(lowGuess,numRange)
        attempts += 1


print("Here is your random number:",guess,"Attempts:",attempts)