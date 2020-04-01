import math
import pygame

pygame.init()

gameDisplay = pygame.display.set_mode((1000,600))
penguinImage = pygame.image.load()


finished = False
while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    pygame.display.flip()
pygame.Quit()