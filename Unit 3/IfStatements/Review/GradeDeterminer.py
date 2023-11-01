"""
Name: Kevin Nhan
Date: November 1 2023
Description: Displays great job when grade is 90 or higher
"""

#Constants and Variables
MINIMUMGRADE = 90

gradeEntered = 0
message = "Great job!"

#Asks user for grade
print("This program will determine if a grade entered by the user is good or not.\n")
gradeEntered = float(input("Please enter a grade: "))
print()

#Checks if grade is higher than the MINIMUMGRADE
if gradeEntered >= MINIMUMGRADE:
    print(message)