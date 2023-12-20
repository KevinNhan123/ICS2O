"""
Name: Kevin Nhan
Date: November 9 2023
Description: Guesses any random number with the binary search algorithm
"""

#Variables
mid = 0

randomNum = 0
upperRange = 0

guess = 0
attempts = 0

guessedNums = []

#Asks user for random number
print("This program will ask the user for a number, the program will try to guess that number.\n")

randomNum = int(input("Please enter a random number: "))

#Loop
while guess != randomNum:
    while guess < randomNum:
        mid = (guess + randomNum) // 2
        if mid < randomNum: #If the average // 2 is less than randomNum
            guess = mid + 1
        elif mid > randomNum: #If the average // 2 is still greater than randomNum
            guess = mid - 1
        guessedNums.append(guess) #Adds guess to list
        
#Outputs result
print("\nI guessed your number in",len(guessedNums),"attempt(s). The number is",guess)
print("Here is the list of numbers I guessed:")
print(guessedNums)