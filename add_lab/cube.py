import math

import pygame

WIDTH = 800
HEIGHT = 800
DISTANCE = 4
FOCAL = 600

vertices = [
    (-1, -1, 1), (-1, 1, 1), (1, 1, 1), (1, -1, 1),
    (-1, -1, -1), (-1, 1, -1), (1, 1, -1), (1, -1, -1),
]

edges = [(0, 1), (1, 2), (2, 3), (3, 0),
         (4, 5), (5, 6), (6, 7), (7, 4),
         (0, 4), (1, 5), (2, 6), (3, 7)]


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spinning Cube")

running = True
angle_x = angle_y = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (0, 255, 0), (400, 300), 150, 5)
    pygame.display.flip()
    
pygame.quit()