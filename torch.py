import os
import pygame

class Torch(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        #Add all the torch frames to self.images
        self.images = []

        image_location1 = os.path.join("assets", "torch1.png")
        self.image1 = pygame.image.load(image_location1).convert_alpha()

        image_location2 = os.path.join("assets", "torch2.png")
        self.image2 = pygame.image.load(image_location2).convert_alpha()

        image_location3 = os.path.join("assets", "torch3.png")
        self.image3 = pygame.image.load(image_location3).convert_alpha()

        image_location4 = os.path.join("assets", "torch4.png")
        self.image4 = pygame.image.load(image_location4).convert_alpha()

        image_location5 = os.path.join("assets", "torch5.png")
        self.image5 = pygame.image.load(image_location5).convert_alpha()

        #Add all images to self.images twice to make it slower
        self.images.append(self.image1)
        self.images.append(self.image1)
        self.images.append(self.image2)
        self.images.append(self.image2)
        self.images.append(self.image3)
        self.images.append(self.image3)
        self.images.append(self.image4)
        self.images.append(self.image4)
        self.images.append(self.image5)
        self.images.append(self.image5)

        self.index = 0

        self.image = self.images[self.index]

        self.rect = self.image.get_rect()

        self.rect.x = 0
        self.rect.y = 0

    #Animate the torches
    def update(self):
        
        #Move to next picture when update is called
        self.index += 1

        #If index is larger than # of images, go back to image 1
        if self.index >= len(self.images):
            self.index = 0
        
        self.image = self.images[self.index]