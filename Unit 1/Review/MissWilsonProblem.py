"""
Name: Kevin Nhan
Date: September 26th 2023
Description: Calculates paint cost and surface area 
"""
#Libraries
import math

#Variables and Constants
length = 0
width = 0
height = 0

surfaceArea = 0

amtOfPaint = 0

newPaintCost = 0

PAINTCOST = 29.99 #per gallon
COVEREDSPACE = 300 #ft (300 square feet in a gallon)

#Prompts the user for length, width, and height in ft
print("This program will calculate the surface area of a room and the cost of paint.\n")

length = float(input("Please enter the length in ft: "))
width = float(input("Please enter the width in ft: "))
height = float(input("Please enter the height in ft: "))
print()

#Calculate the surface area and paint cost
surfaceArea = 2 * (height*length + height*width) #ignoring the ceiling and floor

amtOfPaint = math.ceil(surfaceArea / COVEREDSPACE)
newPaintCost = PAINTCOST * amtOfPaint

#Outputs result to user
print("The surface area of the room is:",surfaceArea,"FT.")
print("The amount of paint required will be:",amtOfPaint,"One gallon Buckets.")
print("The cost of the paint will be: $"+ str(newPaintCost))
