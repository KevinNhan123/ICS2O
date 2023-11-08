"""
Name: Kevin Nhan
Date: November 8 2023
Description: Evaluating an expression with predetermined values for x and y
"""

#Expression
# XY / 3X + Y
# For x = 1 to 6, for y = -4,0,4,8

#Variables
x = 0
y = 0

answer = 0

#Loop
print("This program will evaluate the expression (xy / 3x + y) with given x and y values.\n")
input("Hit <ENTER> to continue.")
print()

for newX in range(0,6):
    for newY in range(-4,9,4): #Middle value is 9 because loops stop right before the end range
        x = newX + 1
        y = newY
        answer = (x * y) / 3*x + y #Evaluates the expression with given x and y
        
        #Outputs result
        x = "x= "+str(x)
        y = "y= "+str(y)
        answer = "Answer: "+str(round(answer,2))
        
        print("{0:10} {1:10} {2:10}".format(x,y,answer))