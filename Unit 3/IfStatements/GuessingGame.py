"""
Name: Kevin Nhan
Date: October 27 2023
Description: Guess Game
"""
#Constants and Variables
RANDOMNUM = 79
ALLOWEDGUESSES = 10

userGuess = 0

#Loop
print("This program will ask the user to guess the random number in 10 tries.\n")

for tries in range(ALLOWEDGUESSES):
    userGuess = int(input("Please enter a number between 0 to 100: "))
    while userGuess < 0 or userGuess > 100: #Checks if the input from the user is from 0 to 100
         userGuess = int(input("\nPlease enter a number between 0 to 100: "))
    
    #Checks the value of the guess and compares it to the random number
    if userGuess > RANDOMNUM:
        print("\nYour guess was too high!")
    elif userGuess < RANDOMNUM:
        print("\nYour guess was too low!")
    elif userGuess == RANDOMNUM:
        print("\nYou guess was correct! Here is the amount of tries it took:",tries + 1)
        break #Ends the loop

if userGuess != RANDOMNUM: #If the user did not guess it in 10 tries
    print("\nYou did not guess the random number in 10 tries!")