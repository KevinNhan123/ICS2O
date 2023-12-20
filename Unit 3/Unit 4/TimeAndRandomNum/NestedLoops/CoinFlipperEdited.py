"""
Name: Kevin Nhan
Date: November 7 2023
Description: Flips a coin 100 times and tells the percentage of heads and tails
"""

#Libraries
import random

#Constants and Variables
HEADS = 1
TAILS = 2

flips = 0
amtOfHeads = 0
amtOfTails = 0

flip = 0

headsPercent = 0
tailsPercent = 0

restart = "Y"

#Loop
while restart.upper() == "Y":
    #Resets all values
    amtOfHeads = 0
    amtOfTails = 0
    headsPercent = 0
    tailsPercent = 0
    
    print("This program will flip your decided amount of coins and will tell you the percentages of heads and tails after.\n")
    input("Hit <ENTER> to continue.")
    
    flips = int(input("Please enter the amount of coins you would like to flip: "))
    while flips < 1 or flips > 10000: #Checks if flips entered is less than 1 or greater than 10000
        flips = int(input("Please enter the amount of coins you would like to flip: "))
    
    for i in range(flips): #Flips a coin for flips amt of time
        flip = random.randint(HEADS,TAILS)
        if flip == HEADS:
            amtOfHeads += 1
        else:
            amtOfTails += 1

    #Calculates the percentages for heads and tails
    headsPercent = amtOfHeads / flips
    tailsPercent = amtOfTails / flips

    #Outputs results
    print("Here are the results after flipping",flips,"coins: ")

    print("Heads percentage: {0:.2%}".format(headsPercent))
    print("Tails percentage: {0:.2%}".format(tailsPercent))
    
    #Asks user if they would like to restart the program
    restart = input("\nWould you like to restart the program? (Y or N): ")

print("Thanks for your time.")