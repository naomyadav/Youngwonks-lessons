<<<<<<< HEAD
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
            break
            exit()
    #Continuously update the screen
=======
import pygame
from tkinter import *
from pygame.locals import *



pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("Colors!!")
while True:
    #Most of our game logic goes here
    # screen.fill((56,75,198))
    # pygame.draw.rect(screen,(0,0,0), (0,0, 600, 500), 10  )
    # pygame.draw.rect(screen,(0,0,0), (0,0, 100, 100), 10  )
    # pygame.draw.rect(screen,(0,0,0), (500,0, 100, 100), 10  )
    # pygame.draw.rect(screen,(0,0,0), (0,400, 100, 100), 10  )
    # pygame.draw.rect(screen,(0,0,0), (500,400, 100, 100), 10)
    # pygame.draw.line(screen, (153, 255, 153), (100, 100), (500, 400), 10)
    # pygame.draw.line(screen, (153, 255, 153), (500, 100), (100, 400), 10)
    # pygame.draw.circle(screen, (0,0,0), (300, 250), 50)
    # pygame.draw.circle(screen, (0,0,0), (600,0), 50)
    # pygame.draw.circle(screen, (0,0,0), (600,500), 50)
    # pygame.draw.circle(screen, (0,0,0), (0,500), 50)
    # pygame.draw.circle(screen, (0,0,0), (0,0), 50)


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    #Continuously update the screen
>>>>>>> 34a7bee428fe9f16a49b09944df95f82bd37f38f
    pygame.display.update()