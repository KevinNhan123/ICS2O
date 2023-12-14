"""
Name: Kevin Nhan
Date: December 13th 2023
Description: Testing with pygame
"""

#Libraries
import pygame
from Functions import *

#Constants and Variables
#Colours
RED = (255,0,0)
YELLOW = (255,255,204)

size = (400,300)

done = False
clock = pygame.time.Clock()

#Initializing pygame window
initializeWindow(size)

#Loop
while not done:
    clock.tick(60)
    for event in pygame.event.get(): #When user inputs anything
        if event.type == pygame.QUIT: #When the user clicks on the "X" button
            done = True
            
    fill("white")
    draw("line",(60, 179, 113), [0, 0], [50, 30], 5)
    draw("rectangle","black", [75, 10], [50, 20], 2)
    draw("rectangle",(0, 0, 0), [150, 10], [50, 20])
    draw("rectangle", "green", [115, 210], [70, 40], 10)
    draw("polygon", "black", [[100, 100], [0, 200], [200, 200]], 5)
    draw("circle", "blue", [60, 250], 40)

    pygame.display.flip()

#End of program
pygame.quit()