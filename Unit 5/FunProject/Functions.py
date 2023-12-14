"""
Name: Kevin Nhan
Date: December 13th 2023
Description: Testing with pygame
"""

#Libraries
import pygame

#Functions
pygame.init() #Sets up graphic toolset

def initializeWindow(size):
    """This function will set up the window for pygame"""
    
    screen = pygame.display.set_mode(size) #Opens window
    
def draw(obj, colour, pos, size = (100,100),width = 1):
    """This function will draw anything on the pygame window"""
    
    screen = pygame.display.get_surface()
    if obj == "rectangle": 
        pygame.draw.rect(screen, colour, [pos,size],width)
    elif obj == "polygon":
        points = pos
        pygame.draw.polygon(screen, colour, points,width)
    elif obj == "circle":
        center = pos
        radius = size
        pygame.draw.circle(screen, colour, center, radius)
    elif obj == "line":
        start = pos
        end = size
        pygame.draw.line(screen, colour, start, end, width)
        
def fill(colour):
    """This function will set the screen background to any colour"""
    
    screen = pygame.display.get_surface()
    screen.fill(colour)