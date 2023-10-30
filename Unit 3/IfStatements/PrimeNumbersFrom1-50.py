# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    PrimeNumbersFrom1-50.py                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Kevin Nhan <kenha4996@ugcloud.ca>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/10/30 17:54:53 by Kevin Nhan        #+#    #+#              #
#    Updated: 2023/10/30 17:54:53 by Kevin Nhan       ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#Constants and Variables
AMTOFNUMS = 700
factors = 0

#Loop
print("This program will output all the prime numbers from 1 to 50.\n")

print("Here is the list of prime numbers:\n")
for num in range(AMTOFNUMS): #from 1 to the constant AMTOFNUMS
    for possibleFactors in range(num+1): #This loop checks for the possible amount of factors in a given number
        if (num+1) / (possibleFactors+1) == (num+1) // (possibleFactors+1): #if the number can be divided by the possible factor evenly, then increase factors by 1
            factors += 1
        
    #Prime numbers only have 2 factors, so this checks if the number in the loop is one or not
    if factors == 2:
        print(num+1, end = " ")
        factors = 0
    else: #If the number has more or less than 2 factors
        factors = 0