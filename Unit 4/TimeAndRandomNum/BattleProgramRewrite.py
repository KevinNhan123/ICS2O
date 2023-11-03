"""
Name: Kevin Nhan
Date: November 2 2023
Description: Battle between a goblin and Bilbo Baggins
"""
#Libraries
import random, math

#Constants and Variables
MIN = 0
MAX = 35

CRITMULTIPLIER = 1.15
CRITCHANCE = 10

goblinHp = 100
bilboBagginsHp = 50

goblinDamage = 0
bilboBagginsDamage = 0
amtOfRounds = 0

#Loop
print("This program is where Bilbo Baggins battles a goblin.")

damage = 0
while goblinHp > 0 and bilboBagginsHp > 0: #will keep looping until one of them has a hp of 0 or less
    input("\nAre you ready Bilbo Baggins? Press <ENTER> to continue.")
    
    #Generates random number
    goblinDamage = random.randint(MIN, MAX)
    bilboBagginsDamage = random.randint(MIN,MAX)
    
        #10% chance for crit multiplier to be applied for bilbo baggins damage
    if random.randint(CRITCHANCE-CRITCHANCE, CRITCHANCE) == CRITCHANCE:
        bilboBagginsDamage = math.floor(bilboBagginsDamage * CRITMULTIPLIER)
        print("\nBilbo Baggins strikes the goblin with a critical hit!", bilboBagginsDamage,"DMG")
    else:
        print("\nBilbo Baggins strikes the goblin!", bilboBagginsDamage,"DMG")
        
    #10% chance for a crit multiplier to be applied to goblin damage
    if random.randint(CRITCHANCE-CRITCHANCE, CRITCHANCE) == CRITCHANCE:
        goblinDamage = math.floor(goblinDamage * CRITMULTIPLIER)
        print("The goblin strikes Bilbo Baggins with a critical hit!", goblinDamage,"DMG")
    else:
        print("The goblin strikes Bilbo Baggins!", goblinDamage,"DMG")
    
    
    #Removes hp from both characters
    goblinHp -= bilboBagginsDamage
    bilboBagginsHp -= goblinDamage
    
    #prints health for both
    print("\nBilbo Baggins health:", max(bilboBagginsHp, 0))
    print("Goblin health:", max(goblinHp, 0))
    
    #increases amount of rounds by 1 and sets damage to -1 so it can loop and ask the user for damage value
    amtOfRounds = amtOfRounds + 1 

#After either the goblin or bilbo baggins hp is 0, it will output amount of rounds it took
if max(goblinHp, 0) == max(bilboBagginsHp, 0):
    print("\nIt was a tie! Both characters have been defeated at the same time!")
elif goblinHp > bilboBagginsHp:
    print("\nBilbo Baggins lost! The goblin wins the battle after",amtOfRounds,"round!")
elif goblinHp < bilboBagginsHp:
    print("\nThe goblin has lost! Bilbo Baggins wins the battle after",amtOfRounds,"rounds!")