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

cloneOfRandomNum = 0
amtOfDigits = 0

guess = 0
offset =  0
amtOfDigits = 0 

attempts = 0

#Asks user to choose a random number
print("This program will guess the number the user enters.\n")
randomNum = int(input("Please enter a random number: "))
while randomNum < 0 or randomNum > 9999999: #Checks if the user entered something lower than 0 or higher than 9999999
    randomNum = int(input("Please enter a random number: "))

cloneOfRandomNum = randomNum
while cloneOfRandomNum > 0:
    cloneOfRandomNum = cloneOfRandomNum // 10
    amtOfDigits += 1

numRange = int("1"+("0"*(amtOfDigits)))
offset = numRange / 100

guess = random.randint(0, numRange)
    
while guess != randomNum:
    if guess < randomNum:
        guess = random.randint(guess,numRange)
        print("Too Low:",guess,offset,numRange)
        attempts += 1
    elif guess > randomNum:
        guess = random.randint(math.floor(guess - (guess / offset)),numRange)
        attempts += 1
        print("Too High:",guess)
    elif guess == randomNum:
        print("Your random number was:",guess)
        attempts += 1

         
print("Attempts:",attempts)