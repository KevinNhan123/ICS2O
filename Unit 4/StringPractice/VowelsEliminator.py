"""
Name: Kevin Nhan
Date: November 10 2023
Description: Removes all vowels from any word the user inputs
"""

#Constants and Variables
VOWELS = "aieouy"

word = 0


#Asks user for word
print("This program will remove all vowels from any word the user inputs.\n")

word = input("Please enter a word: ")
while (not word.isalpha()): #Checks if the word is something other than letters
    word = input("Please enter a word: ")

#Loop
for letter in word:
    for vowel in VOWELS:
        if letter == vowel: #If the letter in the word is a vowel
            word = word.replace(letter, "") #Removes the vowel

#Outputs result
print("Here is your word without vowels:",word)