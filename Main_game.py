import pygame as pg


def main():
    # Billeder som bliver brugt igennem koden
    veg = pg.image.load("Vegeta.png")
    goku = pg.image.load("Goku.png")
    back = pg.image.load("Possible_background.jpg")

    gbeam = pg.image.load("Blast.png")
    vbeam = pg.image.load("Blast_reverse.png")

    # Skærmens størrelse
    screen = pg.display.set_mode((1000, 600))
    font = pg.font.Font(None, 32)
    clock = pg.time.Clock()

    # Input kassens størrelse, samt nogle andre værdier der bruges til kassen
    input_box = pg.Rect(400, 200, 140, 32)
    color_inactive = pg.Color('red')
    color_active = pg.Color('red')
    color = color_inactive
    active = False
    text = ''
    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                # Hvis brugeren trykker på input kassen
                if input_box.collidepoint(event.pos):
                    # Kassen bliver aktiv, så man kan skrive i den
                    active = not active
                else:
                    active = False
                # Farven på kassen ændre sig, så det er nemmere at se man kan skrive i den
                color = color_active if active else color_inactive
            if event.type == pg.KEYDOWN:
                if active:
                    # Hvis man trykker [ENTER], så printer den teksten og sletter alt i kassen
                    if event.key == pg.K_RETURN:
                        print(text)
                        text = ''
                    # Hvis man trykker [BACKSPACE], så sletter man det seneste tilføjede bogstav/tal
                    elif event.key == pg.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill((30, 30, 30))
        # Den render den nuværende tekst
        txt_surface = font.render(text, True, color)
        # Den gør kassen større hvis der står for meget tekst i den
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        screen.blit(back, (0,0))
        # Den blitter teksten
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Den blitter input kassen.
        pg.draw.rect(screen, color, input_box, 2)

        pg.display.flip()
        clock.tick(30)

        # Funktionen for heltens angreb
        def gshot():
            screen.blit(gbeam, (200, 500))
            
        # Funktionen for skurkens angreb
        def vshot():
            screen.blit(vbeam, (200, 485))

if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
