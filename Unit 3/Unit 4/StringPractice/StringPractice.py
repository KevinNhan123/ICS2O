"""
Name: Kevin Nhan
Date: November 10 2023
Description: This program will output the first and last letters or any word
"""

#Constants and Variables
EXIT = "wow"

word = 0

firstLetter = 0
lastLetter = 0

#Loop
print("This program will output the first and last letters or any word.")
print("Enter \"wow\" to exit the program.\n")

#Asks user for a word
word = input("Please enter a word: ")
while word.lower() != EXIT:
    #Grabs the first and last letter in the program
    firstLetter = word[0]
    lastLetter = word[-1]
    
    #Outputs result to user 
    if len(word) < 2:
        print(firstLetter)
    else:
        print(firstLetter + lastLetter)
    
    #Asks user for another word
    word = input("Please enter a word: ")

#End of program
print("\nThank you for using this program.")