from pygame.locals import *
import pygame
pygame.init()
# def show_text(msg, x, y, color, size):
#         fontobj= pygame.font.SysFont("freesans", size)
#         msgobj = fontobj.render(msg,False,color)
#         screen.blit(msgobj,(x, y))
screen = pygame.display.set_mode((504,504))
pygame.display.set_caption("Shapes!!")
evlc=(0,0)
flg=False
while True:
    
    

    for event in pygame.event.get():
        # show_text("Test",252,252,(255,255,255),100)
        if event.type == MOUSEBUTTONDOWN:
            flg=True
        if event.type== MOUSEBUTTONUP:
            flg=False
        if event.type == MOUSEMOTION:
            if flg:
                evlc=event.pos
                pygame.draw.circle(screen,(255,0,0),evlc,20)
        if event.type == QUIT:
            pygame.quit()
            exit()
        
    
    pygame.display.update()