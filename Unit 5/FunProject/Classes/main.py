"""
Name: Kevin Nhan
Date: December 14th 2023
Description: the main file
"""

#Libraries
from Settings import *
from Classes import *

#Variables
options = ["1","2","3"]

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
while True:
    print("\n1: Add Present\n2: Give Presents\n3: Add speed")
    prompt = input("Please enter a prompt: ")
    while prompt not in options:
        print("You did not enter a prompt!")
        prompt = input("Please enter a prompt: ")
    
    if prompt == "1":
        prompt = input("\nPlease enter a present name: ")
        
        present = Present(prompt)
        character.addPresent(present)
        
    elif prompt == "2":
        character.givePresent()
        
    elif prompt == "3":
        speed = input("\nPlease enter a value: ")
        while not speed.isnumeric() and speed[0] != "-":
            print("You did not enter a number!")
            speed = input("Please enter a value: ")
            
        speed = int(speed)
        character.changeSpeed(speed)
        