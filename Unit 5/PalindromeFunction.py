"""
Name: Kevin Nhan
Date: December 8th 2023
Description: Checks if a word is a palindrome or not using a function
"""

#Context of program
print("This program will check if the word entered by the user is a palindrome or not.\n")

#Functions
def isPalindrome(word):
    """This function takes one parameter given as a string and determines if it is a palindrome or not."""
    revWord = ""
    for letter in word:
        revWord = letter + revWord
    if revWord == word:
        return True
    else:
        return False

#Variables
word = 0

#Asks user for word
word = input("Please enter a word: ")
while not word.isalpha():
    print("You did not enter a word!")
    word = input("Please enter a word: ")

#Checks if word is a palindrome or not
if isPalindrome(word) == True:
    print("\nYour word is indeed a palindrome!")
else:
    print("\nYour word is not a palindrome!")