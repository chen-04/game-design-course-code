# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 11:26:21 2019

@author: J. Tyler McGoffin
"""

import pygame, sys
import numpy as np
from pygame.locals import *

from ship import Ship
# from laser import Laser
# from asteroid import Asteroid
from background import Background

#Set up window and frame rate variables
FPS = 30
WINDOWWIDTH = 500
WINDOWHEIGHT = 700

#Set up some Color variables
BLACK = (0, 0, 0)
NAVYBLUE = (0, 0, 128)
DARKPURPLE = (100, 0, 100)
WHITE = (255, 255, 255)
DARKGRAY = (100, 100, 100)

#Start the game
def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT #True globals
    
    pygame.init()
    
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption("Space Shooter")
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)

    showStartScreen()
    while True:
        runGame()
        showGameOverScreen()


def runGame():
    #setup the game
    score = 0#number of asteroids destroyed
    lives = 3
    levelUp = False


    #Create game objects: ship, asteroids,lasers, background
    #ship controls

    leftHeld = False
    rightHeld = False
    upHeld = False
    downHeld = False
    firing = False

    #backgrounds
    backgroundObject = Background("background", WINDOWHEIGHT)
    paralaxObject = Background("paralax", WINDOWHEIGHT)

    #game loop
    while True:
        #event handler
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
                elif event.key == K_a or event.key == K_LEFT:
                    leftHeld = True
                elif event.key == K_d or event.key == K_RIGHT:
                    rightHeld = True
                elif event.key == K_w or event.key == K_UP:
                    upHeld = True
                elif event.key == K_s or event.key == K_DOWN:
                    downHeld = True
                elif event.key == K_SPACE:
                    firing = True
            elif event.type == KEYUP:
                if event.key == K_a or event.key == K_LEFT:
                    leftHelf = False
                elif event.key == K_d or event.key == K_RIGHT:
                    rightHeld = False
                elif event.key == K_w or event.key == K_UP:
                    upHeld = False
                elif event.key == K_s or event.key == K_DOWN:
                    downHeld = False
                elif event.key == K_SPACE:
                    firing = False

        #detect collisions
        #update state
        playerShip.move(Left = leftHeld,right = right,up = upHeld,down = downHeld)

        #draw on screen
        DISPLAYSURF.fill(BLACK)
        draw(backgroundObject.image, backgroundObject.rect)
        draw(paralacObject.image, paralaxObject.rect)
        draw(imageSurf = playerShip.image, imageRect = playerShip.rect)

        pygame.display.update()
        FPSCLOCK.tick()

def draw(imageSurf, imageRect):
    DISPLAYSURF.blit(imageSurf, imageRect)

def terminate():
    pygame.quit()
    sys.exit()

def showGameOverScreen():
    pass
def showStartScreen():
    pass
    
if __name__ == '__main__':
    main()