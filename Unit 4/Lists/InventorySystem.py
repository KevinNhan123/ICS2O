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

#Variables
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
    print("a. Add items")
    print("b. Delete items")
    print("c. Sort inventory")
    print("d. Print inventory")
    print("e. Quit program\n")
    
    #Asks user for prompt
    prompt = input("Please choose an option: ").lower()
    while prompt in options == False:
        