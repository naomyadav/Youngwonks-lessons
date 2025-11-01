import pygame
from pygame.locals import * 

def draw_x(x,y):
    pygame.draw.line(screen,(255,255,255),(x,y),(x+50,y+50),5)
    pygame.draw.line(screen,(255,255,255),(x+50,y),(x,y+50),5)
def draw_o(x,y):
    pygame.draw.circle(screen,(255,255,255),(x+25,y+25),50.0,5)
    
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Colors!!")
TURN="x"
while True:
    #screen.fill((56,75,198))
    pygame.draw.line(screen,(254,1,254),(200,0),(200,600))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type==MOUSEBUTTONUP:
            if TURN=="x":
                draw_x(event.pos[0],event.pos[1])
                TURN="o"
            elif TURN=="o":
                draw_o(event.pos[0],event.pos[1])
                TURN="x"
        
    pygame.display.update()