"""
Name: Kevin Nhan
Date: December 17th 2023
Description: Objects for the game
"""
#Libraries
import pygame, math
from Settings import *

# Classes
class Animation():
    def __init__(self, SpriteAnim):
        self.SpriteAnim = SpriteAnim
        
        self.index = 0
    
    def animate(self, increment, obj, repeat=True):
        """Requires an increment to control the cycle speed of the sprites
            Repeat is turned on by default."""
        if self.index >= len(self.SpriteAnim):
            if repeat == True:
                self.index = 0
            else:
                self.index = len(self.SpriteAnim) - 1
        else:
            obj.image = self.SpriteAnim[int(self.index)]
            self.index += increment
            
class Present(pygame.sprite.Sprite):
    def __init__(self, name):
        super().__init__()
        self.name = name
        
        self.pos = pygame.math.Vector2()
        
        self.image = pygame.transform.scale2x(pygame.image.load("Unit 5\\FunProject\\pygameTest1\\Graphics\\Sprites\\medium_present.png").convert_alpha()) # Base image
        self.rect = self.image.get_rect(center = self.pos)
        
        self.value = 0
        self.defaultValue = 30
    
    def getValue(self):
        if self.name[-1].isnumeric():
            if int(self.name[-1]) <= len(presentValues)-1:     
                self.value = presentValues[int(self.name[-1])]
                print("\nIdenifier found! Returning present value...")
                return self.value
        
        print("\nCould not find the idenifier at the end! Returning default value...")
        return self.defaultValue

    def spawn(self, image, posXY):
        self.pos = pygame.math.Vector2(posXY)
        self.image = pygame.transform.scale2x(pygame.image.load(image).convert_alpha())
        self.rect = self.image.get_rect(center = self.pos)
    

class Player(pygame.sprite.Sprite):
    def __init__(self, name, speed):
        super().__init__()
        self.image = pygame.transform.scale2x(pygame.image.load("Unit 5\\FunProject\\pygameTest1\\Graphics\\Sprites\\player.png").convert_alpha()) # Base image
        self.rect = self.image.get_rect(center = (200, 300))
        
        self.name = name
        self.speed = speed
        
        self.points = 0
        
        self.inv = []
        
        self.walkingSprites = Animation([pygame.transform.scale2x(pygame.image.load("Unit 5\\FunProject\\pygameTest1\\Graphics\\Sprites\\player.png").convert_alpha()),
                               pygame.transform.scale2x(pygame.image.load("Unit 5\\FunProject\\pygameTest1\\Graphics\\Sprites\\player@2x.png").convert_alpha())]) 
    
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.rect.centery -= self.speed
            self.walkingSprites.animate(0.07, self)
        if keys[pygame.K_a]:
            self.rect.centerx -= self.speed
            self.walkingSprites.animate(0.07, self)
        if keys[pygame.K_s]:
            self.rect.centery += self.speed
            self.walkingSprites.animate(0.07, self)
        if keys[pygame.K_d]:
            self.rect.centerx += self.speed
            self.walkingSprites.animate(0.07, self)
        
    def addPresent(self):
        pass