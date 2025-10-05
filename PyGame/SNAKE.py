import pygame
from pygame.locals import *
import random

pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Colors!!")
pygame.draw.rect(screen,(0,0,0), (0,0, 100, 100), 10  )
foodx = (random.randint(0,600) // 50 ) * 50
foody = (random.randint(0,600) // 50 ) * 50
snakex = (random.randint(0,600) // 50 ) * 50
snakey = (random.randint(0,600) // 50 ) * 50
foodimg=pygame.image.load('/Users/naom/Desktop/Screenshot 2025-09-25 at 6.48.51 PM.png')
foodimg=pygame.transform.scale(foodimg,(50,50))
while True:
    #Most of our game logic goes here
    screen.fill((255,255,255))
    screen.blit(foodimg,(foodx,foody))
    snakehead=pygame.draw.rect(screen,(0,255,0),(snakex,snakey,45,45))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_DOWN and snakey!=550:
                snakey = snakey + 50
    #Continuously update the screen
    pygame.display.update()