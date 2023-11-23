"""
Name: Kevin Nhan
Date: November 22 2023
Description: My quiz summative, it will be a quiz that contains 6 questions
"""

#! Libraries
import time

#? Constants and Variables
MAXTRIES = 2

quizRun = True

#Information for file
correct = 0
questionsAnswered = 0

#User related
options = "1234"
prompt = 0

questions = [
    ["Who invented Python?", #! First Question
    ["Guido van Rossum", "Monty Python", "Mr. Ribeiro", "Microsoft"], #! Multiple choices
    0 #! Answer
    ], #-------------------------------------------------------------------------------------
    
    ["When the user enters an input, what is the initial data type?", #* Second Question
    ["String", "Undefined", "Whatever the user entered", "Integer"], #* Multiple choices
    0 #* Answer
    ], #-------------------------------------------------------------------------------------
    
    ["What year was Python created?", #? Third Question
     ["1967", "1991", "1979", "2001"], #? Multiple choices
     1, #? Answer
     MAXTRIES #? Allowed tries
     ], #-------------------------------------------------------------------------------------
    
    ["What is wrong with the following code?\n\n guess = int(input(\"Please enter a number: \"))\n while (not guess.isnumeric()):\n\tprint(\"Your guess was not a number!\")", #! Fourth Question
     ["All of the below", "The loop is going to run regardless of what the user enters", "The code is formatted incorrectly", "The user might not enter a number and the program will crash"], #! Multiple choices
     3, #! Answer
     MAXTRIES #! Allowed tries
    ], #-------------------------------------------------------------------------------------
    
    ["Hoops, boops, poops, _____, you name them all. What is the blank?", #* Fifth question
     "loops" #* Answer
    ], #-------------------------------------------------------------------------------------
    
    ["______ is an amazing and easy-to-learn. With ______, I made this awesome quiz about ______!", #? Last Question
     "python" #? Answer
    ],
    ];

#Loop
while quizRun == True:
    #* Gives context to the user
    print("\nWelcome to my quiz, this quiz is about Python programming.")
    print("You will be given six total questions to answer.")
    print("Two questions will be ordinary multiple choice")
    print("Two will be multiple choice but you will be given 2 tries to get them correct")
    print("And two will be fill-in-the-blank questions.\n")

    print("Good luck!")
    
    #! Loops through the questions
    for question in range(len(questions)):
        time.sleep(2)
        print("\nQUESTION NUMBER",question+1)
        print(questions[question][0]) #Looks into the list and outputs the question
        print()
        
        if len(questions[question]) > 2: #If the question is multiple choice
            for option in range (len(questions[question][1])):
                time.sleep(0.5)
                print(str(option+1)+".", questions[question][1][option]) #Prints out all the options for the question
        
            #Asks user for prompt
            prompt = input("\nPlease chose an option: ")
            while not prompt in options: #Checks if prompt is not one of the options
                print("Your choice was invaild!")
                prompt = input("Please chose an option: ")
            
            #TODO check if there are extra tries allowed and check answer