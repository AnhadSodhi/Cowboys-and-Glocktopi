import os
import pygame
from enemybullet import Enemybullet

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        image_location = os.path.join("assets", "Enemy.png")
        self.image = pygame.image.load(image_location).convert_alpha()

        self.rect = self.image.get_rect()

        self.rect.x = 871 # BOUNDARYX - 1
        self.rect.y = 515 # BOUNDARYY - 1
    
    #Different functions for different bullet directions
    def createnewbulletup(self, enemy, enemybullets, enemybulletsup, screen):

        newbulletup = Enemybullet()

        newbulletup.rect.x = enemy.rect.x
        newbulletup.rect.y = enemy.rect.y

        enemybulletsup.add(newbulletup)
        enemybullets.add(newbulletup)
    
    def createnewbulletright(self, enemy, enemybullets, enemybulletsright):
        
        newbulletright = Enemybullet()

        newbulletright.rect.x = enemy.rect.x
        newbulletright.rect.y = enemy.rect.y

        enemybulletsright.add(newbulletright)
        enemybullets.add(newbulletright)
    
    def createnewbulletdown(self, enemy, enemybullets, enemybulletsdown, screen):
        
        newbulletdown = Enemybullet()

        newbulletdown.rect.x = enemy.rect.x
        newbulletdown.rect.y = enemy.rect.y

        enemybulletsdown.add(newbulletdown)
        enemybullets.add(newbulletdown)
    
    def createnewbulletleft(self, enemy, enemybullets, enemybulletsleft, screen):
        
        newbulletleft = Enemybullet()

        newbulletleft.rect.x = enemy.rect.x
        newbulletleft.rect.y = enemy.rect.y

        enemybulletsleft.add(newbulletleft)
        enemybullets.add(newbulletleft)
