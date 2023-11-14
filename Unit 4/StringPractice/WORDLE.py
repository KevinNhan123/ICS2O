"""
Name: Kevin Nhan
Date: November 14 2023
Description: This is a simplified version of WORDLE
"""

#Constants and Variables
WORD = "MONTY" #Has to be five letters
AMTOFTRIES = 5

guess = 0
restart = "Y"

#Loop
while restart == "Y":
    #Gives the user context of program
    print("This is a simplified version of WORDLE! Try to guess the word in 5 tries!\n")
    print("-"*80)
    
    for attempt in range(AMTOFTRIES):
        #Asks user for guess
        guess = input("\nPlease enter a guess: ").upper()
        while (not guess.isalpha()) or len(guess) < 5 or len(guess) > 5: #Checks if the guess is not a word or greater or less than 5 letters
            guess = input("\nPlease enter a guess (Make sure it is 5 letters and is a word): ").upper()
    
        #Compares guess to word
        for letter in range(len(WORD)):
            if WORD[letter] == guess[letter]:
                print(WORD[letter], end = "")
            else:
                print("-", end = "")
    
        #Checks if guess == word
        if guess == WORD:
            print("\nCongrats! You guessed the word!")
            break

    #End of WORDLE
    if guess != WORD:
        print("\nYou did not guess the word in 5 tries!")

    #Prompts the user if they would like to restart the program
    restart = input("\nWould you like to play again? (Y/N): ").upper()

#End of program (if user does not enter Y)
print("\nProgram complete.")