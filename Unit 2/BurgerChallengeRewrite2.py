"""
Name: Kevin Nhan
Date: October 6th 2023
Description: Fast food restaurant - calculates total for food and outputs the total and change
"""

""" MY ALGORITHM
Step 1: Gather the following inputs:
amount of burgers
amount of fries
amount of sodas
Step 2: Calculate sub total, and total with tax
Step 3: Ask the user for the amount tendered
Step 4: Output the sub total, total, and change due
"""

#Constants and Variables
TAX = 1.13

BURGERCOST = 4.5
FRIESCOST = 2.5
SODASCOST = 1.75

amtOfBurgers = 0
amtOfFries = 0
amtOfSodas = 0

burgerPrice = 0
friesPrice = 0
sodaPrice = 0

subTotal = 0
taxTotal = 0
total = 0

amtTendered = 0

change = 0

#Prompting the user for amt of burgers fries and sodas
print("This program will ask the user for the amount of burgers, fries, and sodas and calculate the cost and change the user will receive after tendering amount of cash.\n")

amtOfBurgers = int(input("Please enter the amount of burgers: "))
amtOfFries = int(input("Please enter the amount of fries: "))
amtOfSodas = int(input("Please enter the amount of sodas: "))

print()

#Calculates the total price for all food, drinks, and then totals
burgerPrice = amtOfBurgers * BURGERCOST
friesPrice = amtOfFries * FRIESCOST
sodaPrice = amtOfSodas * SODASCOST

subTotal = burgerPrice + friesPrice + sodaPrice
total = subTotal * TAX
taxTotal = total - subTotal

#Outputs the cost of all the food and drinks
print("{0} Burgers {1:8.2f}".format(amtOfBurgers, burgerPrice))
print("{0} Fries {1:10.2f}".format(amtOfFries, friesPrice))
print("{0} Sodas {1:10.2f}".format(amtOfSodas, sodaPrice))
print()
print("SUB TOTAL {0:8.2f}".format(subTotal))
print("TAX {0:14.2f}".format(taxTotal))
print("TOTAL {0:12.2f}".format(total))
print()

#Prompts the user for amount tendered
amtTendered = float(input("Please enter amount tendered: "))
print()

#Calculates change
change = amtTendered - total

#Outputs receipt to the user
print("{0} Burgers {1:8.2f}".format(amtOfBurgers, burgerPrice))
print("{0} Fries {1:10.2f}".format(amtOfFries, friesPrice))
print("{0} Sodas {1:10.2f}".format(amtOfSodas, sodaPrice))
print()
print("SUB TOTAL {0:8.2f}".format(subTotal))
print("TAX {0:14.2f}".format(taxTotal))
print("TOTAL {0:12.2f}".format(total))
print()
print("TENDERED {0:9.2f}".format(amtTendered))
print("CHANGE {0:11.2f}".format(change))
