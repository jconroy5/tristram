import pygame
import sys
import os
import Character
import Objects

from Character import Player, Enemy
from Objects import Shell

BLACK = (  0,   0,   0)
GREEN = (  0, 170, 100)
WHITE = (255, 255, 255)

TITLE = "75mm"
WIN_HEIGHT = 900
WIN_WIDTH = 900

game_dir = os.path.dirname(__file__)
#__
assets_dir = os.path.join(game_dir, "Assets")
#____
images_dir = os.path.join(assets_dir, "Images")
#______
sherman_b_u = os.path.join(images_dir, "Sherman Body_u.png")
sherman_b_ul = os.path.join(images_dir, "Sherman Body_ul.png")
sherman_b_ur = os.path.join(images_dir, "Sherman Body_ur.png")
sherman_b_l = os.path.join(images_dir, "Sherman Body_l.png")
sherman_b_r = os.path.join(images_dir, "Sherman Body_r.png")
sherman_b_d = os.path.join(images_dir, "Sherman Body_d.png")
sherman_b_dl = os.path.join(images_dir, "Sherman Body_dl.png")
sherman_b_dr = os.path.join(images_dir, "Sherman Body_dr.png")

sherman_h_u = os.path.join(images_dir, "Sherman Head_u.png")
sherman_h_ul = os.path.join(images_dir, "Sherman Head_ul.png")
sherman_h_ur = os.path.join(images_dir, "Sherman Head_ur.png")
sherman_h_l = os.path.join(images_dir, "Sherman Head_l.png")
sherman_h_r = os.path.join(images_dir, "Sherman Head_r.png")
sherman_h_d = os.path.join(images_dir, "Sherman Head_d.png")
sherman_h_dl = os.path.join(images_dir, "Sherman Head_dl.png")
sherman_h_dr = os.path.join(images_dir, "Sherman Head_dr.png")
#____
music_dir = os.path.join(assets_dir, "Music")
#______
intro_song = os.path.join(music_dir, "bensound-epic.mp3")
# ******************************************************************************** #
def main():
    pygame.init()

    game_window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_caption(TITLE)
    #**************************GAME*LOOP*********************************#
    while True:
        show_start_screen(game_window)

        game_window.fill(WHITE)
        game_sprites = pygame.sprite.Group()
        sherman = Player(WIN_WIDTH, WIN_HEIGHT, pygame.image.load(sherman_b_d).convert_alpha())
        game_sprites.add(sherman)
        sherman_head = Player(WIN_WIDTH, WIN_HEIGHT, pygame.image.load(sherman_h_d).convert_alpha())
        game_sprites.add(sherman_head)
        game_sprites.update()
        game_sprites.draw(game_window)
        pygame.display.update()

        W_Down = False
        A_Down = False
        S_Down = False
        D_Down = False

        UA_Down = False
        LA_Down = False
        DA_Down = False
        RA_Down = False

        is_Shooting = False

        while True:
            for event in pygame.event.get():
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
                    if event.key == pygame.K_UP:
                        UA_Down = True
                    if event.key == pygame.K_LEFT:
                        LA_Down = True
                    if event.key == pygame.K_DOWN:
                        DA_Down = True
                    if event.key == pygame.K_RIGHT:
                        RA_Down = True
                    if event.key == pygame.K_SPACE:
                        is_Shooting = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        W_Down = False
                    if event.key == pygame.K_a:
                        A_Down = False
                    if event.key == pygame.K_s:
                        S_Down = False
                    if event.key == pygame.K_d:
                        D_Down = False
                    if event.key == pygame.K_UP:
                        UA_Down = False
                    if event.key == pygame.K_LEFT:
                        LA_Down = False
                    if event.key == pygame.K_DOWN:
                        DA_Down = False
                    if event.key == pygame.K_RIGHT:
                        RA_Down = False
                    if event.key == pygame.K_SPACE:
                        is_Shooting = False
#******************* 8-point Movement*********************************
#***********************BODY***************************
            if W_Down:
                if A_Down:
                    sherman.y -= sherman.speed
                    sherman.x -= sherman.speed
                    sherman.image = pygame.image.load(sherman_b_ul).convert_alpha()
                elif D_Down:
                    sherman.y -= sherman.speed
                    sherman.x += sherman.speed
                    sherman.image = pygame.image.load(sherman_b_ur).convert_alpha()
                else:
                    sherman.y -= sherman.speed
                    sherman.image = pygame.image.load(sherman_b_u).convert_alpha()
            elif S_Down:
                if A_Down:
                    sherman.y += sherman.speed
                    sherman.x -= sherman.speed
                    sherman.image = pygame.image.load(sherman_b_dl).convert_alpha()
                elif D_Down:
                    sherman.y += sherman.speed
                    sherman.x += sherman.speed
                    sherman.image = pygame.image.load(sherman_b_dr).convert_alpha()
                else:
                    sherman.y += sherman.speed
                    sherman.image = pygame.image.load(sherman_b_d).convert_alpha()
            elif A_Down:
                sherman.x -= sherman.speed
                sherman.image = pygame.image.load(sherman_b_l).convert_alpha()
            elif D_Down:
                sherman.x += sherman.speed
                sherman.image = pygame.image.load(sherman_b_r).convert_alpha()
#***********************HEAD***************************
            if UA_Down:
                if LA_Down:
                    sherman_head.image = pygame.image.load(sherman_h_ul).convert_alpha()
                elif RA_Down:
                    sherman_head.image = pygame.image.load(sherman_h_ur).convert_alpha()
                else:
                    sherman_head.image = pygame.image.load(sherman_h_u).convert_alpha()
            elif DA_Down:
                if LA_Down:
                    sherman_head.image = pygame.image.load(sherman_h_dl).convert_alpha()
                elif RA_Down:
                    sherman_head.image = pygame.image.load(sherman_h_dr).convert_alpha()
                else:
                    sherman_head.image = pygame.image.load(sherman_h_d).convert_alpha()
            elif LA_Down:
                sherman_head.image = pygame.image.load(sherman_h_l).convert_alpha()
            elif RA_Down:
                sherman_head.image = pygame.image.load(sherman_h_r).convert_alpha()
#******************* 8-point Movement*********************************
            if is_Shooting:
                shoot()

            game_window.fill(WHITE)
            game_window.blit(sherman.image, (sherman.x, sherman.y))
            game_window.blit(sherman_head.image, (sherman.x, sherman.y))
            pygame.display.update()



    #*******************************************************************#
def show_start_screen(window):
    title_text = "Press -SPACE- to begin"

    window.fill(BLACK)
    pygame.display.update()
    pygame.mixer.init()
    pygame.mixer.music.load(intro_song)
    pygame.mixer.music.play()
    textRender(window, TITLE, 300, WIN_WIDTH / 2, 50, WHITE)
    textRender(window, title_text, 60, WIN_WIDTH / 2, WIN_HEIGHT - 45, WHITE)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.stop()
                    return
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

def shoot():
    return

def textRender(surface, text, size, x, y, color):
    font_match = pygame.font.match_font('terminal')
    font = pygame.font.Font(font_match, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)
    pygame.display.update()
    # textRender from COMP 388 notes, draws text on screen

main()
