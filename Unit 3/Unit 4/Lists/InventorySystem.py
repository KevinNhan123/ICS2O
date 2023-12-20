"""
Name: Kevin Nhan
Date: November 16 2023
Description: Inventory system
the user will be able to:
- add items
- delete items
- sort inventory
- print inventory
- quit program
"""

#Library
import time

#Constants and Variables
MAX = 5
MIN = 0

inventory = []
options = "abcde"

item = 0
prompt = 0

#Gives context of program to user
print("This program represents an inventory that would be used for a text based RPG.")
print("The user will be able to do the following:")
print("a. Add items")
print("b. Delete items")
print("c. Sort inventory")
print("d. Print inventory")
print("e. Quit program\n")

#Loop
while prompt != "e":
    #Offers user options
    print("What would you like to do?")
    print("a. Add item")
    print("b. Delete item")
    print("c. Sort inventory")
    print("d. Print inventory")
    print("e. Quit program\n")
    
    #Asks user for prompt
    prompt = input("Please choose an option: ").lower()
    while not prompt in options: #Checks if prompt is not one of the options
        print("\nYou did not enter a valid option.")
        prompt = input("Please choose an option: ").lower()
    print()
    
    if prompt == "a": #Adds items
        if len(inventory) == MAX: #If inventory is full
            print("Your inventory is full! You cannot add anymore items.\n")
        else:
            item = input("Add an item: ")
            inventory.append(item)
            print("\nAdded your item successfully.")
        
    elif prompt == "b": #Deletes items
        if len(inventory) == MIN: #If there is nothing in inventory
            print("You have nothing in your inventory!\n")
        else:    
            item = input("Remove an item: ")
            while inventory.count(item) == 0: #Checks if item exists in inventory
                print("Item not found. Here is your inventory:")
                print(inventory)
                item = input("Remove an item: ")
            inventory.remove(item)
            print("\nItem removed successfully.")
    
    elif prompt == "c": #Sorts inventory
        if len(inventory) == MIN:
            print("There is nothing to sort!\n")
        else:   
            inventory.sort()
            print("Sorted inventory successfully.")
        
    elif prompt == "d": #Prints inventory
        print(inventory)
        print()
    
    time.sleep(2)

print("Thank you for your time.")