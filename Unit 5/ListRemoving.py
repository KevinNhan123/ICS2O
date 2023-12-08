"""
Name: Kevin Nhan
Date: December 8th 2023
Description: Given a list and strings, the function will remove all instances of the string from the list
"""

#Libraries
import time

#Context of program
print("This program will demonstrate a function that removes strings from a list.\n")

#Functions
def remove_from_list(list, data):
    """This function will remove a string from any given list."""
    try:
        list.remove(data)
    except ValueError:
        print("There was no found instance of",data,"in the list!")

#Variables
list = ["Bob","Kevin","William","Derrick","Tony","Penh Da","Cole"]
prompt = 0

#Demonstrates a removal of a name
print("This is a names list:",list)
print("\nI am going to remove Bob from the list.")
time.sleep(2)
print("Removing Bob...")
time.sleep(1)
remove_from_list(list,"Bob")
print(list)
print("\nOh look! Bob is gone!")

#Asks user for a removal of a name
time.sleep(2)
print("\nNow it's your turn.")

prompt = input("Please enter a name to remove (case sensitive!): ")
remove_from_list(list, prompt)

time.sleep(2)

print("Here is the list now:",list)