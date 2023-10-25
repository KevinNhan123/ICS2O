"""
Name: Kevin Nhan
Date: September 26th 2023
Description: Burger Challenge rewrite
"""
#Libraries
from datetime import datetime

#Variables and Constants
currentDate = datetime.now().strftime("%Y-%m-%d %H:%M")

amtOfBurgers = 0
amtOfFries = 0
amtOfSodas = 0

burgerPrice = 0
friesPrice = 0
sodaPrice = 0

subTotal = 0
total = 0
taxTotal = 0

amtTendered = 0
change = 0

BURGERCOST = 4.29
FRIESCOST = 2.29
SODACOST = 1.89

TAX = 1.13

#Prompts the user for amount of burgers, fries, and sodas
print("This program will prompt the employee for the number of burgers, fries, and sodas and then displays the total, tax, final cost in receipt form.\n")

amtOfBurgers = int(input("Enter the number of burgers: "))
amtOfFries = int(input("Enter the number of fries: "))
amtOfSodas = int(input("Enter the number of sodas: "))
print()

#Calculates the cost of all items
burgerPrice = amtOfBurgers * BURGERCOST
friesPrice = amtOfFries * FRIESCOST
sodaPrice = amtOfSodas * SODACOST

subTotal = burgerPrice + friesPrice + sodaPrice
total = subTotal * TAX
taxTotal = total - subTotal

#Outputs the cost for the user
print("Subtotal: ${0:.2f}".format(subTotal))
print("Tax:\t  ${0:.2f}".format(taxTotal))
print("Total:\t  ${0:.2f}".format(total))

#Asks user for amount tendered
amtTendered = float(input("Enter amount tendered: "))

#Calculates the change
change = amtTendered - total

#Outputs the receipt
burgerPrice = "${0:.2f}".format(burgerPrice)
friesPrice = "${0:.2f}".format(friesPrice)
sodaPrice = "${0:.2f}".format(sodaPrice)

subTotal = "${0:.2f}".format(subTotal)
taxTotal = "${0:.2f}".format(taxTotal)

total = "${0:.2f}".format(total)
amtTendered = "${0:.2f}".format(amtTendered)
change = "${0:.2f}".format(change)

print("\nORD# 727\t" + currentDate)
print("------------------------------------\n")
print("QTY ITEM\t\tTOTAL")
print("{0:>2} Burgers:{1:>18}".format(amtOfBurgers,burgerPrice))
print("{0:>2} Fries:{1:>20}".format(amtOfFries,friesPrice))
print("{0:>2} Sodas:{1:>20}".format(amtOfSodas,sodaPrice))
print()
print("SUBTOTAL:{0:>20}".format(subTotal))
print("TAX:{0:>25}".format(taxTotal))
print()
print("TOTAL:{0:>23}".format(total))
print()
print("CASH TENDERED:{0:>15}".format(amtTendered))
print("CHANGE:{0:>22}".format(change))
print()
print("Apply at wwww.gcviburgers.ca")
print()
print("------------------------------------")
