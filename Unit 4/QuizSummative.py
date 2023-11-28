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
OPTIONS = ["1","2","3","4"]

quizRun = "Y"

#* Information for file
results = open("QuizSummative_RESULTS.txt", "a")

attempts = 0

correct = []
incorrect = []
answers = []

grade = 0

#* User related
prompt = 0
extraTries = 0

questions = [
    ["Who invented Python?", #! First Question [0][0]
     "1", #! Answer [0][1]
    ["Guido van Rossum", "Monty Python", "Mr. Ribeiro", "Microsoft"] #! Multiple choices [0][2]
    ], #-------------------------------------------------------------------------------------
    
    ["When the user enters an input, what is the initial data type?", #* Second Question [1][0]
     "1", #* Answer [1][1]
    ["String", "Undefined", "Whatever the user entered", "Integer"] #* Multiple choices [1][2]
    ], #-------------------------------------------------------------------------------------
    
    ["What year was Python created?", #? Third Question [2][0]
     "2", #? Answer [2][1]
     ["1967", "1991", "1979", "2001"], #? Multiple choices [2][2]
     MAXTRIES #? Allowed tries [2][3]
     ], #-------------------------------------------------------------------------------------
    
    ["What is wrong with the following code?\n\n guess = int(input(\"Please enter a number: \"))\n while (not guess.isnumeric()):\n\tprint(\"Your guess was not a number!\")", #! Fourth Question [3][0]
      "3", #! Answer [3][1]
     ["The loop is going to run regardless of what the user enters", "The code is formatted incorrectly", "The user might not enter a number and the program will crash", "All of the above"], #! Multiple choices [3][2]
     MAXTRIES #! Allowed tries [3][3]
    ], #-------------------------------------------------------------------------------------
    
    ["Hoops, boops, poops, _____, you name them all. What is the blank?", #* Fifth question [4][0]
     "loops" #* Answer [4][1]
    ], #-------------------------------------------------------------------------------------
    
    ["______ is an amazing and easy-to-learn. With ______, I made this awesome quiz about ______!", #? Last Question [5][0]
     "python" #? Answer [5][1]
    ]
    ];

