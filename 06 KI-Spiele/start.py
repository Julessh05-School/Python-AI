""" Codeinfo """
import random

# Author: Julian Schumacher
# Date: 22.01.2024
# Version: 1.0
# Flappy Bird mit KI

''' Import Bibliotheken '''
import sys

import pygame as pg

''' Definition Startbedingung '''
# Screen
pg.init()
width = 1000
height = 700
screen = pg.display.set_mode((width, height))
FPS = 60
FPSCLOCK = pg.time.Clock()

# Bird Position
birdPosX = width / 5
birdPosY = height / 6
birdRadius = 20
time = 0

points = 0

# Pipe
pipeWidth = 50
pipeHeight = 500
pipeGap = 200
pipeOneUpperX = width / 2
pipeOneUpperY = random.randint(-pipeHeight, 0)
pipeOneLowerX = pipeOneUpperX
pipeOneLowerY = pipeOneUpperY + pipeHeight + pipeGap

pipeTwoUpperX = width
pipeTwoUpperY = random.randint(-pipeHeight, 0)
pipeTwoLowerX = pipeTwoUpperX
pipeTwoLowerY = pipeTwoUpperY + pipeHeight + pipeGap


def print_text(text, pos, font_size, color):
    font = pg.font.SysFont(None, font_size)
    screen.blit(font.render(text, True, color), pos)


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
    screen.fill([111, 111, 111])

    '''Pipe'''
    pipeOneUpperX -= 10
    pipeOneLowerX = pipeOneUpperX
    if pipeOneUpperX < -pipeWidth:
        pipeOneUpperX = width
        pipeOneUpperY = random.randint(-pipeHeight, 0)
        pipeOneLowerY = pipeOneUpperY + pipeHeight + pipeGap
        pipeOneLowerX = pipeOneUpperX
    pg.draw.rect(screen, [255, 0, 0], [pipeOneUpperX, pipeOneUpperY, pipeWidth, pipeHeight])
    pg.draw.rect(screen, [255, 0, 0], [pipeOneLowerX, pipeOneLowerY, pipeWidth, pipeHeight])

    pipeTwoUpperX -= 10
    pipeTwoLowerX = pipeTwoUpperX
    if pipeTwoUpperX < -pipeWidth:
        pipeTwoUpperX = width
        pipeTwoUpperY = random.randint(-pipeHeight, 0)
        pipeTwoLowerY = pipeTwoUpperY + pipeHeight + pipeGap
        pipeTwoLowerX = pipeTwoUpperX
    pg.draw.rect(screen, [255, 0, 0], [pipeTwoUpperX, pipeTwoUpperY, pipeWidth, pipeHeight])
    pg.draw.rect(screen, [255, 0, 0], [pipeTwoLowerX, pipeTwoLowerY, pipeWidth, pipeHeight])

    '''Collision Check'''
    # Pipe One
    if (birdPosX == pipeOneUpperX and birdPosY < pipeOneUpperY + pipeHeight) or (
            birdPosX == pipeOneLowerX and birdPosY > pipeOneLowerY - pipeHeight):
        print_text("Collision", (height / 2, width / 2), 30, (255, 255, 255))

    elif birdPosX > pipeOneUpperX:
        points += 1

    # Pipe Two
    if (birdPosX == pipeTwoUpperX and birdPosY < pipeTwoUpperY + pipeHeight) or (
            birdPosX == pipeTwoLowerX and birdPosY > pipeTwoLowerY - pipeHeight):
        print_text("Collision", (height / 2, width / 2), 30, (255, 255, 255))
    elif birdPosX > pipeTwoUpperX:
        points += 1

    '''Bird'''
    pg.draw.circle(screen, [255, 255, 0], (birdPosX, birdPosY), radius=birdRadius)
    time += 0.25
    birdPosY = birdPosY + time ** 2

    '''Text'''
    print_text("Punkte: " + str(points), (20, 50), 25, (255, 255, 255))
    print_text("Flappy Bird", (400, 20), 40, (0, 0, 0))

    ''' ZEITEN '''
    FPSCLOCK.tick(FPS)
    pg.display.update()
