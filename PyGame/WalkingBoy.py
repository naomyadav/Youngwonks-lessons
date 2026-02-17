import pygame
from tkinter import *
from pygame.locals import *
#PYTHONS



pygame.init()
screen = pygame.display.set_mode((1920,1080))
pygame.display.set_caption("Game")
jump=False
die=[]
for i in range(1,14,1):
    path="/Users/naom/Downloads/santa/png/Walk ("+str(i)+").png"
    image=pygame.image.load(path,"Aninimation")
    die.append(image)
frame=0
clock=pygame.time.Clock()
x=0
mvlft=False
while True:
    screen.fill((45,214,245))
    
    
    clock.tick(15)
    if jump:
        screen.blit(die[frame],(x,-10))
        x+=10
    elif mvlft:
        screen.blit(pygame.transform.flip(die[frame],True, False),(x,-10))
        x-=10
    else:
        screen.blit(die[0],(x,-10))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type==KEYDOWN:
            if event.key==K_RIGHT:
                jump=True
            if event.key==K_LEFT:
                mvlft=True
        if event.type==KEYUP:
            jump=False
            mvlft=False
    frame+=1
   
    if frame==13:
        frame=0
        
    #Continuously update the screen
    pygame.display.update()