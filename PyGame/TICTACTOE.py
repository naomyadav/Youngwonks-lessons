import pygame
from pygame.locals import * 
from time import sleep
from tkinter import messagebox
def draw_x(x,y):
    pygame.draw.line(screen,(255,255,255),(x+50,y+50),(x-50,y-50),5)
    pygame.draw.line(screen,(255,255,255),(x+50,y-50),(x-50,y+50),5)
def draw_o(x,y):
    pygame.draw.circle(screen,(255,255,255),(x,y),50.0,5)

pygame.init()
screen = pygame.display.set_mode((601,601))
pygame.display.set_caption("Colors!!")
TURN="x"
squares={"1":"","2":"","3":"","4":"","5":"","6":"","7":"","8":"","9":""}
TURN_NUM=0
while True:
    #screen.fill((56,75,198))
    pygame.draw.line(screen,(254,1,254),(200,0),(200,600))
    pygame.draw.line(screen,(254,1,254),(0,200),(600,200))
    pygame.draw.line(screen,(254,1,254),(0,400),(600,400))
    pygame.draw.line(screen,(254,1,254),(400,0),(400,600))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            break
            exit()
        if event.type==MOUSEBUTTONDOWN:
            x,y = event.pos
            #1,1-
            if x in range(0,200) and y in range(0,200) and squares["1"]=="":
                if TURN=="x":
                    draw_x(100,100)
                    squares["1"]="x"
                    TURN="o"
                    TURN_NUM+=1
                elif TURN=="o":
                    draw_o(100,100)
                    squares["1"]="o"
                    TURN="x"
                    TURN_NUM+=1
            #1,2-
            if x in range(200,400) and y in range(0,200) and squares["2"]=="":
                if TURN=="x":
                    draw_x(300,100)
                    squares["2"]="x"
                    TURN="o"
                    TURN_NUM+=1
                elif TURN=="o":
                    draw_o(300,100)
                    squares["2"]="o"
                    TURN="x"
                    TURN_NUM+=1
            #1,3-
            if x in range(400,600) and y in range(0,200) and squares["3"]=="":
                if TURN=="x":
                    draw_x(500,100)
                    squares["3"]="x"
                    TURN="o"
                    TURN_NUM+=1
                elif TURN=="o":
                    draw_o(500,100)
                    squares["3"]="o"
                    TURN="x"
                    TURN_NUM+=1
            #2,1-
            if x in range(0,200) and y in range(200,400) and squares["4"]=="":
                if TURN=="x":
                    draw_x(100,300)
                    squares["4"]="x"
                    TURN="o"
                    TURN_NUM+=1
                elif TURN=="o":
                    draw_o(100,300)
                    squares["4"]="o"
                    TURN="x"
                    TURN_NUM+=1
            #2,2-
            if x in range(200,400) and y in range(200,400) and squares["5"]=="":
                if TURN=="x":
                    draw_x(300,300)
                    squares["5"]="x"
                    TURN="o"
                    TURN_NUM+=1
                elif TURN=="o":
                    draw_o(300,300)
                    squares["5"]="o"
                    TURN="x"
                    TURN_NUM+=1
            #2,3-
            if x in range(400,600) and y in range(200,400) and squares["6"]=="":
                if TURN=="x":
                    draw_x(500,300)
                    squares["6"]="x"
                    TURN="o"
                    TURN_NUM+=1
                elif TURN=="o":
                    draw_o(500,300)
                    squares["6"]="o"
                    TURN="x"
                    TURN_NUM+=1
            #3,1-
            if x in range(0,200) and y in range(400,600) and squares["7"]=="":
                if TURN=="x":
                    draw_x(100,500)
                    squares["7"]="x"
                    TURN="o"
                    TURN_NUM+=1
                elif TURN=="o":
                    draw_o(100,500)
                    squares["7"]="o"
                    TURN="x"
                    TURN_NUM+=1
            #3,2-
            if x in range(200,400) and y in range(400,600) and squares["8"]=="":
                if TURN=="x":
                    draw_x(300,500)
                    squares["8"]="x"
                    TURN="o"
                    TURN_NUM+=1
                elif TURN=="o":
                    draw_o(300,500)
                    squares["8"]="o"
                    TURN="x"
                    TURN_NUM+=1
            #3,3-
            if x in range(400,600) and y in range(400,600) and squares["9"]=="":
                if TURN=="x":
                    draw_x(500,500)
                    squares["9"]="x"
                    TURN="o"
                    TURN_NUM+=1
                elif TURN=="o":
                    draw_o(500,500)
                    squares["9"]="o"
                    TURN="x"
                    TURN_NUM+=1
        
    
    if squares["1"] == squares["2"] == squares["3"] != "":
        print(squares["1"]+" WON!",squares["1"]+" WON!")
        pygame.display.update()
        sleep(1);break
    elif squares["4"] == squares["5"] == squares["6"] != "":
        print(squares["4"]+" WON!",squares["4"]+" WON!")
        pygame.display.update()
        sleep(1);break
    elif squares["7"] == squares["8"] == squares["9"] != "":
        print(squares["7"]+" WON!",squares["7"]+" WON!")
        pygame.display.update()
        sleep(1);break
    elif squares["1"] == squares["4"] == squares["7"] != "":
        print(squares["1"]+" WON!",squares["1"]+" WON!")
        pygame.display.update()
        sleep(1);break
    elif squares["2"] == squares["5"] == squares["8"] != "":
        print(squares["2"]+" WON!",squares["2"]+" WON!")
        pygame.display.update()
        sleep(1);break
    elif squares["3"] == squares["6"] == squares["9"] != "":
        print(squares["3"]+" WON!",squares["3"]+" WON!")
        pygame.display.update()
        sleep(1);break
    elif squares["1"]==squares["5"]==squares["9"]!="":
        print(squares["1"]+" WON!",squares["1"]+" WON!")
        pygame.display.update()
        sleep(1);break
    elif squares["3"]==squares["5"]==squares["7"]!="":
        print(squares["1"]+" WON!",squares["1"]+" WON!")
        pygame.display.update()
        sleep(1);break
    elif TURN_NUM>=9:
        print("DRAW")
        pygame.display.update()
        sleep(1);break
    pygame.display.update()