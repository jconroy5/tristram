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

background_b_1a = os.path.join(images_dir, "background_beach-1.png")
background_b_2a = os.path.join(images_dir, "background_beach-2.png")
background_b_3a = os.path.join(images_dir, "background_beach-3.png")
background_b_4a = os.path.join(images_dir, "background_beach-4.png")
background_b_5a = os.path.join(images_dir, "background_beach-5.png")
background_b_6a = os.path.join(images_dir, "background_beach-6.png")
background_b_7a = os.path.join(images_dir, "background_beach-7.png")
#____
music_dir = os.path.join(assets_dir, "Music")
#______
intro_song = os.path.join(music_dir, "bensound-epic.mp3")
war_sounds = os.path.join(music_dir, "war_sounds.mp3")
# ******************************************************************************** #
def main():
    pygame.init()

    game_window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_caption(TITLE)

    timer = pygame.time.get_ticks

    sbu = pygame.image.load(sherman_b_u).convert_alpha()
    sbul = pygame.image.load(sherman_b_ul).convert_alpha()
    sbur = pygame.image.load(sherman_b_ur).convert_alpha()
    sbl = pygame.image.load(sherman_b_l).convert_alpha()
    sbr = pygame.image.load(sherman_b_r).convert_alpha()
    sbd = pygame.image.load(sherman_b_d).convert_alpha()
    sbdl = pygame.image.load(sherman_b_dl).convert_alpha()
    sbdr = pygame.image.load(sherman_b_dr).convert_alpha()

    shu = pygame.image.load(sherman_h_u).convert_alpha()
    shul = pygame.image.load(sherman_h_ul).convert_alpha()
    shur = pygame.image.load(sherman_h_ur).convert_alpha()
    shl = pygame.image.load(sherman_h_l).convert_alpha()
    shr = pygame.image.load(sherman_h_r).convert_alpha()
    shd = pygame.image.load(sherman_h_d).convert_alpha()
    shdl = pygame.image.load(sherman_h_dl).convert_alpha()
    shdr = pygame.image.load(sherman_h_dr).convert_alpha()
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

        intro_map = pygame.image.load(background_b_1a).convert_alpha()
        im2 = pygame.image.load(background_b_2a).convert_alpha()
        im3 = pygame.image.load(background_b_3a).convert_alpha()
        im4 = pygame.image.load(background_b_4a).convert_alpha()
        im5 = pygame.image.load(background_b_5a).convert_alpha()
        im6 = pygame.image.load(background_b_6a).convert_alpha()
        im7 = pygame.image.load(background_b_7a).convert_alpha()
        current_map = intro_map
        timer = 0
        counter = 0
        speed = 200
        pygame.mixer.init()
        pygame.mixer.music.load(war_sounds)
        pygame.mixer.music.play(-1)
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
                    sherman.image = sbul
                elif D_Down:
                    sherman.y -= sherman.speed
                    sherman.x += sherman.speed
                    sherman.image = sbur
                else:
                    sherman.y -= sherman.speed
                    sherman.image = sbu
            elif S_Down:
                if A_Down:
                    sherman.y += sherman.speed
                    sherman.x -= sherman.speed
                    sherman.image = sbdl
                elif D_Down:
                    sherman.y += sherman.speed
                    sherman.x += sherman.speed
                    sherman.image = sbdr
                else:
                    sherman.y += sherman.speed
                    sherman.image = sbd
            elif A_Down:
                sherman.x -= sherman.speed
                sherman.image = sbl
            elif D_Down:
                sherman.x += sherman.speed
                sherman.image = sbr
#***********************HEAD***************************
            if UA_Down:
                if LA_Down:
                    sherman_head.image = shul
                elif RA_Down:
                    sherman_head.image = shur
                else:
                    sherman_head.image = shu
            elif DA_Down:
                if LA_Down:
                    sherman_head.image = shdl
                elif RA_Down:
                    sherman_head.image = shdr
                else:
                    sherman_head.image = shd
            elif LA_Down:
                sherman_head.image = shl
            elif RA_Down:
                sherman_head.image = shr

            if sherman.x < 0:
                sherman.x = 0
            if sherman.x > 775:
                sherman.x = 775
            if sherman.y < 0:
                sherman.y = 0
            if sherman.y > 775:
                sherman.y = 775
#******************* 8-point Movement*********************************
            if is_Shooting:
                shoot()

            game_window.fill(WHITE)
            if current_map == intro_map:
                if counter < 100 and counter >= 0:
                    game_window.blit(intro_map, (0,0))
                    if counter == 0:
                        forward = True
                elif counter < 200 and counter >= 100:
                    game_window.blit(im2, (0,0))
                elif counter < 300 and counter >= 200:
                    game_window.blit(im3, (0,0))
                elif counter < 400 and counter >= 300:
                    game_window.blit(im4, (0,0))
                elif counter < 500 and counter >= 400:
                    game_window.blit(im5, (0,0))
                elif counter < 600 and counter >= 500:
                    game_window.blit(im6, (0,0))
                elif counter <= 700 and counter >= 600:
                    game_window.blit(im7, (0,0))
                    if counter == 700:
                        forward = False

                if forward:
                    counter += 1
                else:
                    counter -= 1
            else:
                game_window.blit(intro_map, (0,0))


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
    pygame.mixer.music.play(loops = -1)
    textRender(window, TITLE, 300, WIN_WIDTH / 2, 50, WHITE)
    textRender(window, title_text, 60, WIN_WIDTH / 2, WIN_HEIGHT - 45, WHITE)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.quit()
                    return
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.QUIT:
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
