"""
Name: Kevin Nhan
Date: September 14th 2023
Description: Converts pennies into smaller change
"""

#Variables
amountOfPennies = int(input("Enter your amount of pennies: "))

quarter = 25
dime = 10
nickel = 5
penny = 1

#Calculates the change with the given amount of pennies
amountOfQuarters = amountOfPennies // quarter
amountOfDimes = amountOfPennies % quarter // dime
amountOfNickels = amountOfPennies % quarter % dime // nickel
remainingPennies = amountOfPennies % quarter % dime % nickel // penny

#Outputs the change
print("Here is your change:")
print(" Quarters:", amountOfQuarters,'\n', "Dimes:", amountOfDimes,'\n', "Nickels:", amountOfNickels,'\n', "Pennies:", remainingPennies)
