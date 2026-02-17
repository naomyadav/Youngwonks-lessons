import pygame
from tkinter import *
from pygame.locals import *



pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("Game!!")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            break
            exit()
    #Continuously update the screen
    pygame.display.update()