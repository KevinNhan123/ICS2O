"""
Name: Kevin Nhan
Date: October 12 2023
Description: Using while loops to ask the user for infinite radiuses for an area of a circle
"""

#Constants and Variables
PI = 3.1415926

radius = 0
area = 0

#Loop
print("This program will use while loops to ask the user for infinite radiuses for an area of a circle")

while radius >= 0:
    radius = float(input("Please enter a radius: "))
    area = PI * (radius**2)
    print("The area of the circle is: {0:.2f}".format(area))

print("The radius is negative...")
