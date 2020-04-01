import math
import pygame

pygame.init()

display_x = 1000
display_y = 600

gameDisplay = pygame.display.set_mode((display_x,display_y))

def message_display(text):
    hitText = pygame.font.Font('freesansbold.ttf', 75)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_x/2),(display_y))
