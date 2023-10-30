"""
Name: Kevin Nhan
Date: October 27 2023
Description: Prints even or odd numbers depending on your age
"""

#Variables
age = 0

#Asking the user for their age
print("This program will start printing even or odd numbers depending on your age.\n")
age = int(input("Please enter your age: "))

#Loop
for num in range(age):
    if age / 2 != age // 2: #If it is odd
        if (num+1) /2 != (num+1) // 2:
            print(num+1) #prints out all odd numbers 
    elif age / 2 == age // 2: #If it is even
        if (num+1) /2 == (num+1) // 2:
            print(num+1) #prints out all even numbers 