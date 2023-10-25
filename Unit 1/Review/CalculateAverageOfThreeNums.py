"""
Name: Kevin Nhan
Date: September 25th 2023
Description: Calculates average of three numbers
"""

#Variables
num1 = 0
num2 = 0
num3 = 0

average = 0

#Prompts user for 3 numbers
print("This program will calculate the average of three numbers.")
print()

num1 = float(input("Please give the first number: "))
num2 = float(input("Please give the second number: "))
num3 = float(input("Please give the last number: "))
print()

#Calculates the average and rounds it
average = round((num1 + num2 + num3) / 3, 2)

#Outputs average to user
print("The average of your three numbers is:", average)
