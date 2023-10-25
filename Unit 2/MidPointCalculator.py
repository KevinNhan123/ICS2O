"""
Name: Kevin Nhan
Date: October 10th 2023
Description: Finds the midpoint of a line segment 
"""

""" MY ALGORITHM
Step 1: Gather the following inputs:
first endpoint (x and y)
second endpoint (x and y)
Step 2: Calculate the averages of x and y
(x1 + x2) / 2 and (y1 + y2) / 2
Step 3: Output the midpoint
"""

#Variables
firstX = 0
firstY = 0

secondX = 0
secondY = 0

midX = 0
midY = 0

#Prompts user for both endpoints
print("This program will determine the midpoint of a line segment given the coordinates of two endpoints.\n")

print("Enter first endpoint.")
firstX = int(input("X: "))
firstY = int(input("Y: "))

print()

print("Enter second endpoint.")
secondX = int(input("X: "))
secondY = int(input("Y: "))

print()

#Calculates the midpoint
midX = (firstX + secondX) / 2
midY = (firstY + secondY) / 2

#Outputs the midpoint to user
print("Midpoint: " +"(" + str(midX) + ", " + str(midY) + ")")
