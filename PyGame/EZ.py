import pygame
from tkinter import *
from pygame.locals import *
from random import randint

ci=0
pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("Colors!!")
x,y=(0,0)
screen.fill((0,0,0))
c=(0,0,0)
while True:
    try:
        pygame.draw.circle(screen,c,(x,y),10)
    except ValueError:
        print("e")
    for event in pygame.event.get():
        if event.type == QUIT:
            break
            exit()
        if event.type == MOUSEMOTION:
            x,y=event.pos
    """if c!=(255,255,255) or ci!=0:
        c=(c[0]+1,c[1]+1,c[2]+1)
    else:
        ci=1
        c=(c[0]-1,c[1]-1,c[2]-1)
    print(c)  """     
    c=(randint(0,255),randint(0,255),randint(0,255)) 
    #Continuously update the screen
    pygame.display.update()