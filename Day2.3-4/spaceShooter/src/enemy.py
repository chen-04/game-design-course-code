import pygame
import numpy as np

class Enemy:
    def __init__(self,speed,WINDOWWIDTH, WINDOWHEIGHT):
        self.image = pygame.transform.scale(pygame.image.load("ArtAssets7/enemy.png"), (60,50))
        self.rect = self.image.get_rect()
        self.speed = random.randint(1,3)
        self.rect.bottom = 0

        self.leftLimit = 5
        self.rightLimit = WINDOWWIDTH - 5
        self.topLimit = 5
        self.bottomLimit = WINDOWHEIGHT - 5

def move(self,WINDOWHEIGHT):
    self.rect.y += self.speed
    if self.rect.y >= WINDOWHEIGHT:
        self.kill()