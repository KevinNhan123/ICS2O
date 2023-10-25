"""
Name: Kevin Nhan
Date: September 28th 2023
Description: Examines a student's use of time and detertimes amount of allowance for doing healthy activities
"""

#Variables

#Inputs
homeworkTime = 0
socialMediaTime = 0
eatingTime = 0
videoGameTime = 0
hobbyTime = 0
familyTime = 0

totalTime = 0

#Helps determine allowance and hours spent on healthy activities in a week
healthyActivityTime = 0
healthyActivityInWeek = 0

#Percentage of time taken for each activity
homeworkPercentage = 0
socialMediaPercentage = 0
eatingPercentage = 0
videoGamePercentage = 0
hobbyPercentage = 0
familyPercentage = 0

allowance = 0

#Prompts the user for amount of time (minutes) spent doing activities in a day
print("This program will determine the percentage of time taken for each activity, how many hours are spent doing healthy activities, and the amount of money earned for doing healthy activites.\n")

homeworkTime = float(input("Please enter the amount of time spent on homework in minutes: "))
socialMediaTime = float(input("Please enter the amount of time spent on social media in minutes: "))
eatingTime = float(input("Please enter the amount of time spent on eating in minutes: "))
videoGameTime = float(input("Please enter the amount of time spent on video games in minutes: "))
hobbyTime = float(input("Please enter the amount of time spent on hobbies in minutes: "))
familyTime = float(input("Please enter the amount of time spent with family in minutes: "))

print()
#Calculates amount of time in healthy activity, allowance, and percentage in time spent for the rest
totalTime = homeworkTime + socialMediaTime + eatingTime + videoGameTime + hobbyTime + familyTime

healthyActivityTime = homeworkTime + eatingTime + familyTime
healthyActivityInWeek = (healthyActivityTime * 7) / 60 #Multiplies healthy Activity time by 7 to get amount of minutes per week then divides by 60 to get hours

homeworkPercentage = round((homeworkTime / totalTime) * 100, 2)
socialMediaPercentage = round((socialMediaTime / totalTime) * 100, 2)
eatingPercentage = round((eatingTime / totalTime) * 100, 2)
videoGamePercentage = round((videoGameTime / totalTime) * 100, 2)
hobbyPercentage = round((hobbyTime / totalTime) * 100, 2)
familyPercentage = round((familyTime / totalTime) * 100, 2)

allowance = (healthyActivityTime / 60) * 5

#Outputs time taken for each activity, hours spent on health activities in a week, and money earned from allowance from healthy activities
print("The total time spent throughout the day during all your activities is:", round(totalTime/60,2),"Hours")
print("Here is the average percentage of time taken for each activity based on the total time spent:")
print("Homework Time:", homeworkPercentage,"%")
print("Social Media Time:", socialMediaPercentage,"%")
print("Eating Time:", eatingPercentage,"%")
print("Video Game Time:", videoGamePercentage,"%")
print("Hobby Time:", hobbyPercentage,"%")
print("Family Time", familyPercentage,"%")
print()
print("Here is the amount of hours in a week spent towards healthy activities:",round(healthyActivityInWeek,2),"Hours")
print()
print("Here is the amount of money you wound earn in the day: ${0:.2f}".format(allowance))
print("And here is the amount of money you would earn in a week: ${0:2.2f}".format(allowance * 7))







