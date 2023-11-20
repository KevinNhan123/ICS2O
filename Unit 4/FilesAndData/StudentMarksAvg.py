"""
Name: Kevin Nhan
Date: November 20 2023
Description: Calculates the average of each student and writes their name and avg
to a new file.
"""

#Files
studentMarks = open("StudentMarks.txt", "a")

#Constants and Variables
AMTOFMARKS = 4

amtOfStudents = 0

name = 0
mark = 0
avgMark = 0

names = []
marks = []

#Gives context to user
print("This program will calculate the average mark of each student.")
print("It will add the student name and average to a new file.\n")

#Asks user for amount of students
amtOfStudents = input("How many students will you mark?: ")
while (not amtOfStudents.isnumeric()): #Checks if what is entered is not a number
    print("\nPlease enter a number.")
    amtOfStudents = input("How many students will you mark?: ")

while int(amtOfStudents) < 1: #If it is less than one
    print("\nPlease enter a number higher than 1.")
    amtOfStudents = input("How many students will you mark?: ")
amtOfStudents = int(amtOfStudents)

#Loop
for student in range(amtOfStudents):
    print("\nSTUDENT #"+str(student+1))
    #Asks user for student name
    name = input("Please enter a name: ")
    names.append(name)
    
    #Loop - Finds marks
    for i in range(AMTOFMARKS):
        print("Mark #"+str(i+1))
        
        #Asks user for mark
        mark = input("Please enter a mark: ")
        while (not mark.replace(".","").isnumeric()): #If it is not a number
            print("\nYou did not enter a mark.")
            mark = input("Please enter a mark: ")
        mark = float(mark)
        avgMark += mark #Acts as an accumulator
        
    #Calculates avgMark
    avgMark = avgMark / 4
    marks.append(avgMark)

#Outputs results
print()
print("{0:15} {1}".format("STUDENTS", "AVERAGE MARK"))
for student in range(len(names)):
    print("{0:10} {1:10.2f}".format(names[student], marks[student]))

#Saves results to file
print("\nSaving data to file...")
for student in range(len(names)):
    studentMarks.write("\n"+names[student] + str(" ") + str(marks[student])) #Writes all student names and avg marks into file
    
studentMarks.close() #Saves file
print("Saved successfully.")