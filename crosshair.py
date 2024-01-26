import os
import pygame

class Crosshair(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        image_location = os.path.join("assets", "crosshair.png")
        self.image = pygame.image.load(image_location).convert_alpha()

        self.rect = self.image.get_rect()