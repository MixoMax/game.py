import math
import random
import pygame
import time

if(0 == 0):
    White = 255, 255, 255
    Black = 0, 0, 0
    Red = 255, 0, 0
    Green = 0, 255, 0
    Blue = 0, 0, 255
    Yellow = 255, 255, 0
    Pink = 255, 0, 255
    Violet = 0, 255, 255
    Orange = 255, 160, 0
screenx = 500
screeny = 500
pygame.init()
screen = pygame.display.set_mode((screenx, screeny))
screen.fill((Black))


while True:
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    pygame.draw.line(screen, (White), (0, 0), (500, 500))
    pygame.display.update()











