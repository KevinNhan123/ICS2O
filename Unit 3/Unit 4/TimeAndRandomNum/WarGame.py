"""
Name: Kevin Nhan
Date: November 2 2023
Description: The card game War
"""

#Libraries
import random

#Constants and Variables
ROUNDS = 26

rollOne = 0
rollTwo = 0

plrOneWins = 0
plrTwoWins = 0

#Loop
print("In this program you have to roll a die. The die has to be greater than the other person's roll. Have fun.\n")
for roundNum in range(ROUNDS):
    print("Round:",roundNum+1,"|| Players, are you ready?")
    input("Press <ENTER> to continue") #Acts as a cooldown for the loop

    #Generates random rolls for both players
    rollOne = random.randint(1,6)
    rollTwo = random.randint(1,6)

    print("\nPlayer one rolls a",rollOne,"!")
    print("Player two rolls a",rollTwo,"!\n")

    if rollOne > rollTwo: #If plr one has a higher roll
        print("Player one wins!")
        plrOneWins += 1
    elif rollOne == rollTwo: #If both rolls were the same
        print("It was a tie!")
        plrOneWins += 1
        plrTwoWins += 1
    elif rollOne < rollTwo: #If plr one rolled less than plr two
        print("Player two wins!")
        plrTwoWins += 1

if plrOneWins > plrTwoWins: #If plr one has more wins at the end
    print("\nPlayer one wins it all with",plrOneWins,"To",plrTwoWins,"!")
elif plrOneWins == plrTwoWins: #If both players have the same amount of wins
    print("\nBoth players have the same amount of wins! It is a tie!")
elif plrOneWins < plrTwoWins: #If plr two has more wins at the end 
    print("\nPlayer two wins it all with",plrTwoWins,"To",plrOneWins,"!")
