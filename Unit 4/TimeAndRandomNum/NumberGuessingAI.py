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

#Main variables for the bot
highestGuess = 0

guess = 0
highGuess = 0
lowGuess = 0

offset =  0

allNums = []
#Asks user to choose a random number
print("This program will guess the number the user enters.\n")
randomNum = int(input("Please enter a random number: "))
while randomNum < 0 or randomNum > 99999999: #Checks if the user entered something lower than 0 or higher than 99999999
    randomNum = int(input("Please enter a random number: "))

#Sets the number range so the program knows where to start guessing
amtOfDigits = int(math.log10(randomNum)) + 1

numRange = int("1"+("0"*(amtOfDigits)))
offset = numRange / 10

#Loop
guess = random.randint(1, numRange)
highGuess = guess
while guess != randomNum:
    #Adds the guess to a list and sorts the numbers
    allNums.append(guess) 
    allNums.sort(reverse=True)

    if guess > randomNum: #If guess is greater than the random number
        highGuess = guess

        if highestGuess < highGuess:
            highestGuess = highGuess
            
        guess = random.randint(lowGuess,highestGuess)
        while highestGuess > randomNum:
            print("Highest",highestGuess)
            guess = random.randint(lowGuess,highGuess)
            highestGuess = guess
            
        print(guess)
        print("Too high:",guess,lowGuess,highGuess,highestGuess)
        
    elif guess < randomNum: #If guess was lower than random number
        lowGuess = guess
 
        guess = random.randint(lowGuess,guess)
        print(guess)
        for i in range(len(allNums)): #Checks list of all numbers already choosen by the bot and makes sure that it doesnt pick the same num again
            while guess <= allNums[i] or guess <= highestGuess:
                guess = random.randint(lowGuess, allNums[i]+offset)
                
        print("Too Low:",lowGuess,guess,highGuess)

#Outputs result
print("\nHere is your random number:",guess,"Attempts:",len(allNums))
print("Here is the list of numbers the AI guessed:\n")
print(allNums)