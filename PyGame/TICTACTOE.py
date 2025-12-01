import pygame
from pygame.locals import * 

def draw_x(x,y):
    pygame.draw.line(screen,(255,255,255),(x-50,y-50),(x+50,y+50),5)
    pygame.draw.line(screen,(255,255,255),(x+50,y-50),(x-50,y+50),5)
def draw_o(x,y):
    pygame.draw.circle(screen,(255,255,255),(x,y),50.0,5)
    
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Colors!!")
TURN="x"
squares={1:"",2:"",3:"",4:"",5:"",6:"",7:"",8:"",9:""}
while True:
    #screen.fill((56,75,198))
    pygame.draw.line(screen,(254,1,254),(200,0),(200,600))
    pygame.draw.line(screen,(254,1,254),(400,0),(400,600))
    pygame.draw.line(screen,(254,1,254),(0,200),(600,200))
    pygame.draw.line(screen,(254,1,254),(0,400),(600,400))    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type==MOUSEBUTTONDOWN:
            x,y=event.pos
            if x in range(0,200) and y in range(0,200) and squares[1]=="":
                if TURN=="x":
                    draw_x(100,100)
                    squares[1]="x"
                    TURN="y"
                elif TURN=="y":
                    draw_o(100,100)
                    squares[1]="y"
                    TURN="x"
            elif x in range(200,400) and y in range(0,200) and squares[2]=="":
                if TURN=="x":
                    draw_x(300,100)
                    squares[2]="x"
                    TURN="y"
                elif TURN=="y":
                    draw_o(300,100)
                    squares[2]="y"
                    TURN="x"
            elif x in range(400,600) and y in range(400,600) and squares[2]=="":
                if TURN=="x":
                    draw_x(300,100)
                    squares[2]="x"
                    TURN="y"
                elif TURN=="y":
                    draw_o(300,100)
                    squares[2]="y"
                    TURN="x"


    """ 
    if TURN=="x":
                draw_x(event.pos[0],event.pos[1])
                TURN="o"
            elif TURN=="o":
                draw_o(event.pos[0],event.pos[1])
                TURN="x"    
                """
    pygame.display.update()