"""
Name: Kevin Nhan
Date: September 25th 2023
Description: A bank machine that outputs the users current balance
"""

#Variables and Constants
withdrawn = 0
deposited = 0

newBalance = 0

BALANCE = 400

#Prompts the user for amount for withdraw and deposit
print("This program will act as a bank machine that outputs the users current balance.\n")
withdrawn = float(input("How much do you want to withdraw?: $"))
deposited = float(input("How much do you want to deposit?: $"))
print()

#Calculates for new balance
newBalance = BALANCE - withdrawn + deposited

#Outputs new balance to user
print("New balanace: $" + str(newBalance))
