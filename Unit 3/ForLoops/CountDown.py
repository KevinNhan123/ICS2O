"""
Name: Kevin Nhan
Date: October 24 2023
Description: Count down loop
"""

#Libraries
import time

#Variables
prompt = 0

#Loop
print("This program will ask the user for a number to count down from.\n")

prompt = int(input("Please enter a integer to count down from: "))
for i in range(prompt, 0, -1):
    print(i, end = " ")
    time.sleep(1)

print("\nBLASTOFF!!!")