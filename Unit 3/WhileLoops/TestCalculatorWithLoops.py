"""
Name: Kevin Nhan
Date: October 19 2023
Description: Test Calculator average with loops
"""

#Variables
totalTests = 0
totalMark = 0

markOfTest = 0

#Loop
print("This program will calculate the averages of all the tests you enter, to leave the loop, enter a negative number.")
markOfTest = float(input("Please enter a mark: "))
while markOfTest >= 0:
    totalMark = totalMark + markOfTest
    totalTests = totalTests + 1
    markOfTest = float(input("Please enter a mark: "))


#Calculates the average
totalMark = totalMark / totalTests

#Output average to user
print("The average of all the tests you entered is {0:.2f}%".format(totalMark))
