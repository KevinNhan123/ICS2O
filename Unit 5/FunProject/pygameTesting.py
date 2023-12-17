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
            