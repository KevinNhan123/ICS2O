"""
Name: Kevin Nhan
Date: November 2 2023
Description: Flips a coin 100 times and tells the percentage of heads and tails
"""

#Libraries
import random

#Constants and Variables
FLIPS = 100
HEADS = 1
TAILS = 2

amtOfHeads = 0
amtOfTails = 0

flip = 0

headsPercent = 0
tailsPercent = 0

#Loop
print("This program will flip "+str(FLIPS)+" coins and will tell you the percentages of heads and tails after.\n")
for i in range(FLIPS):
    flip = random.randint(HEADS,TAILS)
    if flip == HEADS:
        amtOfHeads += 1
    else:
        amtOfTails += 1

#Calculates the percentages for heads and tails
headsPercent = amtOfHeads / FLIPS
tailsPercent = amtOfTails / FLIPS

#Outputs results
print("Here are the results after flipping",FLIPS,"coins: ")

print("Heads percentage: {0:.2%}".format(headsPercent))
print("Tails percentage: {0:.2%}".format(tailsPercent))
