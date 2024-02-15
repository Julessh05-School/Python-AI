""" Codeinfo """
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
pipeOneUpperX = width / 2
pipeOneUpperY = random.randint(-pipeHeight, 0)
pipeOneLowerX = pipeOneUpperX
pipeOneLowerY = pipeOneUpperY + pipeHeight + pipeGap
pipeOnePointSet = False

pipeTwoUpperX = width
pipeTwoUpperY = random.randint(-pipeHeight, 0)
pipeTwoLowerX = pipeTwoUpperX
pipeTwoLowerY = pipeTwoUpperY + pipeHeight + pipeGap
pipeTwoPointSet = False


def print_text(text, pos, font_size, color):
    font = pg.font.SysFont(None, font_size)
    screen.blit(font.render(text, True, color), pos)


'''Bild laden'''
fb = pg.image.load("res/fb.png")
fb = pg.transform.scale(fb, (birdWidth, birdHeight))
base = pg.image.load("res/base.png")
base = pg.transform.scale(screen, (width, height))
bg = pg.image.load("res/background.png")
bg = pg.transform.scale(screen, (width, height))
pipeLow = pg.image.load("res/pipeLow.png")
pipeLow = pg.transform.scale(screen, (0, 0))
pipeUpper = pg.image.load("res/pipeUpp.png")
pipeUpper = pg.transform.scale(screen, (0, 0))

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
    screen.fill([111, 111, 111])

    '''Pipe'''
    pipeOneUpperX -= 10
    pipeOneLowerX = pipeOneUpperX
    if pipeOneUpperX < -pipeWidth:
        pipeOnePointSet = False
        pipeOneUpperX = width
        pipeOneUpperY = random.randint(-pipeHeight, 0)
        pipeOneLowerY = pipeOneUpperY + pipeHeight + pipeGap
        pipeOneLowerX = pipeOneUpperX
    pg.draw.rect(screen, [255, 0, 0], [pipeOneUpperX, pipeOneUpperY, pipeWidth, pipeHeight])
    pg.draw.rect(screen, [255, 0, 0], [pipeOneLowerX, pipeOneLowerY, pipeWidth, pipeHeight])

    pipeTwoUpperX -= 10
    pipeTwoLowerX = pipeTwoUpperX
    if pipeTwoUpperX < -pipeWidth:
        pipeTwoPointSet = False
        pipeTwoUpperX = width
        pipeTwoUpperY = random.randint(-pipeHeight, 0)
        pipeTwoLowerY = pipeTwoUpperY + pipeHeight + pipeGap
        pipeTwoLowerX = pipeTwoUpperX
    pg.draw.rect(screen, [255, 0, 0], [pipeTwoUpperX, pipeTwoUpperY, pipeWidth, pipeHeight])
    pg.draw.rect(screen, [255, 0, 0], [pipeTwoLowerX, pipeTwoLowerY, pipeWidth, pipeHeight])

    '''Collision Check'''
    # Pipe One
    if ((pipeOneUpperX <= birdPosX + birdRadius and pipeOneUpperX + pipeWidth >= birdPosX - birdRadius)
            and (pipeOneUpperY + pipeHeight >= birdPosY - birdRadius or pipeOneLowerY <= birdPosY + birdRadius)):
        print_text("Collision", (height / 2, width / 2), 30, (255, 255, 255))
        gameOver = True

    elif birdPosX > pipeOneUpperX + pipeWidth / 2:
        if not pipeOnePointSet:
            points += 1
            pipeOnePointSet = True

    # Pipe Two
    if ((pipeTwoUpperX <= birdPosX + birdRadius and pipeTwoUpperX + pipeWidth >= birdPosX - birdRadius)
            and (pipeTwoUpperY + pipeHeight >= birdPosY - birdRadius or pipeOneLowerY <= birdPosY + birdRadius)):
        print_text("Collision", (height / 2, width / 2), 30, (255, 255, 255))
        gameOver = True

    elif birdPosX > pipeTwoUpperX + pipeWidth / 2:
        if not pipeTwoPointSet:
            points += 1
            pipeTwoPointSet = True

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
