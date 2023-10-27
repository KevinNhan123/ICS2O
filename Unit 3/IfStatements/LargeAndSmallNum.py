"""
Name: Kevin Nhan
Date: October 27 2023
Description: Finds the largest and smallest num
"""

#Variables
numEntered = 0

largeNum = 0
smallNum = 0

amtOfNums = 0

#Preparation for the loop
print("This program will ask the user for numbers and the final output will print the largest and smallest number.\n")

amtOfNums = int(input("Please enter the amount of numbers you would like to enter: "))
while amtOfNums <= 0: #Checks to make sure the number entered is not less than 0
    amtOfNums = int(input("Please enter the amount of numbers you would like to enter: "))

#Changes these variables before the loop
numEntered = float(input("Please enter a number: "))
largeNum = numEntered
smallNum = numEntered

#Loop
for i in range(amtOfNums):
    numEntered = float(input("Please enter a number: "))
    if numEntered > largeNum:
        largeNum = numEntered
    elif numEntered < smallNum:
        smallNum = numEntered

#Outputs result to user
print("Your largest number was:", largeNum)
print("Your smallest number was:", smallNum)