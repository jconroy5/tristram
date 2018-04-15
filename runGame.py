import pygame
import sys
import os
import Character

from Character import Player, Enemy

BLACK = (  0,   0,   0)
GREEN = (  0, 170, 100)
WHITE = (255, 255, 255)

TITLE = "75mm"
WIN_HEIGHT = 576
WIN_WIDTH = 1024

game_dir = os.path.dirname(__file__)
assets_dir = os.path.join(game_dir, "Assets")
images_dir = os.path.join(assets_dir, "Images")
music_dir = os.path.join(assets_dir, "Music")
intro_song = os.path.join(music_dir, "bensound-epic.mp3")
# ******************************************************************************** #
def main():
    pygame.init()

    game_window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_caption(TITLE)
    #**************************GAME*LOOP*********************************#
    while True:
        show_start_screen(game_window)

        game_sprites = pygame.sprite.Group()

    #*******************************************************************#
    pygame.quit()
    sys.exit()

def show_start_screen(window):
    title_text = "Press -SPACE- to begin"

    window.fill(BLACK)
    pygame.display.update()
    pygame.mixer.init()
    pygame.mixer.music.load(intro_song)
    pygame.mixer.music.play()
    textRender(window, TITLE, 300, WIN_WIDTH / 2, 50)
    textRender(window, title_text, 60, WIN_WIDTH / 2, WIN_HEIGHT - 45)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

#def draw_map(window):

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
