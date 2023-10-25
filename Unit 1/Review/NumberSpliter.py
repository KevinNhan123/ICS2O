"""
Name: Kevin Nhan
Date: September 26th 2023
Description: Number spliter
"""

#Variables

number = 0

hundredsPlace = 0
tensPlace = 0
onesPlace = 0

#Prompts the user for a three digit number
print("This program will take any three digit number and split up the digits.\n")
number = int(input("Please enter a three digit number: "))

#Calculates and splits each digit
hundredsPlace = number // 100
tensPlace = number // 10 % 10
onesPlace = number % 10

#Outputs result to user
print("The hundreds-place digit is:", hundredsPlace)
print("The tens-place digit is:", tensPlace)
print("The ones-place digit is:", onesPlace)
