import pygame,sys
from pygame.locals import *


pygame.init()
FPS = 60
RESOLUTION = (800,600)
DISPLAYSURF = pygame.display.set_mode(RESOLUTION) #single argument

fpsClock = pygame.time.Clock()

sx, sy = 2, 2 #PPF for x, y axis
x, y = 400, 300

#color   =   (  R,  G,  B)
WHITE    =   (255,255,255)
BLUE     =   (  0,  0,255)


#game loop
while True:
    DISPLAYSURF.fill(WHITE)

    if x <= 100 or x >= 700:
        sx = -sx

    elif y <= 100 or y >= 500:
        sy = -sy

    x += sx
    y += sy

    pygame.draw.circle(DISPLAYSURF, BLUE, (x, y), 100)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)