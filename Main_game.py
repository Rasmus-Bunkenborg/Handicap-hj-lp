import math
import pygame



veg = pygame.image.load("Vegeta.png")
goku = pygame.image.load("Goku.png")
back = pygame.image.load("Possible_background.jpg")

gbeam = pygame.image.load("Blast.png")
vbeam = pygame.image.load("Blast_reverse.png")



def main():
    pygame.init()
    gameDisplay = pygame.display.set_mode((1000,600))

    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break
        def gshot():
            gameDisplay.blit(gbeam, (200, 500))

        def vshot():
            gameDisplay.blit(vbeam, (200, 485))
            
        gameDisplay.fill((255, 255, 255))

        gameDisplay.blit(back, (0, 0))

        gameDisplay.blit(goku, (150, 480))

        gameDisplay.blit(veg, (680, 480))

        pygame.display.flip()

    pygame.quit()


main()

