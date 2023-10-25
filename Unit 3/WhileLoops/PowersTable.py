"""
Name: Kevin Nhan
Date: October 20 2023
Description: Powers table
"""

#Constants and Variables
SENTINEL = 10
LASTROW = 5

currentRow = 1
counter = 0

orginalValue = 0
value = 0
exponentValue = 0

#Loop
print("This program will create a power table from a value given by the user.\n")
value = int(input("Please enter an integer: "))
orginalValue = value
while currentRow != LASTROW + 1:
    while counter == SENTINEL:
        currentRow = currentRow + 1
        counter = 0
        value = orginalValue
        print()

    exponentValue = value ** currentRow
    print(str(value)+"^"+str(currentRow),":",exponentValue)
    counter = counter + 1
    value = value + 1
