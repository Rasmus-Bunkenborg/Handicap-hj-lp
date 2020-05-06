import pygame as pg

def main():
    veg = pg.image.load("Vegeta.png")
    goku = pg.image.load("Goku.png")
    back = pg.image.load("Possible_background.jpg")

    gbeam = pg.image.load("Blast.png")
    vbeam = pg.image.load("Blast_reverse.png")
    screen = pg.display.set_mode((1000, 600))
    font = pg.font.Font(None, 32)
    clock = pg.time.Clock()
    input_box = pg.Rect(400, 200, 140, 32)
    color_inactive = pg.Color('red')
    color_active = pg.Color('pink')
    color = color_inactive
    active = False
    text = ''
    done = False
            
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pg.KEYDOWN:
                if active:
                    if event.key == pg.K_RETURN:
                        print(text)
                        text = ''
                    elif event.key == pg.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill((30, 30, 30))
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        screen.blit(back, (0,0))
        # Blit the right character
        screen.blit(goku, (150, 480))
        # Blit the left character
        screen.blit(veg, (680, 480))
        
        def gshot():
            screen.blit(gbeam, (200, 500))

        def vshot():
            screen.blit(vbeam, (200, 485))
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pg.draw.rect(screen, color, input_box, 2)
        
        pg.display.flip()
        clock.tick(30)
        
if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()

