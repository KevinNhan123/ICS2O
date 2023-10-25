"""
Name: Kevin Nhan
Date: September 13th 2023
Description: Converting automobile trip into km/h
"""

# Variables
startTimeHr = int(input("Enter the starting hour and minute: "))
startTimeMin = int(input())
finishingTimeHr = int(input("Enter the finishing hour and minute: "))
finishingTimeMin = int(input())
distanceTraveled = float(input("Enter distance in kilometres: "))

# Calculating average speed km/h
elapsedTimeHr = (finishingTimeHr - startTimeHr) * 60 #Converting hours to minutes
elapsedTimeMin = finishingTimeMin - startTimeMin

totalElapsedTime = elapsedTimeHr + elapsedTimeMin # Adds the converted hour and minutes together

kmPerHour = (distanceTraveled / totalElapsedTime) * 60 # Divides elapsed time by distance traveled and multiplies by 60

# Outputs the average km/h
print("The average km/h is:",kmPerHour,"km/h")
