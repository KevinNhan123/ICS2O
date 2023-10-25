"""
Name: Kevin Nhan
Date: October 2nd 2023
Description: Helps the user with spending patterns
"""

#Variables
food = 0
clothing = 0
entertainment = 0
rent = 0

totalSpent = 0

foodPercent = 0
clothingPercent = 0
entertainmentPercent = 0
rentPercent = 0

#Prompts the user for food, clothing, enterainment, and rent
print("This program will help the user examine their spending patterns within the previous month. Enter the amount spent last month on the following items:\n")

food = float(input("Food: $"))
clothing = float(input("Clothing: $"))
entertainment = float(input("Entertainment: $"))
rent = float(input("Rent: $"))

#Calculates the percentage for the expenditures
totalSpent = food + clothing + entertainment + rent

foodPercent = (food / totalSpent) * 100
clothingPercent = (clothing / totalSpent) * 100
entertainmentPercent = (entertainment / totalSpent) * 100
rentPercent = (rent / totalSpent) * 100

print()

#Outputs and displays a table to the user
print("{0:16}{1}".format("Category", "Budget"))
print("Food {0:16.2f} %".format(foodPercent))
print("Clothing {0:12.2f} %".format(clothingPercent))
print("Entertainment {0:7.2f} %".format(entertainmentPercent))
print("Rent {0:16.2f} %".format(rentPercent))
