"""
Name: Kevin Nhan
Date: October 4th 2023
Description: This program will calculate the total cost of a car with an admin fee, $500 fee, and tax fee
"""

#Constants and Variables
ADMINFEE = 0.08
WARRANTY = 500
TAX = 0.13

carCost = 0
extraCosts = 0

subTotal = 0

adminFeeTotal = 0
taxTotal = 0

finalTotal = 0

#Prompting the user for car cost and any extra costs
print("This program will calculate the total cost of a car with an admin fee, $500 fee, and tax fee.\n")

carCost = float(input("Please enter the cost of the car: $"))
extraCosts = float(input("Please enter any extra cost: $"))
print()

#Calculates the total price for the car along with the fees
subTotal = carCost + extraCosts
adminFeeTotal = subTotal * ADMINFEE
taxTotal = subTotal * TAX

finalTotal = subTotal + subTotal * TAX + subTotal * ADMINFEE + WARRANTY

#Outputs results to the user
print("Here are the costs for your car:\n")

print("The sub total cost of your car is: ${0:.2f}".format(subTotal))
print("Warranty: $" + str(WARRANTY))
print("Admin Fee: ${0:.2f}".format(adminFeeTotal))
print("Tax applied: ${0:.2f}".format(taxTotal))
print()
print("The final cost of your car will be: ${0:.2f}".format(finalTotal))
