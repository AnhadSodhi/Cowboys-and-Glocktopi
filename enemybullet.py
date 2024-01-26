import os
import pygame

class Enemybullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        image_location = os.path.join("assets", "Enemy_Bullet.png")
        self.image = pygame.image.load(image_location).convert_alpha()

        self.rect = self.image.get_rect()

    #Different update functions for different bullet directions
    def updateup(self):
        #Make the up bullets move
        self.speedy = -5
        self.rect.y += self.speedy

    def updateright(self):
        #Make the right bullets move
        self.speedx = 5
        self.rect.x += self.speedx

    def updatedown(self):
        #Make the down bullets move
        self.speedy = 5
        self.rect.y += self.speedy

    def updateleft(self):
        #Make the up bullets move
        self.speedx = -5
        self.rect.x += self.speedx