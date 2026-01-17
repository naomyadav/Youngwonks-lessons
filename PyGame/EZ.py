import pygame
from tkinter import *
from pygame.locals import *
from random import randint


pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("Colors!!")
x,y=(0,0)
while True:
    screen.fill((0,0,0))
    pygame.draw.circle(screen,(0,0,255),(x,y),10)
    for event in pygame.event.get():
        if event.type == QUIT:
            break
            exit()
        if event.type == MOUSEMOTION:
            x,y=event.pos
            
    #Continuously update the screen
    pygame.display.update()