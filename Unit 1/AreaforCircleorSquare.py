"""
Name: Kevin Nhan
Date: September 21th 2023
Description: Prompts the user for a float value and turns it into radius, circumference, and perimeter of square
"""
#Libraries
import math

#Variables and Constants
area = 0

radius = 0
circumference = 0
sideLength = 0
perimeter = 0

PI = math.pi

#Prompts user for area
print("This program will turn a number into the required variables to find the area of a circle and a square")
print()

area = float(input("Please enter a number: "))

#Calculates variables to find area for circle and square
radius = math.sqrt(area / PI)
circumference = 2 * PI * radius

sideLength = math.sqrt(area)
perimeter = sideLength * 4
#Outputs results to user
print("\nIf the area was for a circle then...")
print("The radius would be {0:.2f} and the circumference would be {1:.2f}".format(radius, circumference))

print("\nIf the area for a square then...")
print("The side lengths would be {0:.2f} and the perimeter would be {1:.2f}".format(sideLength, perimeter))
