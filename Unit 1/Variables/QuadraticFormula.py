"""
Name: Kevin Nhan
Date: September 13th 2023
Description: Solving for x using the quadratic formula
"""

# Libaries
import math

# Variables
#x = 0.0

# 3*(x)**2 - 9*x + 3
a = 3
b = -9
c = 3

# Solving for x
x = (-1*b + (math.sqrt(b**2 - 4*a*c)) / 2*a)

print("x is equal to:",round(x,2))

x = (-1*b - (math.sqrt(b**2 - 4*a*c)) / 2*a)

print("or x is equal to:",round(x,2))
