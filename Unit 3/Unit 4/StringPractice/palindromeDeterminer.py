"""
Name: Kevin Nhan
Date: November 13 2023
Description: Determines if a word is a palindrome
"""

#Variables
word = 0
revWord = ""

#Tells user context of program
print("This program will determine if the word you entered is a palindrome or not.\n")

#Asks user for word
word = input("Please enter a word: ")
while (not word.isalpha()): #Checks if what is entered is a word
    word = input("Please enter a word: ")

#Flips the word around
for letter in word:
    revWord = letter + revWord

#Determines if the word is the same as the revWord
if word.lower() == revWord.lower():
    print("\nYour word is a palindrome!")
else:
    print("\nYour word is not a palindrome!")