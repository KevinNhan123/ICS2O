"""
Name: Kevin Nhan
Date: November 1 2023
Description: This is the game of NIM
"""

#Constants and Variables
STARTINGAMT = 20

MINIMUMROCKS = 1
MAXIMUMROCKS = 3

amtOfRocks = STARTINGAMT

plrOne = 0
plrTwo = 0

turn = 1 # 1 = plr 1, 2 = plr 2
restart = "y"

#Loop
print("This is the game of NIM, which is a game where two players remove stones from a pile, one at a time, until no stones are left.")

while restart.lower() == "y":
    #Makes sure all the values are reset (in case of a previous game played)
    turn = 1
    plrOne = 0
    plrTwo = 0
    amtOfRocks = STARTINGAMT
    
    while amtOfRocks > 1: #This will keep looping until amt of rocks is 1 or less
        print("\nThere are "+str(amtOfRocks)+" stones. How many stones would you like to take?")
        plrOne = int(input("Player 1: "))
        while plrOne < MINIMUMROCKS or plrOne > MAXIMUMROCKS: #If plr 1 entered something lower than 1 or higher than 3
            plrOne = int(input("Please enter a proper amount, Player 1: "))
        amtOfRocks -= plrOne #Subtracts amtOfRocks from the amt entered by plr 1
        turn += 1 # Now its plr 2's turn
        
        if amtOfRocks <= 1: #If there is 1 rock after plr 1 finishes, plr 2 automatically loses
            break
        
        print("\nThere are "+str(amtOfRocks)+" stones. How many stones would you like to take?")
        plrTwo = int(input("Player 2: "))
        while plrTwo < MINIMUMROCKS or plrTwo > MAXIMUMROCKS: #If plr 2 entered something lower than 1 or higher than 3
            plrTwo = int(input("Please enter a proper amount, Player 2: "))
        amtOfRocks -= plrTwo
        turn += 1 #Goes back to plr 1
        if turn > 2:
            turn = 1
    #Determines the winner
    if turn == 1: #If the last turn was plr 1, then plr 2 loses
        print("\nThere is 1 stone. Player 1 takes it and loses.\n")
        print("Player 2 wins!")
    else: #Else if the last turn was plr 2, then plr 1 loses
        print("\nThere is 1 stone. Player 2 takes it and loses.\n")
        print("Player 1 wins!")
    
    #Asks if the user would like to restart
    restart = input("Would you like to play again? Y/N: ").lower()
    
print("\nThanks for playing!")