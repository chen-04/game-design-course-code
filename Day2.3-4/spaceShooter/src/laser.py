import pygame

class Laser:
    def __init__(self, shipRect, speed):
        self.image = pygame.image.load("ArtAssets7/laser.png")
        self.rect = self.image.get_rect()
        self.rect.midbottom = shipRect.midtop
        self.speed = speed

    def move(self):  #Takes no input. Once fires, lasers only move up
        self.rect.bottom -= self.speed