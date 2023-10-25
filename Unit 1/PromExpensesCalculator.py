"""
Name: Kevin Nhan
Date: September 20th 2023
Description: Calculates minimum amount of tickets required to cover the cost for prom
"""
#Libaries
import math

#Variables and constants
minAmtOfTickets = 0
totalExpenses = 0

food = 0
djCost = 0
hallCost = 0
decorations = 0
staffCost = 0

TICKETCOST = 65
EXPENDITURES = 100

#Prompts the user for the price for each expense
print("This program will calcuate the minimum amount of tickets required to cover the cost for prom\n")

food = float(input("Please enter how much the food costs: "))
djCost = float(input("Please enter how much the DJ costs: "))
hallCost = float(input("Please enter how much the hall costs: "))
decorations = float(input("Please enter how much the decorations costs: "))
staffCost = float(input("Please enter how much the staff costs: "))

#Calculates total expenses and finds the minimum amount of tickets required
totalExpenses = food + djCost + hallCost + decorations + staffCost + EXPENDITURES
minAmtOfTickets = math.ceil(totalExpenses / TICKETCOST)

#Outputs the minimum amount of tickets required to cover the cost of the prom
print("\nThe minimum amount of tickets required to cover the expenses is:",minAmtOfTickets,"Tickets")
