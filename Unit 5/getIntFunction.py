"""
Name: Kevin Nhan
Date: December 7th 2023
Description: Get int function with 2 parameters
"""

#Context of program
print("This program will ask the user for an integer within a range.\n")

#Functions
def getIntRange(min,max):
    """
        Asks user for integer, but the user is only allowed to input 
        a value from min to max
    """
    
    num = input("\nPlease enter a number: ")
    
    while not(num.isnumeric()): #If the value entered is not a number
        print("You did not enter an integer!")
        num = input("Please enter a number: ")
        
    num = int(num) #Converts number to integer

    while num < min or num > max: #If the number is not in the range
        print("Your number is not in the range!")
        num = input("Please enter a number: ")
        if num.isnumeric() == True:
            num = int(num)
        while not(num.isnumeric()):
            print("You did not enter an integer!")
            num = input("Please enter a number: ")
        num = int(num)
    #If number passes through all validity loops
    return num

#Variables
num = 0

minRange = 0
maxRange = 0

#Asks user for a range
minRange = input("Please enter a minimum range: ")
while (not minRange.isnumeric()):
    print("You did not enter a number!")
    minRange = input("Please enter a minimum range: ")
minRange = int(minRange)

maxRange = input("Please enter a maximum range: ")
while (not maxRange.isnumeric()):
    print("You did not enter a number!")
    maxRange = input("Please enter a maximum range: ")
maxRange = int(maxRange)

if maxRange <= minRange: #Overrides max range if minimum range is greater than max range
    maxRange = minRange + 1

#Calls function
num = getIntRange(minRange,maxRange)

#Outputs results
print("\nHere is your number:",num)