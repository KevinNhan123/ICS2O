"""
Name: Kevin Nhan
Date: October 18 2023
Description: Asks user to repeatedly enter names until they enter "exit"
"""

#Variables
KEYWORD = "EXIT"

userInput = 0

#Loop
print("This program will Asks user to repeatedly enter names until they enter \"exit\".\n")

userInput = input("Please enter a name: ")
while userInput.upper() != KEYWORD:
    print(userInput)
    userInput = input("Please enter a name: ")

print("Thanks for using this program.")
