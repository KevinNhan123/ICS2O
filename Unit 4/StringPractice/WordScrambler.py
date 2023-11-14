"""
Name: Kevin Nhan
Date: November 13 2023
Description: Word Scrambler program
"""

#Libraries
import random

#Constants and Variables
GUESSES = 3

guess = 0

word = "Imagine"
scrambledWord = 0

randomLetter = 0

#Asks user for the word
print("This is a word scrambler program. The player will be given 3 guesses to determine the original word.\n")

#Scrambles the word
scrambledWord = "".join(random.sample(word, len(word))).lower()

#Loop
print("The scrambled word is", scrambledWord)
for attempt in range(GUESSES):
    guess = input("\nGuess the original word: ").lower()
    while (not word.isalpha()): #Checks if word has anything other than letters
        guess = input("\nGuess the original word: ").lower()
    if guess == word.lower():
        print("Congrats! You guessed the word!, the original word is",guess)
        break
    else:
        print("Your guess was not the original word!")

#Outputs result
print()
if guess != word.lower():
    print("Nice try, the word was",word,"better luck next time.")
print("Thank you for using this program.")