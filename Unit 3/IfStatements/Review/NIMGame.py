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

amtRemoved = 0

turn = 1 # 1 = plr 1, 2 = plr 2
restart = "Y"

#Loop
print("This is the game of NIM, which is a game where two players remove stones from a pile, one at a time, until no stones are left.")

while restart.upper() == "Y":
    #Makes sure all the values are reset (in case of a previous game played)
    turn = 1
    amtRemoved = 0
    amtOfRocks = STARTINGAMT
    
    while amtOfRocks > 1: #This will keep looping until amt of rocks is 1 or less
        print("\nThere are "+str(amtOfRocks)+" stones. How many stones would you like to take?")
        
        amtRemoved = int(input("Player "+str(turn)+": "))
        while amtRemoved < MINIMUMROCKS or amtRemoved > MAXIMUMROCKS: #Checks if plr entered something lower than 1 or higher than 3
            amtRemoved = int(input("Please enter a proper amount, Player "+str(turn)+": "))
            
        amtOfRocks -= amtRemoved #Subtracts amtOfRocks from the amt entered by the plr
        turn = turn %2 +1 # This will alternate between plr 1 and 2
        
        input("\nPress <ENTER> to continue") #Acts as a little cooldown

    #Outputs the winner
    print("\nThere is one stone left... Player "+str(turn)+" takes it and loses.\n")
    print("Player "+str(turn %2 +1)+" wins!")
    
    #Asks if the user would like to restart
    restart = input("\nWould you like to play again? (Y/N): ").upper()
    
print("\nThanks for playing!")