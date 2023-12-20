"""
Name: Kevin Nhan
Date: November 10 2023
Description: 

Asks for first name, last name and OEN Number and 
outputs a windows login
Ex. John Doe 342034054 -> jodoe4054
"""

#Variables
firstName = 0
lastName = 0
oenNum = 0

windowsLogin = 0

#Asks user for first and last name and OEN
print("This program will create a login for you.\n")

firstName = input("Please enter your first name: ")
while (not firstName.isalpha()): #Checks if name entered is a number / anything else
    firstName = input("Please enter your first name: ")

lastName = input("Please enter your last name: ")
while (not lastName.isalpha()):
    lastName = input("Please enter your last name: ")

oenNum = input("Please enter your OEN Number: ")
while (not oenNum.isnumeric()): #Checks if the oen entered is not a number
    oenNum = input("Please enter your OEN Number (make sure there are no spaces, letters, etc): ")

#Grabs the determined amount of letters and numbers from the name and oen
firstName = firstName[:2]
lastName = lastName[:3]
oenNum = oenNum[5:]

#Outputs created login
print("Welcome, "+(firstName+lastName+oenNum).lower()+"@ugcloud.ca")