"""
Name: Kevin Nhan
Date: December 5th 2023
Description: Decoedes any caesar cipher
"""

#Variables
codeWord = ";TV^Xe"

isTheWord = "N"
newWord = ""
shift = 1
location = 0

#Loop
while isTheWord != "Y":
    for letter in codeWord:
        location = ord(letter)+shift
        if location > 127:
            location = location - 127
        newWord = newWord + chr(location)
        print(location)
    
    codeWord = newWord
    newWord = ""
    print(codeWord)
    
    isTheWord = input("Is it the word? (Y/N): ").upper()
    
    if isTheWord == "Y":
        print("Word deciphered")