"""
Name: Kevin Nhan
Date: November 15 2023
Description: This program will output 1 of 5 random fortunes to the user
"""

#Libraries
import random

#Variables
fortunes = ["Keep your nose on the grindstone.","Look left and right.","Do not be afraid of competition.","Forget injuries; never forget kindnesses.","In the cookie of life, friends are the chocolate chips."]

chosenFortune = 0
restart = "Y"

#Context for user
print("This program will display one of five unique fortunes to the user.\n")

#Loop
chosenFortune = fortunes[random.randint(0,len(fortunes)-1)]
while restart == "Y":
    input("Press <ENTER> to continue.")
    
    print("\nYour fortune is:",chosenFortune)
    restart = input("Would you like to read your fortune again? (Y/N): ").upper()
    print()
    
#End of program
print("Program complete.")