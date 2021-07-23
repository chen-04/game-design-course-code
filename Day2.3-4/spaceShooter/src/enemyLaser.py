import pygame

class EnemyLaser:
    def __init__(self, enemyRect, speed):
        self.image = pygame.image.load("ArtAssets7/enemyLaser.png")
        self.rect = self.image.get_rect()
        self.rect.midtop = enemyRect.midbottom
        self.speed = speed

    def move(self):  #Takes no input. Once fires, lasers only move up
        self.rect.bottom += self.speed