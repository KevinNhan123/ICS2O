"""
Name: Kevin Nhan
Date: December 13th 2023
Description: Testing with pygame
"""

# Libraries
import pygame
from Functions import *
from Settings import *
from Classes import *

pygame.init()
pygame.font.init()

# Constants and Variables

#Text related
textFont = pygame.font.Font("Unit 5\\FunProject\\pygameTest1\\Graphics\\Fonts\\Pixeltype.ttf", 50)

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

text = textFont.render("Points: ", False, RED)
textRect = text.get_rect(center = (400,80))

while done != True:
    # Events handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Detects when user closes window
            done = True
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]: #If the user holds the W key
        player.move(player.speed)
        player.animate("Walk", 0.07)
    elif keys[pygame.K_s]:
        player.move(-1*player.speed)
        player.animate("Walk", 0.07)
    
    screen.fill((255,255,255))
    
    #Drawing the player
    SpriteGroup.draw(screen)
    screen.blit(text, textRect)
    
    pygame.display.flip()
    clock.tick(fps)

# End of program
pygame.quit()