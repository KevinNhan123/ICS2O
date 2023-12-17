"""
Name: Kevin Nhan
Date: December 14th 2023
Description: Experienmenting with OOP
"""

#Libraries
from Settings import *

#Classes
class Present:
    """This class will define the presents. It controls all their values and attributes."""
    
    def __init__(self, name):
        self.name = name
        self.value = None
        self.defaultValue = 3
    
    def getValue(self):
        if self.name[-1].isnumeric():
            if int(self.name[-1]) <= len(presentValues)-1:     
                self.value = presentValues[int(self.name[-1])]
                print("\nIdenifier found! Returning present value...")
                return self.value
        
        print("\nCould not find the idenifier at the end! Returning default value...")
        return self.defaultValue

class Character:
    """This class defines the character. It has the core functions and attributes for the character."""
    
    def __init__(self, speed, name):
        self.speed = speed
        self.name = name
        
        self.inv = []
        self.MAXITEMS = 5
        self.points = 0
    
    def addPresent(self, present):
        """This function will add a present to the character's inventory.
            There is a limit of five presents.
        """
        
        if len(self.inv) < self.MAXITEMS:
            self.inv.append(present)
            print(f"\n{self.name} has gained the present, {present.name}!")
        else:
            print(f"\n{self.name} cannot hold anymore presents!")
    
    def givePresent(self):
        """This function will remove all presents from the character's inventory and give them over to Santa.
            The character will be given points based on the presents in the inventory.
        """
        
        if len(self.inv) != 0:
            for present in range(len(self.inv)):
                self.points += self.inv[present].getValue()
                
                print("Updated points:",self.points)
            self.inv.clear()
            print(f"\n{self.name}'s inventory has been wiped!")
        else:
            print(f"\n{self.name} does not have any presents!")
        
    def changeSpeed(self, value):
        """This function requires a value for a change in the characters speed."""
        
        self.speed += value
        print(f"\n{self.name} feels like they gained a plus {value} speed boost! {self.name} now has the speed {self.speed}!")
