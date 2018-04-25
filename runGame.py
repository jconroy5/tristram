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
sherman_b_u = os.path.join(images_dir, "Sherman Body_u.png")
sherman_b_l = os.path.join(images_dir, "Sherman Body_l.png")
sherman_b_r = os.path.join(images_dir, "Sherman Body_r.png")
sherman_b_d = os.path.join(images_dir, "Sherman Body_d.png")
sherman_h_u = os.path.join(images_dir, "Sherman Head_u.png")
sherman_h_l = os.path.join(images_dir, "Sherman Head_l.png")
sherman_h_r = os.path.join(images_dir, "Sherman Head_r.png")
sherman_h_d = os.path.join(images_dir, "Sherman Head_d.png")
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

        game_window.fill(BLACK)
        game_sprites = pygame.sprite.Group()
        sherman = Player(WIN_WIDTH, WIN_HEIGHT, pygame.image.load(sherman_b_d).convert())
        game_sprites.add(sherman)
        game_sprites.update()
        game_sprites.draw(game_window)
        pygame.display.update()

        W_Down = False
        A_Down = False
        S_Down = False
        D_Down = False
        while True:
            events = pygame.event.set_repeat()
            for event in events.get_repeat():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_w:
                        W_Down = True
                    if event.key == pygame.K_a:
                        A_Down = True
                    if event.key == pygame.K_s:
                        S_Down = True
                    if event.key == pygame.K_d:
                        D_Down = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        W_Down = False
                    if event.key == pygame.K_a:
                        A_Down = False
                    if event.key == pygame.K_s:
                        S_Down = False
                    if event.key == pygame.K_d:
                        D_Down = False

                if W_Down:
                    sherman.y -= sherman.speed
                    sherman.image = pygame.image.load(sherman_b_u).convert()
                if A_Down:
                    sherman.x -= sherman.speed
                    sherman.image = pygame.image.load(sherman_b_l).convert()
                if S_Down:
                    sherman.y += sherman.speed
                    sherman.image = pygame.image.load(sherman_b_d).convert()
                if D_Down:
                    sherman.x += sherman.speed
                    sherman.image = pygame.image.load(sherman_b_r).convert()
                game_window.blit(sherman.image, (sherman.x, sherman.y))
                pygame.display.update()


    #*******************************************************************#
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
