import random, pygame, sys, time, datetime
from pygame.locals import *

WINDOWWIDTH = 640
WINDOWHEIGHT = 480
CELLSIZE = 20
assert WINDOWWIDTH % CELLSIZE == 0, "Window width must be a multiple of cell size"
assert WINDOWHEIGHT % CELLSIZE == 0, "Window height must be a multiple of cell size."
CELLWIDTH = int(WINDOWWIDTH/CELLSIZE)
CELLHEIGHT = int(WINDOWHEIGHT/CELLSIZE)
FPS = 15

#Define Colors
#Name         (   R,   G,   B)
WHITE       = ( 255, 255, 255)
BLACK       = (   0,   0,   0)
RED         = ( 255,   0,   0)
GREEN       = (   0, 255,   0)
DARKGREEN   = (   0, 155,   0)
DARKGRAY    = (  40,  40,  40)
BLUE        = (   0,   0, 255)
SKYBLUE     = (   0, 191, 255)
GOLD        = ( 255, 215,   0)
BGCOLOR = BLACK

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

#2
UP = 'W'
DOWN = 'S'
LEFT = 'A'
RIGHT = 'D'

HEAD = 0 #This is the index of the worm's head
HEADw = 0

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT
    
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('Wormies')
    
    showStartScreen()
    while(True):
        runGame(FPS)
        showGameOverScreen()
        
