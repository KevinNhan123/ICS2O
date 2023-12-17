"""
Name: Kevin Nhan
Date: December 13th 2023
Description: Testing with pygame
"""

# Libraries
import secrets
import pygame
from Functions import *
from Settings import *
from Classes import *

pygame.init()

# Constants and Variables

# Colours
RED = (255,0,0)
YELLOW = (255,255,204)

#Pygame window related
done = False

clock = pygame.time.Clock()

# Setting up the window
screen = pygame.display.set_mode(size)
pygame.display.set_caption("12/25: Santa's Present Hunt")

#Setting up the player
player = Player("Roman", speed)

SpriteGroup = pygame.sprite.GroupSingle()
SpriteGroup.add(player)


while done != True:
    # Events handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Detects when user closes window
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                print("Pressed W")
                player.move(player.speed)
            
    screen.fill((255,255,255))
    
    #Drawing the player
    SpriteGroup.draw(screen)
    
    pygame.display.flip()
    
    clock.tick(fps)

# End of program
pygame.quit()