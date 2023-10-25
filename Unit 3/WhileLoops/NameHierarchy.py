"""
Name: Kevin Nhan
Date: October 12 2023
Description: A loop that will ask the user for names that will compare it to my name. if the name comes after mine the loop will end.
"""

#Constants and Variables
THESENTINEL = "kevin"

name = ""

#Loop
while THESENTINEL >= name.lower():
    name = input("Please enter a name: ")

print("Nice, your name is after mine.")