def runGame(speed):
    #Spaw at a random starting point
    startx = random.randint(5, CELLWIDTH - 6)
    starty = random.randint(5, CELLHEIGHT - 6)
    if startx <= (CELLWIDTH/2):
        wormCoords = [{'x': startx, 'y': starty},
                    {'x': startx - 1, 'y': starty},
                    {'x': startx - 2, 'y': starty}]
        direction = RIGHT
    else:
        wormCoords = [{'x': startx, 'y': starty},
                    {'x': startx + 1, 'y': starty},
                    {'x': startx + 2, 'y': starty}]
        direction = LEFT
    #2
    startxw = random.randint(5, CELLWIDTH - 6)
    startyw = random.randint(5, CELLHEIGHT - 6)
    if startxw <= (CELLWIDTH/2):
        wormCoordsw = [{'x': startxw, 'y': startyw},
                    {'x': startxw - 1, 'y': startyw},
                    {'x': startxw - 2, 'y': startyw}]
        directionw = RIGHT
    else:
        wormCoordsw = [{'x': startxw, 'y': startyw},
                    {'x': startxw + 1, 'y': startyw},
                    {'x': startxw + 2, 'y': startyw}]
        directionw = LEFT
    
    #start the apple in a random location

    apple = getRandomLocation()
    anotherApple = getRandomLocation()
    
    
    
    while(True): #main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if (event.key == K_LEFT) and direction != RIGHT:
                    direction = LEFT
                elif (event.key == K_RIGHT) and direction != LEFT:
                    direction = RIGHT
                elif (event.key == K_UP) and direction != DOWN:
                    direction = UP
                elif (event.key == K_DOWN) and direction != UP:
                    direction = DOWN
                if (event.key == K_a) and directionw != RIGHT:
                    directionw= LEFT
                elif (event.key == K_d) and directionw != LEFT:
                    directionw = RIGHT
                elif (event.key == K_w) and directionw != DOWN:
                    directionw = UP
                elif (event.key == K_s) and directionw != UP:
                    directionw = DOWN
                elif event.key == K_ESCAPE:
                    terminate()
                
        # check to see if the worm has hit itself or the wall
        if wormCoords[HEAD]['x'] == -1 or wormCoords[HEAD]['y'] == -1 or wormCoords[HEAD]['x'] == CELLWIDTH or wormCoords[HEAD]['y'] == CELLHEIGHT:
            return
        for wormBody in wormCoords[3:]:
            if wormBody['x'] == wormCoords[HEAD]['x'] and wormBody['y'] == wormCoords[HEAD]['y']:
                return
        #2
        if wormCoordsw[HEADw]['x'] == -1 or wormCoordsw[HEADw]['y'] == -1 or wormCoordsw[HEADw]['x'] == CELLWIDTH or wormCoordsw[HEADw]['y'] == CELLHEIGHT:
            return
        for wormBodyw in wormCoordsw[3:]:
            if wormBodyw['x'] == wormCoordsw[HEADw]['x'] and wormBodyw['y'] == wormCoords[HEADw]['y']:
                return
            
        
        #check to see if the worm has eaten the apple
        if wormCoords[HEAD]['x'] == apple['x'] and wormCoords[HEAD]['y'] == apple['y'] or (wormCoords[HEAD]['x'] == anotherApple['x'] and wormCoords[HEAD]['y'] == anotherApple['y']):
            pass
        else:
            del wormCoords[-1]
        #2
        if wormCoordsw[HEADw]['x'] == apple['x'] and wormCoordsw[HEADw]['y'] == apple['y'] or (wormCoordsw[HEADw]['x'] == anotherApple['x'] and wormCoordsw[HEADw]['y'] == anotherApple['y']):
            pass
        else:
            del wormCoordsw[-1]


        
        #move the worm by adding a new head in the direction of travel
        if direction == UP:
            newHead = {'x': wormCoords[HEAD]['x'], 'y': wormCoords[HEAD]['y'] - 1}
        elif direction == DOWN:
            newHead = {'x': wormCoords[HEAD]['x'], 'y': wormCoords[HEAD]['y'] + 1}
        elif direction == LEFT:
            newHead = {'x': wormCoords[HEAD]['x'] - 1, 'y': wormCoords[HEAD]['y']}
        elif direction == RIGHT:
            newHead = {'x': wormCoords[HEAD]['x'] + 1, 'y': wormCoords[HEAD]['y']}

        if wormCoords[HEAD]['x'] == apple['x'] and wormCoords[HEAD]['y'] == apple['y']:
            apple = getRandomLocation()
        #2
        if directionw == UP:
            newHeadw = {'x': wormCoordsw[HEADw]['x'], 'y': wormCoordsw[HEADw]['y'] - 1}
        elif directionw == DOWN:
            newHeadw = {'x': wormCoordsw[HEADw]['x'], 'y': wormCoordsw[HEADw]['y'] + 1}
        elif directionw == LEFT:
            newHeadw = {'x': wormCoordsw[HEADw]['x'] - 1, 'y': wormCoordsw[HEADw]['y']}
        elif directionw == RIGHT:
            newHeadw = {'x': wormCoordsw[HEADw]['x'] + 1, 'y': wormCoordsw[HEADw]['y']}

        if wormCoordsw[HEADw]['x'] == apple['x'] and wormCoordsw[HEADw]['y'] == apple['y']:
            apple = getRandomLocation()
        
        #check if eat the special apple
        if wormCoords[HEAD]['x'] == anotherApple['x'] and wormCoords[HEAD]['y'] == anotherApple['y']:
            anotherApple = getRandomLocation()
            speed = speed + 2
            if direction == UP:
                newHead = {'x': wormCoords[HEAD]['x'], 'y': wormCoords[HEAD]['y'] - 1}
            elif direction == DOWN:
                newHead = {'x': wormCoords[HEAD]['x'], 'y': wormCoords[HEAD]['y'] + 1}
            elif direction == LEFT:
                newHead = {'x': wormCoords[HEAD]['x'] - 1, 'y': wormCoords[HEAD]['y']}
            elif direction == RIGHT:
                newHead = {'x': wormCoords[HEAD]['x'] + 1, 'y': wormCoords[HEAD]['y']}
                #2
        if wormCoordsw[HEADw]['x'] == anotherApple['x'] and wormCoordsw[HEADw]['y'] == anotherApple['y']:
            anotherApple = getRandomLocation()
            speed = speed + 2
            if directionw == UP:
                newHeadw = {'x': wormCoordsw[HEADw]['x'], 'y': wormCoordsw[HEADw]['y'] - 1}
            elif directionw == DOWN:
                newHeadw = {'x': wormCoordsw[HEADw]['x'], 'y': wormCoordsw[HEADw]['y'] + 1}
            elif directionw == LEFT:
                newHeadw = {'x': wormCoordsw[HEADw]['x'] - 1, 'y': wormCoordsw[HEADw]['y']}
            elif directionw == RIGHT:
                newHeadw = {'x': wormCoordsw[HEADw]['x'] + 1, 'y': wormCoordsw[HEADw]['y']}
            
            
        wormCoords.insert(0, newHead)
        wormCoordsw.insert(0, newHeadw)#2
        DISPLAYSURF.fill(BGCOLOR)
        drawGrid()
        drawWorm(wormCoords)
        drawWormw(wormCoordsw)#2
        drawApple(apple)
        drawSpecialApple(anotherApple)
        timeLeft()
        drawScore(len(wormCoords)- 3,len(wormCoordsw)-3)
        
        pygame.display.update()
        FPSCLOCK.tick(speed)
        
def drawGrid():
    for x in range(0, WINDOWWIDTH, CELLSIZE):
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (x, 0), (x, WINDOWHEIGHT))
    for y in range(0, WINDOWHEIGHT, CELLSIZE):
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (0, y), (WINDOWWIDTH, y))
    
def drawWorm(wormCoords):
    for coord in wormCoords:
        x = coord['x'] * CELLSIZE
        y = coord['y'] * CELLSIZE
        wormSegmentRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
        pygame.draw.rect(DISPLAYSURF, BLUE, wormSegmentRect)
        wormInnerSegmentRect = pygame.Rect(x + 4, y + 4, CELLSIZE - 8, CELLSIZE - 8)
        pygame.draw.rect(DISPLAYSURF, WHITE, wormInnerSegmentRect)
