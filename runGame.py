import pygame
import sys
import Character

from Character import Player, Enemy

BLACK = (  0,   0,   0)
GREEN = (  0, 170, 100)
WHITE = (255, 255, 255)

TITLE = "Tristram"
WIN_HEIGHT = 576
WIN_WIDTH = 1024
# ******************************************************************************** #
def main():
    pygame.init()

    game_window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_caption(TITLE)

    show_start_screen(game_window)


def show_start_screen(window):
    title_text = "Press -SPACE- to begin"

    window.fill(BLACK)
    pygame.display.update()
    textRender(window, title_text, 60, WIN_WIDTH / 2, WIN_HEIGHT - 40)

    events = pygame.event.get()
    while True:
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_SPACE:
                    return
                if event.type == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()


def playerMove

def textRender(surface, text, size, x, y):
    font_match = pygame.font.match_font('terminal')
    font = pygame.font.Font(font_match, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)
    pygame.display.update()
    # textRender from COMP 388 notes, draws text on screen

main()
