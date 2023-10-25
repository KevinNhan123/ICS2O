"""
Name: Kevin Nhan
Date: October 6th 2023
Description: This program will calculate the amount of tickets required to break even for expenses
"""

""" MY ALGORITHM
Step 1: Ask the user for the expenses for the following:
snacks
DJ
decorations
Step 2: Calculate the total and calculate the amount of tickets to sell to break even
Step 3: Output the amount of tickets to break even
"""

#Libraries
import math

#Constants and Variables
TICKETCOST = 10

snacks = 0
dj = 0
decorations = 0

total = 0
minAmtOfTickets = 0
#Asks the user for the expenses for snacks, dj and decorations
print("This program will calculate the amount of tickets required to break even for expenses.\n")

snacks = int(input("Enter the cost for snacks: $"))
dj = int(input("Enter the cost for the DJ: $"))
decorations = int(input("Enter the cost for the decorations: $"))

print()
#Calculates the total cost for the expenses and the amount of tickets to break even
total = snacks + dj + decorations

minAmtOfTickets = math.ceil(total / TICKETCOST)

#Outputs result
print("The amount of tickets to break even is:", minAmtOfTickets, "Tickets")
