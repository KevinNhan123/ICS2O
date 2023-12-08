"""
Name: Kevin Nhan
Date: December 8th 2023
Description: repeats a string a number of times given by a numeric parameter
"""

#Context of program
print("This program will repeat a string the user enters a given amount of times from a numeric parameter.\n")

#Functions
def getInt(message):
    """This function will ask the user for an integer, with error proofing"""
    num = input(message)
    while not num.isnumeric():
        print("You did not enter an integer!")
        num = input("Please enter a number: ")
    num = int(num)
    return num

def repeat(amt, message):
    """This function prints a message a given amount of times"""
    for i in range(amt):
        print(message)

#Variables
amt = 0
message = 0

#Asks user for message and amt of times to be repeated
message = input("Please enter a message: ")
amt = getInt("Please enter the amount of times you would like to repeat this message: ")

#Outputs results
print()
repeat(amt, message)