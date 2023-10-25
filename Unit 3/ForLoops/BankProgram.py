"""
Name: Kevin Nhan
Date: October 24 2023
Description: Computes bank balance at the end of each year for 10 years from a deposit of $1000
"""

#Constants and Variables
INITALDEPOSIT = 1000
ANNUALRATE = 1.06
ENDYEAR = 10

newBalance = 0
yearInterest = 0

#Loop
newBalance = INITALDEPOSIT
for year in range(ENDYEAR):
    yearInterest = newBalance
    newBalance = newBalance * ANNUALRATE
    yearInterest = newBalance - yearInterest
    #Outputs initial balance, new balance, and interest for each year 
    print("End of Year "+str(year+1)+": Initial Balance:",INITALDEPOSIT, " New Balance:",round(newBalance,2),"Interest:",round(yearInterest,2))