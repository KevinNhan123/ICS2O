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

plrGroup = pygame.sprite.Group()
plrGroup.add(player)

text = textFont.render("Points: ", False, RED)
textRect = text.get_rect(center = (400,80))

# Presents
presentOne = Present("small_present_0")

presentGroup = pygame.sprite.Group()
presentGroup.add(presentOne)

while done != True:
    # Events handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Detects when user closes window
            done = True
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]: #If the user holds the W key
        player.move(player.speed)
    elif keys[pygame.K_s]:
        player.move(-1*player.speed)
    
    screen.fill((70,70,70))
    
    #Drawing the player
    plrGroup.draw(screen)
    screen.blit(text, textRect)

    presentGroup.draw(screen)
    
    hit = pygame.sprite.spritecollide(player, presentGroup, True)
    if hit:
        print("True")
    
    pygame.display.flip()
    clock.tick(fps)

# End of program
pygame.quit()