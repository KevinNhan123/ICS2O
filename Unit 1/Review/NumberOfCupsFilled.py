"""
Name: Kevin Nhan
Date: September 25th 2023
Description: Takes 3 integers that represent height, radius of cylinder, and volume
"""

#Variables and Constants
height = 0
radius = 0
volume = 0

volumeOfCup = 0
numOfCups = 0

PI = 3.1415926
#Prompts the user for 3 integers
print("This program will take 3 integers from the user which will be the size of a cup and the volume of water in a pitcher.\n")

height = int(input("Enter the height in cm: "))
radius = int(input("Enter the radius in cm: "))
volume = int(input("Enter the volume of water for the pitcher: "))
print()

#Calculates the size of the cup and amount of cups that will be filled from pitcher
volumeOfCup = (PI * radius**2) * height
numOfCups = round(volume / volumeOfCup,2)

#Outputs result to user
print("The number of cups that will be filled by the pitcher is around:",numOfCups, "Cups.")
