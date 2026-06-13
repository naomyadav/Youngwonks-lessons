import pygame
import random

class Shape:
    def __init__(self, radius, x, y, color):
        self.radius = radius
        self.x = x
        self.y = y
        self.color = color

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Colors!")
screen.fill((255, 255, 255))

shape1 = Shape(
    random.randint(20, 100), 
    random.randint(100, 700),  
    random.randint(100, 500),  
    (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
)

shape2 = Shape(
    random.randint(20, 100), 
    random.randint(100, 700), 
    random.randint(100, 500), 
    (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
)

shape3 = Shape(
    random.randint(20, 100), 
    random.randint(100, 700), 
    random.randint(100, 500), 
    (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
)

shape1.draw(screen)
shape2.draw(screen)
shape3.draw(screen)

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
