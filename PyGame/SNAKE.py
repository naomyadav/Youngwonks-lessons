import pygame
from pygame.locals import *
import random

pygame.init()
def show_text(msg, x, y, color, size):
    try:
        fontobj= pygame.font.SysFont("freesans", size)
        msgobj = fontobj.render(chr(msg),False,color)
        screen.blit(msgobj,(x, y))
    except:
        print("there has been an error!")
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Tic Tac Toe!")
pygame.draw.rect(screen,(0,0,0), (0,0, 100, 100), 10  )
foodx = (random.randint(0,600) // 50 ) * 50
foody = (random.randint(0,600) // 50 ) * 50
snakex = (random.randint(0,600) // 50 ) * 50
snakey = (random.randint(0,600) // 50 ) * 50
foodimg=pygame.image.load('/Users/naom/Downloads/Untitled_design-removebg-preview.png')
foodimg=pygame.transform.scale(foodimg,(45,45))
snakelegnth=[]
snakelegnth.append([snakex,snakey])
score=0
while True:
    #Most of our game logic goes here
    screen.fill((255,255,255))
    show_text(score,10,10,(0,0,0),10)
    screen.blit(foodimg,(foodx,foody))
    for i in snakelegnth:
        snakehead=pygame.draw.rect(screen,(0,255,0),(i[0],i[1],45,45))
    snakelegnth.insert(0,[snakex,snakey])
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_DOWN and snakey!=550:
                snakey = snakey + 50
            elif event.key == K_UP and snakey!=0:
                snakey = snakey - 50
            elif event.key == K_LEFT and snakex!=0:
                snakex = snakex - 50
            elif event.key == K_RIGHT and snakex!=550:
                snakex = snakex + 50
    if snakehead.colliderect(pygame.Rect(foodx,foody,45,45)):
        foodx = (random.randint(0,600) // 50 ) * 50
        foody = (random.randint(0,600) // 50 ) * 50 
        snakelegnth.append([snakex,snakey])
    else:
        snakelegnth.pop()
        
    #Continuously update the screen
    pygame.display.update()