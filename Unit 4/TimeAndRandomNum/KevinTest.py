"""
Name: Kevin Nhan
Date: November 6 2023
Description: A simple dice game where the goal is to obtain a sum of 4 or less when rolling two 6-sided dice
"""

#Libraries
import random

#Variables
plrOneName = 0
plrTwoName = 0

#The amt of rolls each player will have after attempting to roll a 4 or less
plrOneRolls = 0
plrTwoRolls = 0

#The values for the rolls
rollOne = 0
rollTwo = 0

sum = 5 #Sets the sum to something higher than 4 so the loop will start 

turn = 1 # 1 = plr one || 2 = plr two

#Asks players for their names
print("This program is a simple dice game, where the goal is to roll 2 6-sided dice and have the sum of 4 or less.\n")

plrOneName = input("Player one, please enter your name: ")
plrTwoName = input("Player two, please enter your name: ")

#Loop
while turn <= 2: #This will continue looping until plr two finds a sum of 4 or less
    if turn == 1: #If it's plr one's turn
        input("\nAre you ready "+plrOneName+"?"+" Press <ENTER> to continue.")
        plrOneRolls += 1
    else: #If it's plr two's turn
        input("\nAre you ready "+plrTwoName+"?"+" Press <ENTER> to continue.")
        plrTwoRolls += 1

    #Rolls two random numbers
    rollOne = random.randint(0,6)
    rollTwo = random.randint(0,6)
    
    #Adds both rolls together
    sum = rollOne + rollTwo
    
    #Outputs result
    if sum <= 4: #If plr one receives a sum of 4 or less, it will be plr two's turn. If plr two receives a sum of 4 or less, the loop will end
        print("Nice one! Your sum of the two rolls is",sum,"It is now "+plrTwoName+"'s turn!")
        turn += 1
    else:
        print("You rolled the numbers",rollOne,"and",rollTwo,"! The sum of those two rolls is",sum)

#Outputs the results and the winner of the game
print("\n{0:10} {1}".format("Player","# Of Rolls"))
print("{0:7} {1:4}".format(plrOneName,plrOneRolls))
print("{0:7} {1:4}".format(plrTwoName,plrTwoRolls))
print()

#Figures out who had the most rolls and determines the winner with the least amount of rolls
if plrOneRolls > plrTwoRolls:
    print(plrTwoName,"wins!")
elif plrOneRolls < plrTwoRolls:
    print(plrOneName,"wins!")
else:
    print("It was a tie between both players!")