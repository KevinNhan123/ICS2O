"""
Name: Kevin Nhan
Date: October 25 2023
Description: Gold Coins question
"""

#Libraries
import math

#Constants and Variables
INITIALCOINS = 20
MULTIPLIER = 1.5
STOLENAMT = 3
AMTOFDAYS = 365

newAmtOfCoins = 0

#Loop
print("This program will calculate the amount of gold coins you will have after a year of replicating and having them stolen.\n")

newAmtOfCoins = INITIALCOINS #Setting newAmtOfCoins to initial amt so the loop doesn't start with it as 0
for day in range(AMTOFDAYS):
    newAmtOfCoins = newAmtOfCoins * MULTIPLIER - STOLENAMT #Multiplies amount of coins by 1.5 (adding half to the new value) and then subtracts the stolen amount
    #Outputs the day and the total amount of coins 
    print("Day " + str(day+1),"||","Gold Coins:",math.floor(newAmtOfCoins))
