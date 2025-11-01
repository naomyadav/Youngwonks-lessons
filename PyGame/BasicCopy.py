import pygame
from pygame.locals import * 



pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("Colors!!")
while True:
    screen.fill((56,75,198))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()