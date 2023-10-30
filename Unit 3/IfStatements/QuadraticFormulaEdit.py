"""
Name: Kevin Nhan
Date: October 30 2023
Description: modified version of the quadratic formula, checks if the discriminant is < 0 or a perfect square
"""

#Libraries
import math

#Variables
x = 0

a = 0
b = 0
c = 0

discriminant = 0

#Asks user for variables required in the quadratic formula
print("This program will take any variable in the quadratic formula and solve for it.\n")

a = float(input("Please enter the value for a: "))
b = float(input("Please enter the value for b: "))
c = float(input("Please enter the value for c: "))

discriminant = b**2 - 4*a*c

#Checks if a solution exists
if discriminant < 0:
    print("The solution does not exist.")
    
elif discriminant / 2 == discriminant // 2: #If the solution could have been factored
    print("The solution could have been factored")
    x = (-b + math.sqrt(discriminant)) / 2*a
    print("The solution is:", round(x,2))
    x = (-b - math.sqrt(discriminant)) / 2*a
    print("Or:", round(x,2))
elif discriminant / 2 != discriminant // 2: #If it can't be factored
    x = (-b + math.sqrt(discriminant)) / 2*a
    print("The solution is:", round(x,2))
    x = (-b - math.sqrt(discriminant)) / 2*a
    print("Or:", round(x,2))