#? Loop
while quizRun == "Y":
    #? Resets variables before starting quiz
    correct = []
    incorrect = []
    answers = []
    
    results = open("QuizSummative_RESULTS.txt", "r")
    if results.read() != "": #! If there is something in the file
        results = open("QuizSummative_RESULTS.txt", "r")
        attempts = results.read()[-3] #Finds the last attempt in the file
        attempts = int(attempts) #Sets that attempt as the new attempt

    #* Gives context to the user
    print("{0:24} {1}".format("","** ATTEMPT: " + str(attempts+1)+" **"))
    
    print("-"*70)
    print("\nWelcome to my quiz, this quiz is about Python programming.")
    time.sleep(0.5)
    print("You will be given six total questions to answer.\n")
    time.sleep(1)
    print("Two questions will be ordinary multiple choice")
    time.sleep(0.5)
    print("Two will be multiple choice but you will be given 2 tries to get them correct")
    time.sleep(0.5)
    print("And two will be fill-in-the-blank questions.\n")
    time.sleep(2)

    print("{0:27} {1}".format("", "Good Luck!"))
    print("-"*70)
    
    #? Loops through the questions
    for question in range(len(questions)):
        time.sleep(2)
        print("\nQUESTION NUMBER",question+1)
        time.sleep(0.5)
        print(questions[question][0]) #Looks into the list and outputs the question
        print()
        
        if len(questions[question]) > 2: #If the question is multiple choice
            for option in range (len(questions[question][2])): #Prints out all the options for the question
                time.sleep(0.5)
                print(str(option+1)+".", questions[question][2][option]) 

            #? Checks if the question allows for extra tries
            try: #This is used because for some of the questions in the list, MAXTRIES is not defined in the list so it will output an error. This is like a safety net, if there is no MAXTRIES in the list, it will set extraTries to False
                if questions[question].index(MAXTRIES) == 3:
                    extraTries = MAXTRIES
            except ValueError:
                extraTries = 1
            
            #? Asks user for prompt
            time.sleep(0.5)
            if extraTries == MAXTRIES:
                print("\nThis is a hard multiple choice question! You get two tries!")
                
            for i in range(extraTries):
                prompt = input("\nPlease chose an option: ")
                while not prompt in OPTIONS: #Checks if prompt is not one of the options
                    print("Your choice was invaild!")
                    prompt = input("Please chose an option: ")
                    
                #? Checks if the prompt matches up with the answer
                if prompt == questions[question][1]:
                    correct.append(question) #* Adds question to correct list
                    print("Correct!")
                    break
                else: #! If the user did not answer the question correctly (If the question is not in the correct list)
                    print("Incorrect!")

            #After the two tries, if the last prompt was incorrect then the question is added to the incorrect list and answer is added to answers list
            if prompt != questions[question][1]:
                incorrect.append(question)
                answers.append(prompt)
        
        else: #? If the question is a fill-in-the-blanks
            time.sleep(0.5)
            prompt = input("Please enter an answer: ").lower()
            
            #* Checks if prompt is correct
            if prompt == questions[question][1]:
                correct.append(question)
                print("Correct!")
            else: #! If it is incorrect
                incorrect.append(question)
                answers.append(prompt)
                print("Incorrect!")
    
    #? Outputs results and saves results after quiz is over
    print("\n-------------------QUIZ OVER-------------------")
    time.sleep(1)
    print("Good job! You completed the quiz!")
    time.sleep(1)
    print("Here are your results:\n")
    time.sleep(0.5)
    
    results = open("QuizSummative_RESULTS.txt", "a")
    results.write("** ATTEMPT " + str(attempts+1) + " **\n")
    
    #* Outputs all correct answers
    results.write("----------------CORRECT ANSWERS----------------\n")
    print("----------------CORRECT ANSWERS----------------")
    for question in correct:
        time.sleep(1)
        print("Question "+ str(question+1) + ": " + questions[question][0] + "\nAnswer: " + questions[question][1])
        results.write("Question "+ str(question+1) + ": "+questions[question][0] + "\nAnswer: " + questions[question][1] + "\n\n")
        print()
    
    time.sleep(1)
    print("You got",len(correct),"out of",len(questions),"correct!\n") #* Tells user how many they got correctly
    results.write("You got " + str(len(correct)) + " out of " + str(len(questions)) + " correct!\n\n")
    time.sleep(3)
    
    #! Outputs all incorrect answers
    results.write("---------------INCORRECT ANSWERS---------------\n")
    print("---------------INCORRECT ANSWERS---------------")
    for question in range(len(incorrect)):
        time.sleep(1)
        print("Question "+ str(question+1) + ": " + questions[incorrect[question]][0] + "\nYour answer: " + answers[question] + "\nCorrect answer: " + questions[incorrect[question]][1])
        results.write("Question "+ str(question+1) + ": " + questions[incorrect[question]][0] + "\nYour answer: " + answers[question] + "\nCorrect answer: " + questions[incorrect[question]][1] + "\n\n")
        print()
    
    time.sleep(1)
    print("You got",len(incorrect),"incorrect!\n") #! Tells user how many they got incorrectly
    results.write("You got " + str(len(incorrect)) + " incorrect!\n")
    time.sleep(3)
    
    #? Tells user their grade
    grade = (len(correct) / len(questions)) * 100
    print("Your grade is: {0:.2f}%".format(grade))
    results.write("Your grade is: " + str(round(grade, 2)) + "%\n")
    results.write(str(attempts+1)+"\n\n")
    results.close() #Saves results to file
    
    #? Asks user if they would like to re-do the quiz
    quizRun = input("Would you like to re-do the quiz? (Y/N): ").upper()

#! End of program
print("\nThank you for doing my quiz!")