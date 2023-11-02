"""
Name: Kevin Nhan
Date: November 2 2023
Description: A menu that asks the user for type of die and outputs the value to them
"""
#Libraries
import random

#Variables
userPrompt = 0
randNum = 0

#All the dice
diceValues = [4, 6, 8, 10, 12, 20]

#Asks the user for a dice
print("This program will prompt you a menu to choose between a variety of dice.")
while userPrompt != 7:
    print("\nPlease choose an option by inputting the corresponding number.")
    for i in range(len(diceValues)): #Prints all dice values in the list to the user
        print(str(i+1)+": "+str(diceValues[i])+" Sided Die")

    userPrompt = int(input("\nChoose an option (ENTER 7 to EXIT): "))
    while userPrompt < 1 or userPrompt > 7: #Checks if value entered is less than 1 or greater than 7
        userPrompt = int(input("\nChoose an option (ENTER 7 to EXIT): "))

#Checks the dice they choose or if they exited
    if userPrompt == 7:
        break
    else:
        randNum = diceValues[userPrompt-1] #Finds the dice value in list
        randNum = random.randint(1,randNum) #Generates a random num with the chosen value
        print("Your chosen dice rolled a",randNum,"!")
        input("Press <ENTER> to continue.")
    
print("\nThank you for using this program.")