"""
Name: Kevin Nhan
Date: November 22 2023
Description: My quiz summative, it will be a quiz that contains 6 questions
"""

#! Libraries
import time

#? Variables
quizRun = True

correct = 0
questionsAnswered = 0

questions = [
    ["Who invented Python?", #! First Question
    ["Bill Gates","Monty Python","Mr. Ribeiro","Microsoft"], #! Multiple choices
    "b" #! Answer
    ], #-------------------------------------------------------------------------------------
    
    ["When the user enters an input, what is the initial data type?", #* Second Question
    ["String","Undefined","Whatever the user entered","Integer"], #* Multiple choices
    "a" #* Answer
    ], #-------------------------------------------------------------------------------------
    
    [""]
    ];

#* Gives context to the user
print("Welcome to my quiz, this quiz is about Python programming.")
print("You will be given six total questions to answer.")
print("Two questions will be ordinary multiple choice")
print("Two will be multiple choice but you will be given 2 tries to get them correct")
print("And two will be fill-in-the-blank questions.\n")

print("Good luck!\n")

#TODO Loop
while quizRun == True:
    print("dojfdf")