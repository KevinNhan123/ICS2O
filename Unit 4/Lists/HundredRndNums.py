"""
Name: Kevin Nhan
Date: November 15 2023
Description: Creates a list with 100 random nums, user will enter a number and program will tell if that number was in list or not
"""

#Library
import random

#Variables
numbers = []
generatedNum = 0

number = 0
foundNum = False

#Gives user context of program
print("This program will generate 100 random numbers.")
print("The user will enter a random number")
print("and the program will tell the user if the number is in the list or not.\n")

#Generates 100 random numbers
for i in range(100):
    generatedNum = random.randint(0,100)
    numbers.append(generatedNum)

#Asks user for a number
number = int(input("Please enter a number: "))

#Checks list for user number
for num in range(len(numbers)-1):
    if numbers[num] == number:
        foundNum = True
        print("Number was found at index:",num)

#If there was no number found
if foundNum == False:
    print("\nYour number was not found in the list.")