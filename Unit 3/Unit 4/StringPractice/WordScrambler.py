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

originalWord = "Imagine"
word = originalWord
scrambledWord = ""

randomLetter = 0

#Asks user for the word
print("This is a word scrambler program. The player will be given 3 guesses to determine the original word.\n")

#Scrambles the word
for i in range(len(originalWord)):
    randomLetter = random.randint(0, len(word)-1)
    
    scrambledWord = word[randomLetter] + scrambledWord
    word = word[:randomLetter] + word[randomLetter + 1:]

#Loop
print("The scrambled word is", scrambledWord.lower())
for attempt in range(GUESSES):
    guess = input("\nGuess the original word: ").lower()
    while (not guess.isalpha()): #Checks if guess has anything other than letters
        guess = input("\nGuess the original word: ").lower()
    if guess == originalWord.lower():
        print("Congrats! You guessed the word!, the original word is",originalWord)
        break
    else:
        print("Your guess was not the original word!")

#Outputs result
print()
if guess != originalWord.lower():
    print("Nice try, the word was",originalWord,"better luck next time.")
print("Thank you for using this program.")