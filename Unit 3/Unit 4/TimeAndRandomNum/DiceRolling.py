"""
Name: Kevin Nhan
Date: November 2 2023
Description: Dice rolling with suspense
"""

#Libraries
import random, time

#Variables
die1 = 0
die2 = 0

#Assigning a random number to die1 and die2
die1 = random.randint(1,20)
die2 = random.randrange(20) + 1

#Outputting result to user with time delay
print("Your first roll is a", end = "")
for i in range(5):
    print(".", end = "")
    time.sleep(1)
print(die1)

print("And your second roll is a", end = "")
for i in range(5):
    print(".", end = "")
    time.sleep(1)
print(die2)