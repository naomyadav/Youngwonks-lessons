import pygame
from tkinter import *
from pygame.locals import *
#PYTHONS



pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Game")
die=[]
for i in range(1,16,1):
    path="/Users/naom/Downloads/png/Dead ("+str(i)+").png"
    image=pygame.image.load(path,"Aninimation")
    die.append(image)
frame=0
clock=pygame.time.Clock()
while True:
    clock.tick(30)
    screen.fill((45,214,245))
    screen.blit(die[frame],(-10,-10))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    frame+=1
    if frame==15:
        frame=0
    #Continuously update the screen
    pygame.display.update()