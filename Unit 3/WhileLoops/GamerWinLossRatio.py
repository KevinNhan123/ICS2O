"""
Name: Kevin Nhan
Date: October 20 2023
Description: Gamer Win to loss ratio
"""

#Variables
rounds = 0

totalWins = 0
totalLosses = 0

wins = 1
losses = 1

winsLossRatio = wins / losses

#Loop
print("This program will keep track of a gamers win to loss ratio.")

while losses != 0 and winsLossRatio > 0.1:
    wins = int(input("\nPlease enter the amount of wins: "))
    losses = int(input("Please eneter the amount of lossses: "))

    totalWins = totalWins + wins
    totalLosses = totalLosses = totalLosses + losses

    rounds = rounds + 1

    print("Round", rounds,":","Wins:",wins,"Losses:",losses)
    input("\nPress <ENTER> to continue: ")

print("\nHere is your total ratio for all the rounds: Total Wins:",totalWins,"Total Losses:",totalLosses)
