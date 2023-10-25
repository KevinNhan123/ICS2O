"""
Name: Kevin Nhan
Date: September 21th 2023
Description: Test score calculator
"""

#Varaibles
name = 0

testMarkRecieved1 = 0
testMarkRecieved2 = 0
testMarkRecieved3 = 0

testTotalMark1 = 0
testTotalMark2 = 0
testTotalMark3 = 0

testMark1 = 0
testMark2 = 0
testMark3 = 0

averageMark = 0

#Prompt user for the name and scores for tests
print("This program will calculate three test scores and the average score out of all of them\n")

name = input("What is your name?: ")
print()
testMarkRecieved1 = float(input("What mark did you recieve on the first test?: "))
testTotalMark1 = float(input("What was the first test marked out of?: "))

testMarkRecieved2 = float(input("\nWhat mark did you recieve on the second test?: "))
testTotalMark2 = float(input("What was the second test marked out of?: "))

testMarkRecieved3 = float(input("\nWhat mark did you recieve on the third test?: "))
testTotalMark3 = float(input("What was the third test marked out of?: "))

#Calculating test scores and the average
testMark1 = testMarkRecieved1 / testTotalMark1
testMark2 = testMarkRecieved2 / testTotalMark2
testMark3 = testMarkRecieved3 / testTotalMark3

averageMark = (testMark1 + testMark2 + testMark3) / 3

#Outputs results to the user
print()
print(name + " scored {0:.2%} on the first test.".format(testMark1))
print(name + " scored {0:.2%} on the second test.".format(testMark2))
print(name + " scored {0:.2%} on the third test.".format(testMark3))
print()
print(name + "'s average performance for all the tests: {0:.2%}".format(averageMark))
