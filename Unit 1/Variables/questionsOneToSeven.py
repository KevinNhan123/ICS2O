"""
Name: Kevin Nhan
Date: September 11th 2023
Description: Variable Exercises
"""

""" #FIRST EXERCISE (James Bond Program)
#Prompts the user for their first and last name
firstName = input("What is your first name? : ")
lastName = input("What is your last name? : ")

print("The name's " + lastName + ". " + firstName + " " + lastName + ".") #Outputs their first and last name James Bond Style
"""


""" #SECOND EXERCISE (Calculating the area of a circle)
PI = 3.14159
radius = float(input("What is the radius of the circle? : ")) #Prompts the user for a float value

areaOfCircle = PI * (radius**2) # squares the radius and then multiplies by PI

print("The area of the circle is about {0:.2f}".format(areaOfCircle))
"""


""" #FOURTH EXERCISE (Converting inches to cm)
# prompts an input for length of desk
lengthOfDesk = float(input("What is the length of the desk in inches? : "))
CONVERSION = lengthOfDesk * 2.54 # multiplies length of desk by 2.54 to get a conversion to cm

print("The length of the desk in centimeters is: ", CONVERSION) 
"""


""" #FIFTH EXERCISE (Calculating age from year of birth)
#Prompts the user for their year of birth
yearOfBirth = int(input("What year were you born in? : "))
currentYear = 2023
age = currentYear - yearOfBirth # subtracts the current year by year of birth to get age

print("You are {0} years old.".format(age))
"""


""" #SIXTH EXERCISE (Calculating with two numbers chosen by user)
#Prompts the user for two numbers
firstNumber = int(input("Please enter a number: "))
secondNumber = int(input("Please enter another number: "))

print("Here are your numbers: {0} and {1}".format(firstNumber, secondNumber)) #Outputs both numbers

print("Here are some math calculations using those two numbers:") # Performs addition, subtraction and multiplication on both numbers
print("{0} + {1} =".format(firstNumber, secondNumber), firstNumber + secondNumber)
print("{0} - {1} =".format(firstNumber, secondNumber), firstNumber - secondNumber)
print("{0} x {1} =".format(firstNumber, secondNumber), firstNumber * secondNumber)
"""


""" #SEVENTH EXERCISE (Solving an equation with a given x value)
# Prompts the user for the value of x
x = float(input("y = 2x^2 - 5x + 9, Please give any value for x: "))
problem = 2*(x)**2 - 5*(x)+ 9 # Takes the input of the user and solves the problem
print("y is equal to", problem)
"""

import math

a = 3
b = -9
c = 3

x = (-b + math.sqrt(b**2 - 4*a*c)) / 2*a


print(3*(x**2) - 9*x + 3)

x = (-b - math.sqrt(b**2 - 4*a*c)) / 2*a

print(3*(x**2) - 9*x + 3)
