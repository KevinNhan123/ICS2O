"""
Name: Kevin Nhan
Date: December 13th 2023
Description: Testing with pygame
"""

# Libraries
from turtle import pen
import pygame, math, random
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

# Pygame window related
done = False

clock = pygame.time.Clock()

# Setting up the window
screen = pygame.display.set_mode(size)
pygame.display.set_caption("12/25: Santa's Present Hunt")

# Camera Control
class Camera(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        
        # Camera offset
        self.offset = pygame.math.Vector2()
        self.half_w = self.display_surface.get_size()[0] // 2
        self.half_h = self.display_surface.get_size()[1] // 2
        
        # Background
        self.ground_surf = pygame.image.load("Unit 5\\FunProject\\pygameTest1\\Graphics\\background.png").convert_alpha()
        self.ground_rect = self.ground_surf.get_rect(topleft = (0,0))
    
    def center_target_camera(self, target):
        self.offset.x = target.rect.centerx - self.half_w
        self.offset.y = target.rect.centery - self.half_h
    
    def custom_draw(self, player):
        self.center_target_camera(player)
        
        # Background
        ground_offset = self.ground_rect.topleft - self.offset
        self.display_surface.blit(self.ground_surf, ground_offset)
        
        # Active Elements
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)

# Game Elements
player = Player("Roman", speed)

cameraGroup = Camera()
cameraGroup.add(player)

presentGroup = pygame.sprite.Group()

text = textFont.render("Points: ", False, RED)
textRect = text.get_rect(center = (100,50))

# Adding presents
for i in range(20):
    presentNames = ["small_present","medium_present","large_present", "golden_present"]
    rndPresent = random.randint(0,3)
    present = Present(presentNames[rndPresent]+"_"+str(rndPresent))
    present.spawn("Unit 5\\FunProject\\pygameTest1\\Graphics\\Sprites\\"+presentNames[rndPresent]+".png",(random.randint(400, 1500),random.randint(400,1500) + 100))
    presentGroup.add(present)

cameraGroup.add(presentGroup)

# Loop
while done != True:
    # Events handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Detects when user closes window
            done = True
    
    screen.fill("black")

    cameraGroup.update()
    cameraGroup.custom_draw(player)
    player.update()
    screen.blit(textFont.render(f"Points: {player.points}", False, RED), textRect)
    
    presentCollision = pygame.sprite.spritecollide(player, presentGroup, True)
    for present in presentCollision:
        player.points += present.getValue()
    
    pygame.display.flip()
    clock.tick(fps)

# End of program
pygame.quit()