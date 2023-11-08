"""
Name: Kevin Nhan
Date: November 8 2023
Description: Roll a dice three times and you win if it is greater or equal to the target number
"""

#Libraries
import random, time

#Variables
rollSum = 0

wins = 0
losses = 0

#Loop
print("This program will generate a random number and the user will have to roll until the sum of their rolls is higher than the generated number.")

for rounds in range(0,3): #This will loop 3 times 
    target = random.randint(10,18)
    
    print("\nRound",rounds+1)
    input("Are you ready? Hit <ENTER> to continue.")
    print()
    
    for rolls in range(0,3): #The user will get three chances to roll their dice
        roll = random.randint(1,6)
        rollSum = rollSum + roll #Accumulator, adds rolls in a loop 3 times
        
        print("Sum of your rolls:",rollSum)
        time.sleep(1)
    
    if rollSum >= target: #If sum of rolls is equal or greater than target
        print("\nYou win! The target number was", target)
        wins += 1
    else: #If it is less than target
        print("\nYou lose! The target number was", target)
        losses += 1
    
    rollSum = 0 #Resets rollSum

#Outputs result to user
print("Here are your wins:",wins,"\nHere are your losses:", losses)