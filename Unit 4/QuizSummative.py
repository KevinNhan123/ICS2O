"""
Name: Kevin Nhan
Date: November 22 2023
Description: My quiz summative, it will be a quiz that contains 6 questions

NOTE: I am using an extension that changes the colour of comments based on the tag I added to them, that is why there are "!", "?" and "*" on most of my comments
"""

#! Libraries
import time

#? Constants and Variables
MAXTRIES = 2
OPTIONS = "1234"

quizRun = "Y"

#* Information for file
results = open("QuizSummative_RESULTS.txt", "a")

attempts = 0

correct = []
incorrect = []

grade = 0

#* User related
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

#? Loop
while quizRun == "Y":
    #? Resets variables before starting quiz
    correct = []
    incorrect = []
    
    results = open("QuizSummative_RESULTS.txt", "r")
    if results != "": #! If there is something in the file
        attempts = results.read()[-3] #Finds the last attempt in the file
        attempts = int(attempts) #Sets that attempt as the new attempt

    #* Gives context to the user
    print("**ATTEMPT:",attempts+1,"**")
    
    print("\nWelcome to my quiz, this quiz is about Python programming.")
    time.sleep(0.5)
    print("You will be given six total questions to answer.")
    print("Two questions will be ordinary multiple choice")
    time.sleep(2)
    print("Two will be multiple choice but you will be given 2 tries to get them correct")
    print("And two will be fill-in-the-blank questions.\n")
    time.sleep(2)

    print("Good luck!")
    
    #? Loops through the questions
    for question in range(len(questions)):
        time.sleep(2)
        print("\nQUESTION NUMBER",question+1)
        print(questions[question][0]) #Looks into the list and outputs the question
        print()
        
        if len(questions[question]) > 2: #If the question is multiple choice
            for option in range (len(questions[question][1])):
                time.sleep(0.5)
                print(str(option+1)+".", questions[question][1][option]) #Prints out all the options for the question

            #? Checks if the question allows for extra tries
            try: #This is used because for some of the questions in the list, MAXTRIES is not defined in the list so it will output an error. This is like a safety net, if there is no MAXTRIES in the list, it will set extraTries to False
                if questions[question].index(MAXTRIES) == 3:
                    extraTries = True
            except ValueError:
                extraTries = False
            
            #? Asks user for prompt
            time.sleep(1)
            if extraTries == True: #? If the question is one of the harder multiple choice questions
                print("\nThis is a hard multiple choice question! You get two tries!")
                time.sleep(0.5)
                for i in range(MAXTRIES):
                    prompt = input("\nPlease chose an option: ")
                    while not prompt in OPTIONS: #Checks if prompt is not one of the options
                        print("Your choice was invaild!")
                        prompt = input("Please chose an option: ")
                        
                    #? Checks if the prompt matches up with the answer
                    if prompt == questions[question][2]:
                        correct.append(question) #* Adds question to correct list
                        print("\nNice! You got the question correct!")
                        break
                    else: #! If the user did not answer the question correctly (If the question is not in the correct list)
                        print("\nIncorrect!")
                    
                if prompt != questions[question][2]: #After the two tries, if the last prompt was incorrect then the question is added to the incorrect list
                    incorrect.append(question)
                
            else: #? If it is regular multiple choice
                prompt = input("\nPlease chose an option: ")
                while not prompt in OPTIONS: #Checks if prompt is not one of the options
                    print("Your choice was invaild!")
                    prompt = input("Please chose an option: ")
                
                #* Checks if it is correct
                if prompt == questions[question][2]:
                    correct.append(question) #Adds question to correct list
                    print("\nNice! You got the question correct!")
                else: #! If it is incorrect
                    incorrect.append(question)
                    print("\nIncorrect!")
        
        else: #? If the question is a fill-in-the-blanks
            time.sleep(1)
            prompt = input("Please enter an answer: ").lower()
            
            #* Checks if prompt is correct
            if prompt == questions[question][1]:
                correct.append(question)
                print("\nNice! You got the question correct!")
            else: #! If it is incorrect
                incorrect.append(question)
                print("\nIncorrect!")
    
    #? Outputs results and saves results after quiz is over
    print("-------------------QUIZ OVER-------------------")
    time.sleep(1)
    print("\nGood job! You completed the quiz!")
    time.sleep(1)
    print("Here are your results:\n")
    time.sleep(0.5)
    
    results = open("QuizSummative_RESULTS.txt", "a")
    results.write("----------------CORRECT ANSWERS----------------\n")
    
    print("----------------CORRECT ANSWERS----------------")
    for question in correct: #* Outputs all correct answers
        time.sleep(0.5)
        print("Question "+ str(question+1) + ": ", questions[question][0])
        results.write("Question "+ str(question+1) + ": "+questions[question][0]+"\n\n")
        print()
    
    time.sleep(1)
    print("You got",len(correct),"out of",len(questions),"correct!\n")
    results.write("You got " + str(len(correct)) + " out of " + str(len(questions)) + " correct!\n\n")
    time.sleep(0.5)
    results.write("---------------INCORRECT ANSWERS---------------\n")
    
    print("---------------INCORRECT ANSWERS---------------")
    for question in incorrect: #! Outputs all incorrect answers
        time.sleep(0.5)
        print("Question "+ str(question+1) + ": ", questions[question][0])
        results.write("Question "+ str(question+1) + ": "+questions[question][0]+"\n\n")
        print()
    
    time.sleep(1)
    print("You got",len(incorrect),"incorrect!\n")
    results.write("You got " + str(len(incorrect)) + " incorrect!\n")
    time.sleep(0.5)
    
    #? Tells user their grade
    grade = (len(correct) / len(questions)) * 100
    print("Your grade is: {0:.2f}%".format(grade))
    results.write("Your grade is: " + str(grade) + "%\n")
    results.write("ATTEMPT " + str(attempts+1)+"\n\n")
    results.close()
    
    #? Asks user if they would like to re-do the quiz
    quizRun = input("Would you like to re-do the quiz? (Y/N): ").upper()

#! End of program
print("\nThank you for doing my quiz!")