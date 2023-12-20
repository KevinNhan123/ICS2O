"""
Name: Kevin Nhan
Date: November 15 2023
Description: Stores 5 names inputted by user and outputs names in reverse order
"""

#Variables
names = []

name = 0

#Gives user context
print("This program will ask the user for 5 names. After, it will output all names in reverse order.\n")

#Loop
for i in range(5):
    #Asks user for name
    name = input("Please enter a name: ")
    
    #Adds name to list
    names.append(name)

#Reverses the list
names.reverse()

#Outputs result
print("\nHere are all your names in reverse order.")
print(names)