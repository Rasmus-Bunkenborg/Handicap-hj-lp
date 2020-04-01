import math
import pygame
import random




pygame.init()


gameDisplay = pygame.display.set_mode((1000,600))


<<<<<<< Updated upstream
=======
def hitMissText():
    font = pygame.font.SysFont("comicsansms", 72)
    textHit = font.render("You hit!", False, (84, 194, 45))
    textMiss = font.render("You missed!", False, (163, 41, 33))
    
def asdasd():
    if textHit == True:
        screen.blit(textHit, (display_x/2, display_y/2))
    if textMiss == True:
        screen.blit(textMiss, (display_x/2, display_y/2))
        
rand = (random.randrange(1, 3))
if rand == 1:
    textHit = True
    textMiss = False
    asdasd()
if rand == 2:
    textHit = False
    textMiss = True
    asdasd()
>>>>>>> Stashed changes
