"""
Name: Kevin Nhan
Date: October 25 2023
Description: a program that will find the sum of a number of terms of a infinite series given a term n and value x
"""

#Variables
termN = 0
valueX = 0

sum = 0
#Asks the user for the amt of terms and base value
print("This program will find the sum of a number of terms of a infinite series given a term n and value x.\n")

termN = int(input("Please enter the amount of terms you would like added: "))
valueX = float(input("Please enter the base value for x: "))
print()
#Loop
for power in range(termN):
    sum = sum + valueX**(power)
    
print("The sum is:",sum)