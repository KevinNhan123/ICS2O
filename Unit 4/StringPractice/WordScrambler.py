"""
Name: Kevin Nhan
Date: November 13 2023
Description: Word Scrambler program
"""

#Libraries
import random

#Constants and Variables
GUESSES = 3

originalWord = 0
word = 0
scrambledWord = ""

randomLetter = 0

#Asks user for the word
print("This is a word scrambler program. The player will be given 3 guesses to determine the original word.\n")

word = input("Please enter a word: ")
originalWord = word

#Scrambles the word
word = "Tennis"

print(word)
word = word.replace("n","")
print(word)
"""for letter in word:
    randomLetter = word[random.randint(0,len(word))]
    scrambledWord = randomLetter + scrambledWord
    word = word.replace(randomLetter,"")
    print(word)

print(word,scrambledWord,originalWord)
"""