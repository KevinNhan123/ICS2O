"""
Name: Kevin Nhan
Date: November 16 2023
Description:
A list that stores x automatically generated random numbers
after the list is filled, it will output the mean, median and mode
"""

#Library
import random, math

#Variables
numList = []

rndNum = 0
amtOfNum = 0

mode = 0
modeNum = 0

median = 0
mean = 0


#Gives user context of program
print("This program will generate a list with any random amount of numbers and tell the user the mode, median, and mean.\n")

#Figures out amount of numbers in list
amtOfNum = random.randint(100,1000)

#Loop to add in random numbers for list
for i in range(amtOfNum):
    rndNum = random.randint(1,100) #Generates a random number

    numList.append(rndNum) #Adds the random number to the list

numList.sort() #Sorts the list from lowest to greatest

#Finds mean, median, mode
for num in numList: # Finds mode
    if numList.count(num) > mode: #If the num in the list appears more times than the previous num
        mode = numList.count(num) #Sets mode to new amount of that num
        modeNum = num #Sets the modeNum to the number

#Finds median
if len(numList) % 2 == 1: #If the amt of nums in list is odd
    median = (numList[int(math.floor(len(numList) / 2))] + numList[(int(math.floor(len(numList) / 2) + 1))]) / 2
else: #If it is even
    median = numList[int(len(numList) / 2)]

#Finds mean
for num in numList:
    mean += num

mean = mean / len(numList)

#Outputs results
print("The mode is:",modeNum)
print("The median is:",median)
print("The mean is about:",round(mean,2))