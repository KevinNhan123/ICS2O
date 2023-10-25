"""
Name: Kevin Nhan
Date: October 6th 2023
Description: Calculates area of trapezoid using the given three dimensions
"""

""" MY ALGORITHM
Step 1: Ask users for these inputs:
lengthA
lengthB
height
Step 2: Calculate the area using the formula:
area = (a+b)h / 2
Step 3: Output the area to the user
"""

#Varaibles
lengthA = 0
lengthB = 0
height = 0

area = 0

#Asks the user for the three inputs required for the area
print("This program will calculate the area of a trapezoid using the given three dimesions from the user.\n")

lengthA = float(input("Please enter length A: "))
lengthB = float(input("Please enter length B: "))
height = float(input("Please enter the height: "))

print()

#Calculates the area
area = ((lengthA + lengthB) * height) / 2

#Outputs result to user
print("The area of the trapezoid using the given three dimensions is:", area)
