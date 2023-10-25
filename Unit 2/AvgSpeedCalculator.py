"""
Name: Kevin Nhan
Date: October 6th 2023
Description: Charity Road Race that gets a runner's starting time and finishing time and calculates average speed in km/h
"""

""" MY ALGORITHM
Step 1: Get the following inputs from the user:
Starting time:
hours
minutes
Ending time:
hours
minutes
distanceOfRace
Step 2: Calculate the runner's average speed in km/h
Step 3: Output the result to the user
"""

#Variables
startingHr = 0
startingMin = 0

endingHr = 0
endingMin = 0

distanceOfRace = 0

totalMin = 0
totalHr = 0

totalTime = 0

#Asks user for starting and ending times and distance of race
print("This program will get a runner's starting time and finishing time and calculates average speed in km/h.\n")

distanceOfRace = float(input("Please enter the distance of the race in km: "))

startingHr = int(input("Please enter the starting hour: "))
startingMin = int(input("Please enter the starting minute: "))

print()

endingHr = int(input("Please enter the ending hour: "))
endingMin = int(input("Please enter the ending minute: "))

print()

#Calculates total time and avg speed
convertedStartTime = startingHr * 60 + startingMin
convertedEndingTime = endingHr * 60 + endingMin


totalTime = (convertedEndingTime - convertedStartTime)

avgSpeed = round((distanceOfRace / totalTime) * 60, 2)

#Outputs result to user
print("The runner's average speed is",avgSpeed,"km/hr")

