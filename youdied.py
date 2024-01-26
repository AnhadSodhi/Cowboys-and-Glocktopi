import os
import pygame
import math

class EndScreen(pygame.sprite.Sprite):
    def __init__(self, endx, endy, endwidth, endheight):
        """
        Create a platform sprite. Note that these platforms are designed to be very wide and not very tall.
        
        It is required that the width is greater than or equal to the height. It is recommended to make height 50 or less. 
        Best visual effects are when the width is a multiple of the height.

        Args:
            x: The x coordinate of the platform
            y: The y coordinate of the platform
            width: The width of the platform. Must be greater than or equal to the height
            height: The height of the platform. Recommended to be 50 or less.
        """
        super().__init__()

        self.image = self.create_image(os.path.join("assets", "Endscreen.png"), endwidth, endheight)

        self.rect = self.image.get_rect()
        self.rect.x = endx
        self.rect.y = endy
        
    def create_image(self, image_location, width, height):
        
        tile_image = pygame.image.load(image_location).convert_alpha()
        
        tile_width = width
        tile_height = height
        tile_image = pygame.transform.scale(tile_image, (tile_width, tile_height))

        image = pygame.Surface((width, height))
        blits_data = [(tile_image, (tile_width * i, 0)) for i in range(math.ceil(width / tile_width))]
        image.blits(blits_data)

        return image