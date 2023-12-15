"""
Name: Kevin Nhan
Date: December 14th 2023
Description: the main file
"""

#Libraries
from Settings import *
from Classes import *

#Variables
name = 0
speed = 100
present = 0

character = 0
prompt = 0

#Context of program
print("This program has a character, you can give the character presents, change their speed, and give presents for points")

#Asks user for name
name = input("Please enter a name: ")

#Defines the character
character = Character(speed, name)

#Loop
character.changeSpeed(10)
character.addPresent("small_present_5")
character.addPresent("small_present_0")
character.addPresent("medium_present_1")
character.addPresent("large_present_2")
character.addPresent("small_present_0")

character.addPresent("small_present_5")

character.givePresent()


