"""
Name: Kevin Nhan
Date: December 11th 2023
Description: Converts imperial units to metric units
"""

#Context of program
print("This program will convert imperial units to metric units")
print("The user will be prompted a menu and they will choose what imperial unit to convert.")

#Functions
def inchesToCm(value):
    """This function will convert inches to centimeters"""
    INCHESTOCM = 2.54
    
    convertedInches = value * INCHESTOCM
    
    return [convertedInches, "Cm"]

def feetToCm(value):
    """This function will convert feet to centimeters"""
    FEETTOCM = 30
    
    convertedFeet = value * FEETTOCM
    
    return [convertedFeet, "Cm"]

def yardsToMeters(value):
    YARDSTOMETERS = 0.91
    
    convertedMeters = value * YARDSTOMETERS
    
    return [convertedMeters, "M"]

def milesToKm(value):
    MILESTOKM = 1.6
    
    convertedMiles = value * MILESTOKM
    
    return [convertedMiles, "Km"]

#Variables
options = ["1","2","3","4","5"]
optionNames = ["Inches to Centimeters","Feet to centimeters","Yards to meters","Miles to kilometers","Exit"]

prompt = 0
value = 0

#Loop
while prompt != "5":
    print("\nIMPERIAL UNITS TO METRIC UNITS CONVERSION")
    for option in range(len(options)): #Prints all options out
        print(options[option] + ". " + optionNames[option])
    print()
    
    #Asks user for prompt
    prompt = input("Please enter an option: ")
    while prompt not in options: #Checks if user did not enter an option in list
        print("You did not enter an option!")
        prompt = input("Please enter an option: ")
        
    #Runs the function based off the prompt
    if prompt != "5":
        value = input("\nPlease enter a unit (integer): ")
        while not value.isnumeric(): #Checks if value is not a number
            print("You did not enter a number!")
            value = input("Please enter a unit (integer): ")
        value = int(value)
    
    if prompt == "1": #Inches to cm
        print("Here is your conversion:", inchesToCm(value)[0], inchesToCm(value)[1])
    elif prompt == "2": #Feet to cm
        print("Here is your conversion:", feetToCm(value)[0], feetToCm(value)[1])
    elif prompt == "3": #Yards to m
        print("Here is your conversion:", yardsToMeters(value)[0], yardsToMeters(value)[1])
    elif prompt == "4": #Miles to km
        print("Here is your conversion:", milesToKm(value)[0], milesToKm(value)[1])
    
    #Acts as a cool down so the user has time to look at the conversion
    input("Press <ENTER> to continue.")

#End of program
print("\nThank you for your time.")