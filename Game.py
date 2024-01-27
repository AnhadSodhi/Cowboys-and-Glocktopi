"""
COWBOYS AND GLOCKTOPI
"""

import sys
import os
import pygame
from random import randint

from playerbullet import Playerbullet
from player import Player
from enemy import Enemy
from crosshair import Crosshair
from floor import Floor
from torch import Torch
from youdied import EndScreen
from youwon import WinScreen

"""
SETUP section - preparing everything before the main loop runs
"""
pygame.init()

# Global constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
FRAME_RATE = 60

# The player and enemy have the same dimensions, so these boundaries apply to both.
# BOUNDARYX = SCREEN_WIDTH - CHARACTER_WIDTH
BOUNDARYX = 872
# BOUNDARYY = SCREEN_HEIGHT - CHARACTER_HEIGHT
BOUNDARYY = 516

# Useful colors 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Creating the screen and the clock
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.set_alpha(0)  # Make alpha bits transparent
clock = pygame.time.Clock()

#You Died screen
endx = 0
endy = 0
endw = 1000
endh = 600
diescreen = EndScreen(endx, endy, endw, endh)
diescreens = pygame.sprite.Group()
diescreens.add(diescreen)

#You win screen
winscreen = WinScreen(endx, endy, endw, endh)
winscreens = pygame.sprite.Group()
winscreens.add(winscreen)

#Floor
flrx = 0
flry = 0
flrw = 1000
flrh = 600
floor = Floor(flrx, flry, flrw, flrh)
floors = pygame.sprite.Group()
floors.add(floor)

#Player
player = Player()
players = pygame.sprite.Group()
players.add(player)
playerspeed = 5
playerhp = 5

#Enemy
enemy = Enemy()
enemies = pygame.sprite.Group()
enemies.add(enemy)
enemyspeedx = randint(3, 5)
enemyspeedy = randint(3, 5)
enemyhp = 5
enemybulletspeed = 5

#Bullet groups
enemybulletsup = pygame.sprite.Group()
enemybulletsright = pygame.sprite.Group()
enemybulletsdown = pygame.sprite.Group()
enemybulletsleft = pygame.sprite.Group()
enemybullets = pygame.sprite.Group()
playerbullets = pygame.sprite.Group()

#Torches
torchtopleft = Torch()
torchtopmid = Torch()
torchtopright = Torch()
torchmidleft = Torch()
torchmidright = Torch()
torchbotleft = Torch()
torchbotmid = Torch()
torchbotright = Torch()

torchestop = [torchtopleft, torchtopmid, torchtopright]
torchesmidy = [torchmidleft, torchmidright]
torchesbot = [torchbotleft, torchbotmid, torchbotright]
torchesleft = [torchtopleft, torchmidleft, torchbotleft]
torchesmidx = [torchtopmid, torchbotmid]
torchesright = [torchtopright, torchmidright, torchbotright]

#Set locations for torches
for t in torchestop:
    t.rect.y = 0
for t in torchesmidy:
    t.rect.y = SCREEN_HEIGHT / 2 #Halfway down the screen
for t in torchesbot:
    t.rect.y = SCREEN_HEIGHT - 70 #58 = image height

for t in torchesleft:
    t.rect.x = 0
for t in torchesmidx:
    t.rect.x = SCREEN_WIDTH / 2 #Halfway across the screen
for t in torchesright:
    t.rect.x = SCREEN_WIDTH - 33 #23 = image width

torches = pygame.sprite.Group()
torches.add(torchtopleft, torchtopmid, torchtopright, torchmidleft, torchmidright, torchbotleft, torchbotmid, torchbotright)

#Aimer
crosshairs = Crosshair()
aimers = pygame.sprite.Group()
aimers.add(crosshairs)

#Adding delay to firing the bullets - no spamming
playerprevioustime = pygame.time.get_ticks()
enemyprevioustime = pygame.time.get_ticks()

#Adding delay to the enemy + player collision
previousbodycollisiontime = pygame.time.get_ticks()
previousbulletcollisiontime = pygame.time.get_ticks()

