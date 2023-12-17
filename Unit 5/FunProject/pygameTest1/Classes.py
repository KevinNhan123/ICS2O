"""
Name: Kevin Nhan
Date: December 17th 2023
Description: Objects for the game
"""
#Libraries
import pygame

# Classes
class Player(pygame.sprite.Sprite):
    def __init__(self, name, speed):
        super().__init__()
        self.image = pygame.transform.scale2x(pygame.image.load("Unit 5\\FunProject\\pygameTest1\\Graphics\\Sprites\\player.png").convert_alpha())
        self.rect = self.image.get_rect(midbottom = (200, 300))
        
        self.name = name
        self.speed = speed
        
        self.inv = []
    
    def move(self, value):
        self.rect.centerx += value