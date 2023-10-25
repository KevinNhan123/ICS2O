# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    HowIsYourDay                                       :+:    :+:             #
#                                                      +:+                     #
#    By: Kevin Nhan <kenha4996@ugcloud.ca>            +#+                      #
#                                                    +#+                       #
#    Created: 2023/10/23 11:25:11 by Kevin Nhan    #+#    #+#                  #
#    Updated: 2023/10/23 11:25:11 by Kevin Nhan    ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

#Constants and Variables
MAXSCALE = 10

prompt = 0

#Loop
prompt = int(input("How is your day on a scale of 1 to 10?: "))
while prompt > MAXSCALE: # If the user enters something higher than 10
    prompt = int(input("How is your day on a scale of 1 to 10?: "))

for i in range(MAXSCALE - prompt): #Subtracts 
    print("Have a nice day")