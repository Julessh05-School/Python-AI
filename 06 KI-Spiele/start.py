""" Code info """
# Author: Julian Schumacher
# Date: 22.01.2024
# Version: 1.0
# Flappy Bird mit KI


''' Import Bibliotheken '''

import random
import sys

import pygame as pg

''' Definition Startbedingung '''
# Screen
pg.init()
width = 1000
height = 700
screen = pg.display.set_mode((width, height))
FPS = 30
FPSCLOCK = pg.time.Clock()

# Bird Position
birdPosX = width / 5
birdPosY = height / 6
birdRadius = 20
birdWidth = 35
birdHeight = 50
time = 0

points = 0
gameOver = False

# Pipe
pipeWidth = 50
pipeHeight = 500
pipeGap = 200
pipeOneX = width / 2
pipeOneUpperY = random.randint(-pipeHeight, 0)
pipeOneLowerY = pipeOneUpperY + pipeHeight + pipeGap
pipeOnePointSet = False

pipeTwoX = width
pipeTwoUpperY = random.randint(-pipeHeight, 0)
pipeTwoLowerY = pipeTwoUpperY + pipeHeight + pipeGap
pipeTwoPointSet = False


def print_text(text, pos, font_size, color):
    font = pg.font.SysFont(None, font_size)
    screen.blit(font.render(text, True, color), pos)


'''Bild laden'''
fb = pg.image.load("res/fb.png")
fb = pg.transform.scale(fb, (birdWidth, birdHeight))
base = pg.image.load("res/base.png")
base = pg.transform.scale(base, (width, height))
bg = pg.image.load("res/background.png")
bg = pg.transform.scale(bg, (width, height))
pipeLow = pg.image.load("res/pipeLow.png")
pipeLow = pg.transform.scale(pipeLow, (0, 0))
pipeUpper = pg.image.load("res/pipeUpp.png")
pipeUpper = pg.transform.scale(pipeUpper, (0, 0))

while True:
    ''' EVENTS '''
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                time = 0
                birdPosY -= 100
                pass

    ''' HINTERGRUND '''
    screen.blit(bg, (0, 0))

    '''Pipe'''
    pipeOneX -= 10
    if pipeOneX < -pipeWidth:
        pipeOnePointSet = False
        pipeOneX = width
        pipeOneUpperY = random.randint(-pipeHeight, 0)
        pipeOneLowerY = pipeOneUpperY + pipeHeight + pipeGap
    pg.draw.rect(screen, [255, 0, 0], [pipeOneX, pipeOneUpperY, pipeWidth, pipeHeight])
    pg.draw.rect(screen, [0, 255, 0], [pipeOneX, pipeOneLowerY, pipeWidth, pipeHeight])

    pipeTwoX -= 10
    if pipeTwoX < -pipeWidth:
        pipeTwoPointSet = False
        pipeTwoX = width
        pipeTwoUpperY = random.randint(-pipeHeight, 0)
        pipeTwoLowerY = pipeTwoUpperY + pipeHeight + pipeGap
    pg.draw.rect(screen, [255, 0, 0], [pipeTwoX, pipeTwoUpperY, pipeWidth, pipeHeight])
    pg.draw.rect(screen, [0, 255, 0], [pipeTwoX, pipeTwoLowerY, pipeWidth, pipeHeight])

    '''Collision Check'''
    # Pipe One
    if ((pipeOneX <= birdPosX + birdRadius and pipeOneX + pipeWidth >= birdPosX - birdRadius)
            and (birdPosY - birdRadius <= pipeOneUpperY + pipeHeight or birdPosY + birdRadius >= pipeOneLowerY)):
        print_text("Collision", (height / 2, width / 2), 30, (255, 255, 255))
        gameOver = True
        print(f"birdPos: ({birdPosX},{birdPosY}), birdRadius: {birdRadius}")
        print(f"pipeOne: ({pipeOneX},{pipeOneUpperY},{pipeOneLowerY}), pipeWidth: {pipeWidth}")
    elif birdPosX - birdRadius > pipeOneX + pipeWidth:
        if not pipeOnePointSet:
            points += 1
            pipeOnePointSet = True

    # Pipe Two
    if ((pipeTwoX <= birdPosX + birdRadius and pipeTwoX + pipeWidth >= birdPosX - birdRadius)
            and (birdPosY - birdRadius <= pipeTwoUpperY + pipeHeight or birdPosY + birdRadius >= pipeTwoLowerY)):
        print_text("Collision", (height / 2, width / 2), 30, (255, 255, 255))
        gameOver = True
        print(f"birdPos: ({birdPosX},{birdPosY}), birdRadius: {birdRadius}")
        print(f"pipeTwo: ({pipeTwoX},{pipeTwoUpperY},{pipeTwoLowerY}), pipeWidth: {pipeWidth}")
    elif birdPosX - birdRadius > pipeTwoX + pipeWidth:
        if not pipeTwoPointSet:
            points += 1
            pipeTwoPointSet = True

    # Ceiling and floor
    # if (birdPosY + birdRadius > height or birdPosY - birdRadius < 0):
    #   gameOver = True

    '''Game Over'''
    if gameOver:
        print_text("Game Over", (height / 2, width / 2), 50, (255, 255, 0))

    '''Bird'''
    pg.draw.circle(screen, [255, 255, 0], (birdPosX, birdPosY), radius=birdRadius)
    time += 0.25
    birdPosY = birdPosY + time ** 2

    '''Text'''
    print_text("Punkte: " + str(points), (20, 50), 25, (255, 255, 255))
    print_text("Flappy Bird", (400, 20), 40, (0, 0, 0))

    ''' ZEITEN '''
    FPSCLOCK.tick(FPS)
    # TODO: change
    if not gameOver:
        pg.display.update()
