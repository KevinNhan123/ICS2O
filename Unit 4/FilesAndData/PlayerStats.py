"""
Name: Kevin Nhan
Date: November 21 2023
Description: There are 3 stats
Strength, Speed, and Stamina
The program will ask the user for these stats and will save them
There will also be an option to load the stats.
"""

#Gives context to user
print("This program will ask you for three stats:")
print("Strength, speed, and stamina.")
print("The user will enter values for these stats and the program will save the data.")
print("If there is already data saved, the user will be asked if they would like to load their data.\n")

#Variables
strength = 0
speed = 0
stamina = 0

stats = ["Strength","Speed","Stamina"]
loadData = 0

#File
playerStats = open("Y:\\ICD2O\\Unit 4\\FilesAndData\\PlayerStats.txt", "r")

if playerStats.read() != "": #If there is  data in the file
    loadData = input("Data found! Would you like to load your stats? (Y/N): ").upper()

#Asks user for stats
if loadData != "Y":
    playerStats = open("Y:\\ICD2O\\Unit 4\\FilesAndData\\PlayerStats.txt", "w")
    strength = input("Please enter your strength: ")
    while(not strength.isnumeric()): #If the strength entered is not a number
        print("You did not enter a number!")
        strength = input("Please enter your strength: ")
    
    speed = input("\nPlease enter your speed: ")
    while(not speed.isnumeric()):
        print("You did not enter a number!")
        speed = input("Please enter your speed: ")
    
    stamina = input("\nPlease enter your stamina: ")
    while(not stamina.isnumeric()):
        print("You did not enter a number!")
        stamina = input("Please enter your stamina: ")
    
    #Adds stats to list
    stats.append(strength)
    stats.append(speed)
    stats.append(stamina)
    
    #Saves data
    print("\nSaving data...")
    for stat in range(len(stats)-3):
        playerStats.write(stats[stat]+": "+stats[len(stats)-3+stat]+"\n")
    playerStats.close()
    print("Saved data successfully.")
else:
    print("\nHere are your stats:\n")
    playerStats = open("Y:\\ICD2O\\Unit 4\\FilesAndData\\PlayerStats.txt", "r")
    print(playerStats.read())