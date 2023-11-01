"""
Name: Kevin Nhan
Date: November 1 2023
Description: Checks if the number entered is less than 20 or greater than 50
"""

#Constants and Variables
MINIMUM = 20
MAXIMUM = 50

numEntered = 0

#Asks user to enter a number
print("This program checks if a number entered is less than 20 or greater than 50.\n")
numEntered = float(input("Please enter a number: "))

#Checks the number
if numEntered >= MAXIMUM or numEntered <= MINIMUM:
    print("Error")
else:
    print("Nice")