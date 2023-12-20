"""
Name: Kevin Nhan
Date: November 17 2023
Description: Determines marks for a class of 5 students.
This program has 3 lists, one for student names, application marks, and TIPS mark
"""

#Constants and Variables
AMTOFSTUDENTS = 5
APPPERCENT = 0.65
TIPSPERCENT = 0.35

studentNames = []
marks = []
appMarks = []
tipsMarks = []

name = 0
mark = 0

appMark = 0
tipsMark = 0

#Gives context of program to user
print("This program will determine the marks for a class of 5 students.")
print("It will ask for the student names, application mark, and TIPS mark.\n")

#Loop
for student in range(AMTOFSTUDENTS):
    #Asks user for name and mark
    name = input("Please enter a name: ")
    appMark = input("Please enter a application mark: ")
    while (not appMark.isnumeric()):
        appMark = input("Please enter a application mark: ")
    appMark = float(appMark)
    
    tipsMark = input("Please enter a TIPS mark: ")
    while (not tipsMark.isnumeric()):
        tipsMark = input("Please enter a TIPS mark: ")
    tipsMark = float(tipsMark)
    print()
    
    #Adds name and marks to their respective list
    studentNames.append(name)
    appMarks.append(appMark)
    tipsMarks.append(tipsMark)

for i in range(AMTOFSTUDENTS):
    mark = (appMarks[i]*APPPERCENT) + (tipsMarks[i]*TIPSPERCENT)
    marks.append(mark)

#Outputs results
print("{0:10} {1:16} {2:15}".format("STUDENTS","CATEGORY MARKS","OVERALL MARK"))
for student in range(len(studentNames)):
    print("{0:10} {1:15} {2:6.1f}".format(studentNames[student], str(appMarks[student])+", "+str(tipsMarks[student]),marks[student]))

#Finds students who failed
print("\nSTUDENTS WHO FAILED THE COURSE:")
for i in range(AMTOFSTUDENTS):
    if marks[i] < 50:
        print(studentNames[i])