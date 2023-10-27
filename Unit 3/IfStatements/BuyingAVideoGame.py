"""
Name: Kevin Nhan
Date: October 26 2023
Description: Buying a video game
"""

#Constants and Variables
HST = 1.14
DISCOUNT = 0.3

videoGamePrice = 0
amtToBuy = 0

cost = 0
finalCost = 0

discountAmt = 20

#Asks the user for the video game cost and the amount they want to buy
print("This program will ask the user for a video game to buy.\n")

videoGamePrice = float(input("How much does your video game cost?: $"))
amtToBuy = int(input("How many would you like to buy?: "))

#Calculates the total cost
cost = videoGamePrice * amtToBuy

#Checks if the amt bought is greater than discountAmt
if amtToBuy > discountAmt:
    cost = cost - (cost * DISCOUNT)

#Adds HST
finalCost = cost * HST

#Outputs
print("\nHere is the final cost of all your video games: ${0:.2f}".format(finalCost))
