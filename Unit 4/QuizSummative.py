"""
Name: Kevin Nhan
Date: November 22 2023
Description: My quiz summative, it will be a quiz that contains 6 questions
"""

#! Libraries
import time

#? Constants and Variables
MAXTRIES = 2
OPTIONS = "1234"

quizRun = True

#Information for file
correct = []
incorrect = []

questionsAnswered = 0

#User related
prompt = 0

extraTries = False

questions = [
    ["Who invented Python?", #! First Question
    ["Guido van Rossum", "Monty Python", "Mr. Ribeiro", "Microsoft"], #! Multiple choices
    "1" #! Answer
    ], #-------------------------------------------------------------------------------------
    
    ["When the user enters an input, what is the initial data type?", #* Second Question
    ["String", "Undefined", "Whatever the user entered", "Integer"], #* Multiple choices
    "1" #* Answer
    ], #-------------------------------------------------------------------------------------
    
    ["What year was Python created?", #? Third Question
     ["1967", "1991", "1979", "2001"], #? Multiple choices
     "2", #? Answer
     MAXTRIES #? Allowed tries
     ], #-------------------------------------------------------------------------------------
    
    ["What is wrong with the following code?\n\n guess = int(input(\"Please enter a number: \"))\n while (not guess.isnumeric()):\n\tprint(\"Your guess was not a number!\")", #! Fourth Question
     ["All of the below", "The loop is going to run regardless of what the user enters", "The code is formatted incorrectly", "The user might not enter a number and the program will crash"], #! Multiple choices
     "4", #! Answer
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

            #Checks if the question allows for extra tries
            try: #This is used because for some of the questions in the list, MAXTRIES is not defined in the list so it will output an error. This is like a safety net, if there is no MAXTRIES in the list, it will set extraTries to False
                if questions[question].index(MAXTRIES) == 3:
                    extraTries = True
            except ValueError:
                extraTries = False
            
            #Asks user for prompt
            if extraTries == True: #If the question is one of the harder multiple choice questions
                print("\nThis is a hard multiple choice question! You get two tries!")
                for i in range(MAXTRIES):
                    prompt = input("\nPlease chose an option: ")
                    while not prompt in OPTIONS: #Checks if prompt is not one of the options
                        print("Your choice was invaild!")
                        prompt = input("Please chose an option: ")
                        
                    #Checks if the prompt matches up with the answer
                    if prompt == questions[question][2]:
                        correct.append(question) #Adds question to correct list
                        print("\nNice! You got the question correct!")
                        break
                    else: #If the user did not answer the question correctly (If the question is not in the correct list)
                        print("\nIncorrect!")
                    
                if prompt != questions[question][2]: #After the two tries, if the last prompt was incorrect then the question is added to the incorrect list
                    incorrect.append(question)
                
            else: #If it is regular multiple choice
                prompt = input("\nPlease chose an option: ")
                while not prompt in OPTIONS: #Checks if prompt is not one of the options
                    print("Your choice was invaild!")
                    prompt = input("Please chose an option: ")
                
                #Checks if it is correct
                if prompt == questions[question][2]:
                    correct.append(question) #Adds question to correct list
                    print("\nNice! You got the question correct!")
                else: #If it is incorrect
                    incorrect.append(question)
                    print("\nIncorrect!")
        
        else: #If the question is a fill-in-the-blanks
            prompt = input("\nPlease enter an answer: ").lower()
            
            #Checks if prompt is correct
            if prompt == questions[question][1]:
                correct.append(question)
                print("\nNice! You got the question correct!")
            else: #If it is incorrect
                incorrect.append(question)
                print("\nIncorrect!")