def drawWormw(wormCoords):
    for coord in wormCoords:
        x = coord['x'] * CELLSIZE
        y = coord['y'] * CELLSIZE
        wormSegmentRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
        pygame.draw.rect(DISPLAYSURF, RED, wormSegmentRect)
        wormInnerSegmentRect = pygame.Rect(x + 4, y + 4, CELLSIZE - 8, CELLSIZE - 8)
        pygame.draw.rect(DISPLAYSURF, WHITE, wormInnerSegmentRect)
    
def drawApple(coord):
    x = coord['x'] * CELLSIZE
    y = coord['y'] * CELLSIZE
    appleRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
    pygame.draw.rect(DISPLAYSURF, RED, appleRect)

def drawSpecialApple(coord):
    x = coord['x'] * CELLSIZE
    y = coord['y'] * CELLSIZE
    anotherAppleRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
    pygame.draw.rect(DISPLAYSURF, SKYBLUE, anotherAppleRect)


def drawScore(score,scorew):
    scoreSurf = BASICFONT.render('Score for BLUE is: '+str(score), True, WHITE)
    scorewSurf = BASICFONT.render('Score for RED is: '+str(scorew), True, WHITE)
    scoreRect = scoreSurf.get_rect()
    scorewRect = scorewSurf.get_rect()
    scoreRect.topleft = (WINDOWWIDTH - 200, 25)
    scorewRect.topleft = (WINDOWWIDTH - 200, 44)
    DISPLAYSURF.blit(scoreSurf, scoreRect)
    DISPLAYSURF.blit(scorewSurf, scorewRect)


def terminate():
    pygame.quit()
    sys.exit()
    #sys.quit() for macs
        
def getRandomLocation():
    return {'x': random.randint(2, CELLWIDTH - 2), 'y': random.randint(2, CELLHEIGHT - 2)}

def getRandomApple():
    return random.randint(0, 2)
    
def showStartScreen():
    titleFont = pygame.font.Font('freesansbold.ttf', 100)
    titleSurf1 = titleFont.render('Wormy!', True, WHITE, BLUE)
    titleSurf2 = titleFont.render('Wormy!', True, RED)
    
    degrees1 = 0
    degrees2 = 0
    while(True): #looks like a game loop
        DISPLAYSURF.fill(BGCOLOR)
        rotatedSurf1 = pygame.transform.rotate(titleSurf1, degrees1)
        rotatedRect1 = rotatedSurf1.get_rect()
        rotatedRect1.center = (WINDOWWIDTH/2, WINDOWHEIGHT/2)
        DISPLAYSURF.blit(rotatedSurf1, rotatedRect1)
        
        rotatedSurf2 = pygame.transform.rotate(titleSurf2, degrees2)
        rotatedRect2 = rotatedSurf2.get_rect()
        rotatedRect2.center = (WINDOWWIDTH/2, WINDOWHEIGHT/2)
        DISPLAYSURF.blit(rotatedSurf2, rotatedRect2)
        
        drawPressKeyMsg()
        
        if checkForKeyPress():
            pygame.event.get() #clear the event cache
            return
        pygame.display.update()
        FPSCLOCK.tick(FPS)
        degrees1 += 3
        degrees2 += 7
        
def checkForKeyPress():
    for event in pygame.event.get():
        if event.type == QUIT:
            terminate()
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                terminate()
            else:
                return True
    return False

def timeLeft():
    firstTime = pygame.time.get_ticks()
    timeSurf = BASICFONT.render('You have survived for '+str(int(firstTime/1000)) +' seconds', True, GREEN)
    timeRect = timeSurf.get_rect()
    timeRect.midtop = (WINDOWWIDTH/2, 10)
    DISPLAYSURF.blit(timeSurf, timeRect)


def drawPressKeyMsg():
    pressKeySurf = BASICFONT.render('Press any key to play.', True, DARKGRAY)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.topleft = (WINDOWWIDTH - 200, WINDOWHEIGHT - 30)
    DISPLAYSURF.blit(pressKeySurf, pressKeyRect)
    
def showGameOverScreen():
    gameOverFont = pygame.font.Font('freesansbold.ttf', 150)
    gameSurf = gameOverFont.render('Game', True, WHITE)
    overSurf = gameOverFont.render('Over', True, WHITE)
    gameRect = gameSurf.get_rect()
    overRect = overSurf.get_rect()
    gameRect.midtop = (WINDOWWIDTH/2, 10)
    overRect.midtop = (WINDOWWIDTH/2, gameRect.height + 10 + 25)
    
    DISPLAYSURF.blit(gameSurf, gameRect)
    DISPLAYSURF.blit(overSurf, overRect)
    drawPressKeyMsg()
    
    pygame.display.update()
    pygame.time.wait(500)
    checkForKeyPress() #clear the event cache
    
    while(True):
        if checkForKeyPress():
            pygame.event.get() #clear the event cache
            return
    
if __name__ == '__main__':
    main()