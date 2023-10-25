"""
Name: Kevin Nhan
Date: September 27th 2023
Description: Turns improper fractions into mixed fractions 
"""

#Variables
numerator = 0
denominator = 0

wholeNumber = 0
remainder = 0

#Prompting the user for a numerator and a denominator
print("The program will convert a improper fraction into a mixed fraction.\n")

numerator = int(input("Please enter a numerator: "))
denominator = int(input("Please enter a denominator: "))

#Calculates both the numbers and converts into a mixed fraction
wholeNumber = numerator // denominator
remainder = numerator % denominator

#Outputs mixed fraction to user
print(str(numerator)+"/"+str(denominator),"as a mixed fraction is",wholeNumber,str(remainder)+"/"+str(denominator))
