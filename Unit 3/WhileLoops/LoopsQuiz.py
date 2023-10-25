"""
Name: Kevin Nhan
Date: October 23 2023
Description: Loop Quiz test for Flow Chart
"""

#Constants and Variables
MAXTEMP = 100

totalTemp = 0
avgTemp = 0
entries = 0

temp = 0

#Loop
print("This program will calculate the average temperature the user enters but will break after entering a temperature greater than 100 degrees.\n")

temp = float(input("Please enter a temperature: "))
while temp < MAXTEMP:
    entries = entries + 1
    totalTemp = totalTemp + temp
    temp = float(input("Please enter a temperature: "))

#Calculate after loop breaks
avgTemp = totalTemp / entries

#Outputs avg temp and amount of entries
print("The average temperature is: {0:.2f} degrees and the amount of entries is: {1}".format(avgTemp, entries))
