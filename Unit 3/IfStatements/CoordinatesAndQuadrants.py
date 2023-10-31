"""
Name: Kevin Nhan
Date: October 30 2023
Description: asks the user to input an (x,y) coordinate and tells them which quadrant it's in
"""

#Variables
xCoord = 0
yCoord = 0

#Asks the user for x and y
print("This program will take any given x and y value and tells which quadrant the coordinates are in.\n")

xCoord = float(input("Please enter the x coordinate: "))
yCoord = float(input("Please enter the y coordinate: "))

#Checks which quadrant the coords are in
if xCoord == 0 and yCoord == 0:
    print("The coordinates ({0}, {1}) is the origin point.".format(xCoord, yCoord))
elif xCoord == 0:
    print("The coordinates is on the x axis.")
elif yCoord == 0:
    print("The coordinates is on the y axis")
elif xCoord >= 0 and yCoord >= 0:
    print("The coordinates ({0}, {1}) are in the first quadrant.".format(xCoord, yCoord))
elif xCoord <= 0 and yCoord >= 0:
    print("The coordinates ({0}, {1}) are in the second quadrant.".format(xCoord, yCoord))
elif xCoord <= 0 and yCoord <= 0:
    print("The coordinates ({0}, {1}) are in the third quadrant.".format(xCoord, yCoord))
elif xCoord >= 0 and yCoord <= 0:
    print("The coordinates ({0}, {1}) are in the fourth quadrant.".format(xCoord, yCoord))
