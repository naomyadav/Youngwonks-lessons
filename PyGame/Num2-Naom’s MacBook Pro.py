import pygame
from tkinter import *
from pygame.locals import *



pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("Colors!!")
up=False
down=False
left=False
right=False
shift=True

x1=300
y1=250
while True:
    screen.fill((255,255,255))
    if shift:
        pygame.draw.circle(screen, (0,0,0), (x1,y1), 50)
    if right:
        x1+=1
    if left:
        x1-=1
    if down:
        y1+=1
    if up:
        y1-=1
    if x1-50 < 0:
        x1=50
    if x1+50 > 600:
        x1=550
    if y1-50 < 0:
        y1=50
    if y1+50 > 500:
        y1=450

    for event in pygame.event.get():
        if event.type == QUIT:
            break
            exit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                right=True
            if event.key == K_LEFT:
                left=True
            if event.key == K_UP:
                up=True
            if event.key == K_DOWN:
                down=True
            if event.key == K_LSHIFT or event.key == K_RSHIFT:
                shift=False
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                right=False
            if event.key == K_LEFT:
                left=False
            if event.key == K_UP:
                up=False
            if event.key == K_DOWN:
                down=False
            if event.key == K_LSHIFT or event.key == K_RSHIFT:
                shift=True

    #Continuously update the screen
    pygame.display.update()