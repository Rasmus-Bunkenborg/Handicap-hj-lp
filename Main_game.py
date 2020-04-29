import math
import pygame


color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
veg = pygame.image.load("Vegeta.png")
goku = pygame.image.load("Goku.png")
back = pygame.image.load("Possible_background.jpg")
def main():
    pygame.init()
    gameDisplay = pygame.display.set_mode((1000,600))

    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break

        gameDisplay.fill((255, 255, 255))

        gameDisplay.blit(back, (0, 0))

        gameDisplay.blit(goku, (150, 480))

        gameDisplay.blit(veg, (750, 480))

        pygame.display.flip()

    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    font = pygame.font.Font(None, 32)
    clock = pygame.time.Clock()
    input_box = pygame.Rect(100, 100, 140, 32)
    color = color_inactive
    active = False
    text = ''
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        print(text)
                        text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        gameDisplay.fill((30, 30, 30))
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        gameDisplay.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pygame.draw.rect(gameDisplay, color, input_box, 2)

        pygame.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    pygame.init()
    main()
    pygame.quit()


    pygame.quit()


main()
