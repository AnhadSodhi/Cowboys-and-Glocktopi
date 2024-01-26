import os
import pygame

class Playerbullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        image_location = os.path.join("assets", "Player_Bullet.png")
        self.image = pygame.image.load(image_location).convert_alpha()

        self.rect = self.image.get_rect()
    
    #Make the bullets move
    def update(self):
        self.speedx = 5
        self.rect.x += self.speedx
        