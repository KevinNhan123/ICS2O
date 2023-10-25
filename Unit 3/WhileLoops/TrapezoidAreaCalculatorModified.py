"""
Name: Kevin Nhan
Date: October 13th 2023
Description: Modiftying a previous program so that a program will loop if the user says yes
"""

#Variables
lengthA = 0
lengthB = 0
height = 0

area = 0

response = "Y"

#Loop

while response == "Y":
    #Asks the user for the three inputs required for the area
    print("This program will calculate the area of a trapezoid using the given three dimesions from the user.\n")
    
    lengthA = float(input("Please enter length A: "))
    lengthB = float(input("Please enter length B: "))
    height = float(input("Please enter the height: "))
    
    print()

    #Calculate the area
    area = ((lengthA + lengthB) * height) / 2

    #Outputs result to user
    print("The area of the trapezoid using the given three dimensions is:", area)
    print()
    response = input("Would you like to run the program again? (Y/N): ").upper()
    print()

print("Thank you for using this program.")
