"""
Name: Kevin Nhan
Date: October 13th 2023
Description: Challenge question: takes and positive number and outputs the sum of their digits (ex. 345 = 12)
"""

#Variables
choosenNum = 0
orginalNum = 0

amtOfDigits = 0

#Values required for the use of integer division on the choosen num
a = "1"
b = "0"
c = 0

sumOfDigits = 0

#Loop
choosenNum = int(input("Please enter a whole positive number: "))
orginalNum = choosenNum #Copy of value is required as choosenNum is modified in the following loop

print()

#Figures out the total amount of digits
while choosenNum > 0:
    choosenNum = choosenNum // 10
    amtOfDigits = amtOfDigits + 1

#Outputs the total amount of digits
print("Total amount of digits:", amtOfDigits)
print()

#Calculates the sum of all the digits using integer and mod functions on the choosen num
while amtOfDigits > 0:
    amtOfDigits = amtOfDigits - 1
    b = b * (amtOfDigits)
    c = int(a + b) #The number we will divide with
    
    sumOfDigits = sumOfDigits + orginalNum // c % 10 
    b = "0"

#Outputs the sum of all the digits
print("The sum of all the digits is:", sumOfDigits)
