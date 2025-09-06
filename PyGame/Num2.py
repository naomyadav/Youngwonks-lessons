from pygame.locals import *
import pygame
pygame.init()
def show_text(msg, x, y, color, size):
        fontobj= pygame.font.SysFont("freesans", size)
        msgobj = fontobj.render(msg,False,color)
        screen.blit(msgobj,(x, y))
screen = pygame.display.set_mode((504,504))
pygame.display.set_caption("Shapes!!")
while True:
    for event in pygame.event.get():
        show_text("Test",252,252,(255,255,255),100)
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()