while True:
    """
    EVENTS section - how the code reacts when users do things
    """
    # Mouse events
    mouse_pos = pygame.mouse.get_pos()  # Get position of mouse as a tuple representing the
    # (x, y) coordinate
    mouse_x, mouse_y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # When user clicks the 'x' on the window, close our game
            pygame.quit()
            sys.exit()

    # Keyboard events (Making the player move and making escape close the game)
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_w]:
        player.rect.y -= playerspeed
    if keys_pressed[pygame.K_a]:
        player.rect.x -= playerspeed
    if keys_pressed[pygame.K_s]:
        player.rect.y += playerspeed
    if keys_pressed[pygame.K_d]:
        player.rect.x += playerspeed
    if keys_pressed[pygame.K_ESCAPE]:
        pygame.quit()

    #Adding cooldown to player shots - no spamming
    mouse_buttons = pygame.mouse.get_pressed()
    if mouse_buttons[0]:  # If left mouse pressed
        playershottime = pygame.time.get_ticks()
        if playershottime - playerprevioustime >= 1000:
            playerprevioustime = playershottime
            player.createnewbullet0(player, playerbullets)
    if mouse_buttons[2]:  # If right mouse pressed
        pass  # Replace this line


    """
    UPDATE section - manipulate everything on the screen
    """

    """
    Aimer
    """

    crosshairs.rect.x = 876
    crosshairs.rect.y = player.rect.y

    """
    Player
    """
    
    #Player boundaries
    if player.rect.x <= 0:
        player.rect.x = 0

    if player.rect.x >= BOUNDARYX:
        player.rect.x = BOUNDARYX

    if player.rect.y <= 0:
        player.rect.y = 0

    if player.rect.y >= BOUNDARYY:
        player.rect.y = BOUNDARYY
    
    #What to do if the player dies (die screen code is in the draw function)
    if playerhp <= 0:
        player.kill()
        crosshairs.kill()
        enemy.kill()
        for b in playerbullets:
            b.kill()
        for b in enemybullets:
            b.kill()
        for t in torches:
            t.kill()
        floor.kill()

    """
    Player Bullet
    """

    #Make the bullets move and delete them if they're off screen
    playerbullets.update()
    for b in playerbullets:
        if b.rect.x >= 1000:
            b.kill()
        if b.rect.x <= 0:
            b.kill()
        if b.rect.y >= 600:
            b.kill()
        if b.rect.y <= 0:
            b.kill()

    """
    Enemy
    """
    
    #Making the enemy move and setting boundaries
    enemy.rect.x += enemyspeedx
    enemy.rect.y += enemyspeedy

    if enemy.rect.x <= 0:
        enemyspeedx *= -1

    if enemy.rect.x >= BOUNDARYX:
        enemyspeedx *= -1

    if enemy.rect.y <= 0:
        enemyspeedy *= -1

    if enemy.rect.y >= BOUNDARYY:
        enemyspeedy *= -1
    
    #What to do if you kill the enemy (win screen code is in the draw function)
    if enemyhp <= 0:
        player.kill()
        crosshairs.kill()
        enemy.kill()
        for b in playerbullets:
            b.kill()
        for b in enemybullets:
            b.kill()
        for t in torches:
            t.kill()
        floor.kill()

    """
    Enemy Bullet
    """

    #Make 4 new enemybullets appear every second, each in a different direction
    enemyshottime = pygame.time.get_ticks()
    if enemyshottime - enemyprevioustime >= 1000:
        enemyprevioustime = enemyshottime
        enemy.createnewbulletup(enemy, enemybullets, enemybulletsup, screen)
        enemy.createnewbulletright(enemy, enemybullets, enemybulletsright)
        enemy.createnewbulletdown(enemy, enemybullets, enemybulletsdown, screen)
        enemy.createnewbulletleft(enemy, enemybullets, enemybulletsleft, screen)
    
    #Make the enemy bullets move
    for b in enemybulletsup:
        b.updateup()
    for b in enemybulletsright:
        b.updateright()
    for b in enemybulletsdown:
        b.updatedown()
    for b in enemybulletsleft:
        b.updateleft()

    #Delete bullets when off-screen
    for b in enemybullets:
        if b.rect.x >= 1000:
            b.kill()
        if b.rect.x <= 0:
            b.kill()
        if b.rect.y >= 600:
            b.kill()
        if b.rect.y <= 0:
            b.kill()

    """
    Torches
    """

    #Animate the torches
    for t in torches:
        t.update()

    """
    Collisions
    """

    #Player + enemy collision cooldown (player takes damage)
    if pygame.sprite.collide_rect(player, enemy):
        currentbodycollisiontime = pygame.time.get_ticks()
        if currentbodycollisiontime - previousbodycollisiontime >= 2000:
            playerhp -= 1
    
    #player shooting enemy damage
    for p in playerbullets:
        if pygame.sprite.collide_rect(p, enemy):
            enemyhp -= 1
            p.kill()
    
    #Enemy shooting player damage
    for p in enemybullets:
        currentbulletcollisiontime = pygame.time.get_ticks()
        if pygame.sprite.collide_rect(player, p):
            if previousbulletcollisiontime - currentbulletcollisiontime >= 2000:
                playerhp -= 1
                p.kill()

    """
    DRAW section - make everything show up on screen
    """

    #Only draw these if the game is not over
    if playerhp > 0 and enemyhp > 0:
        floors.draw(screen)
        torches.draw(screen)
        playerbullets.draw(screen)
        enemybullets.draw(screen)
        players.draw(screen)
        enemies.draw(screen)
        aimers.draw(screen)
    
    #If you die, show the die screen
    if playerhp <= 0:
        diescreens.draw(screen)
    
    #If you win, show the win screen
    if enemyhp <= 0:
        winscreens.draw(screen)
    
    pygame.display.flip()  # Pygame uses a double-buffer, without this we see half-completed frames
    clock.tick(FRAME_RATE)  # Pause the clock to always maintain FRAME_RATE frames per second

