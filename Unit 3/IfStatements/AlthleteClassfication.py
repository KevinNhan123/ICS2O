"""
Name: Kevin Nhan
Date: October 26 2023
Description: Classifies althletes into three weight categories
"""

#Constants and Variables
HEAVY = 80
MEDIUM = 60
LIGHT = 0

weight = 0

#Loop
print("This program will ask the user for the weight of three althletes, then it will classify them in different weight categories.\n")

for althlete in range(3): #Will loop 3 times for three althletes
    weight = float(input("Please enter the weight of your althlete: "))

    #Checks the weight entered and classifies the althlete
    if weight >= HEAVY:
        print("\nYour althlete would be classified as heavy weight.")
    elif weight >= MEDIUM:
        print("\nYour althlete would be classified as medium weight.")
    elif weight >= LIGHT:
        print("\nYour althlete would be classified as light weight.")
    else:
        print("\nInvalid weight.")
