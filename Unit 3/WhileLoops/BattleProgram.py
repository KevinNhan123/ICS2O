"""
Name: Kevin Nhan
Date: October 17th 2023
Description: Battle between a goblin and Bilbo Baggins
"""

#Constants and Variables
GOBLINDAMAGE = 10

goblinHp = 100
bilboBagginsHp = 50

damage = 0
amtOfRounds = 0

#Loop
print("This program is where a goblin battles Bilbo Baggins.\n")

damage = 0
while goblinHp > 0 and bilboBagginsHp > 0: #will keep looping until one of them has a hp of 0 or less
    damage = int(input("Please enter amount of damage (from 0 to 35): "))

    while damage <= 0 or damage >= 35: #checks if the damage value is from 0 or 35, if not it will ask user again for damage value
        damage = int(input("Please enter amount of damage (from 0 to 35): "))
        
    #decreases both goblin and bilbo baggins hp
    goblinHp = goblinHp - damage 
    bilboBagginsHp = bilboBagginsHp - GOBLINDAMAGE

    #prints health for both
    print("\nGoblin health:", goblinHp)
    print("Bilbo Baggins health:", bilboBagginsHp)

    #increases amount of rounds by 1 and sets damage to -1 so it can loop and ask the user for damage value
    amtOfRounds = amtOfRounds + 1 
    damage = -1

#After either the goblin or bilbo baggins hp is 0, it will output amount of rounds it took
print("The round is now over. Here is the amount of rounds it took:",amtOfRounds)
