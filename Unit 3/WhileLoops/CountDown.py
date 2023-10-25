"""
Name: Kevin Nhan
Date: October 16th 2023
Description: Count down from 10 to 1
"""

#Libaries
import time

#Variables
start = 10
end = 0



#Loop
print("Wait until this countdown reaches zero for a surprise...")

while start != end:
    print(str(start) + "...")
    start = start - 1
    time.sleep(1)
    
print("BLAST OFF!!!")
