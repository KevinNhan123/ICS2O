"""
Name: Kevin Nhan
Date: September 14th 2023
Description: Creates a receipt
"""

#Libaraies
from datetime import datetime

#Variables and constants
currentDate = datetime.now().strftime("%Y-%m-%d %H:%M")

amountOfBurgers = 0
amountOfFries = 0
amountOfSodas = 0
amountTendered = 0

subTotal = 0
taxTotal = 0
total = 0
change = 0

TAX = 1.13
PRICEOFBURGER = 4.29
PRICEOFFRIES = 2.29
PRICEOFSODA = 1.89

#Prompts the user for inputs
amountOfBurgers = int(input("Enter the number of burgers: "))
amountOfFries = int(input("Enter the number of fries: "))
amountOfSodas = int(input("Enter the number of sodas: "))

#Calculates subtotal price and final price after tax
burgerPrice = amountOfBurgers * PRICEOFBURGER
friesPrice = amountOfFries * PRICEOFFRIES
sodaPrice = amountOfSodas * PRICEOFSODA

subTotal = burgerPrice + friesPrice + sodaPrice
total = subTotal * TAX
taxTotal = total - subTotal

#Outputs price to user
print("\nSubtotal: ${0:.2f}".format(subTotal))
print("Tax:\t  ${0:.2f}".format(taxTotal))
print("Total:\t  ${0:.2f}".format(total))

#Asks user for amount tendered
amountTendered = float(input("\nEnter amount tendered: "))

#Calculates change
change = amountTendered - total

#Outputs receipt to user
burgerPrice = "${0:.2f}".format(burgerPrice)
friesPrice = "${0:.2f}".format(friesPrice)
sodaPrice = "${0:.2f}".format(sodaPrice)

subTotal = "${0:.2f}".format(subTotal)
taxTotal = "${0:.2f}".format(taxTotal)

total = "${0:.2f}".format(total)
amountTendered = "${0:.2f}".format(amountTendered)
change = "${0:.2f}".format(change)

print("\nORD# 72\t\t" + currentDate)
print("------------------------------------\n")
print("QTY ITEM\t\tTOTAL")
print("{0:>2} Burgers:{1:>18}".format(amountOfBurgers,burgerPrice))
print("{0:>2} Fries:{1:>20}".format(amountOfFries,friesPrice))
print("{0:>2} Sodas:{1:>20}".format(amountOfSodas,sodaPrice))
print()
print("SUBTOTAL:{0:>20}".format(subTotal))
print("TAX:{0:>25}".format(taxTotal))
print()
print("TOTAL:{0:>23}".format(total))
print()
print("CASH TENDERED:{0:>15}".format(amountTendered))
print("CHANGE:{0:>22}".format(change))
print()
print("Apply at wwww.gcviburgers.ca")
print()
print("------------------------------------")
