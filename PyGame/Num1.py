import pygame
from tkinter import *
from pygame.locals import * 



pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("Colors!!")
pygame.draw.rect(screen,(0,0,0), (0,0, 100, 100), 10  )
while True:
    #Most of our game logic goes here
    screen.fill((56,75,198))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    #Continuously update the screen
    pygame.display.update()