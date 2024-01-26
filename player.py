import os
import pygame
from playerbullet import Playerbullet

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        image_location = os.path.join("assets", "Player.png")
        self.image = pygame.image.load(image_location).convert_alpha()

        self.rect = self.image.get_rect()

        self.rect.x = 100
        self.rect.y = 200
    
    #Shooting function
    def createnewbullet0(self, player, playerbullets):

        newbullet = Playerbullet()

        newbullet.rect.x = player.rect.x
        newbullet.rect.y = player.rect.y

        playerbullets.add(newbullet)
        
        