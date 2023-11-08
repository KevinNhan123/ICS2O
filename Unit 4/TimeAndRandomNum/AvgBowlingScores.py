"""
Name: Kevin Nhan
Date: November 8 2023
Description: Calculates average bowling scores
"""

#Libraries
import time

#Constants and Variables
PEOPLE = 4
AMTOFSCORES = 6

scores = []
names = []

totalScore = 0
avgScore = 0

#Loop
print("This program will calculate average bowling scores for 4 people (each person has 6 individual scores).\n")

for person in range(PEOPLE):
    names.append(input("Please enter a name: "))
    print()
    
    for score in range(AMTOFSCORES):
        totalScore += int(input("Please enter a score: "))
        
    #Calculates avgScore and then resets all values before moving onto the next person
    avgScore = round(totalScore / 6,2)
    scores.append(avgScore)
    
    totalScore = 0
    avgScore = 0
    print()

for i in range(len(names)):
    print("For",names[i],"they scored an average of",scores[i])
    time.sleep(2)