import pygame
import sys
import os
import Character
import Objects

from Character import Player, Enemy
from Objects import Shell

BLACK = (  0,   0,   0)
GREEN = (  0, 170, 100)
RED   = (200,   0,   0)
PURPLE= (170,   0, 100)
WHITE = (255, 255, 255)

TITLE = "75mm"
WIN_HEIGHT = 900
WIN_WIDTH = 900

#*********************GAME DIRECTORY****************************
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

panzer_no_t = os.path.join(images_dir, "Panzer 2-layer head and body.png")

opening_background = os.path.join(images_dir, "Sherman_tank_and_Horsa_glider_900x907.png")

background_b_1a = os.path.join(images_dir, "background_beach-1.png")
background_b_2a = os.path.join(images_dir, "background_beach-2.png")
background_b_3a = os.path.join(images_dir, "background_beach-3.png")
background_b_4a = os.path.join(images_dir, "background_beach-4.png")
background_b_5a = os.path.join(images_dir, "background_beach-5.png")
background_b_6a = os.path.join(images_dir, "background_beach-6.png")
background_b_7a = os.path.join(images_dir, "background_beach-7.png")

background_cs_1 = os.path.join(images_dir, "background_square.png")

#____
music_dir = os.path.join(assets_dir, "Music")
#______
intro_song = os.path.join(music_dir, "bensound-epic.mp3")
war_sounds = os.path.join(music_dir, "war_sounds.mp3")
#*********************GAME DIRECTORY****************************

# ******************************************************************************** #
def main():
    pygame.init()
    pygame.mixer.init()

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
        W_Down = False
        A_Down = False
        S_Down = False
        D_Down = False

        UA_Down = False
        LA_Down = False
        DA_Down = False
        RA_Down = False

        is_Shooting = False

        opening_bg = pygame.image.load(opening_background).convert_alpha()

        intro_map = pygame.image.load(background_b_1a).convert_alpha()
        im2 = pygame.image.load(background_b_2a).convert_alpha()
        im3 = pygame.image.load(background_b_3a).convert_alpha()
        im4 = pygame.image.load(background_b_4a).convert_alpha()
        im5 = pygame.image.load(background_b_5a).convert_alpha()
        im6 = pygame.image.load(background_b_6a).convert_alpha()
        im7 = pygame.image.load(background_b_7a).convert_alpha()

        city_square = pygame.image.load(background_cs_1).convert_alpha()
        city_north = 1
        city_east = 2
        city_west = 3

        just_entered = False

        current_map = intro_map

        counter = 0
        speed = 200

        show_start_screen(game_window, opening_bg)

        game_window.fill(BLACK)

        game_sprites = pygame.sprite.Group()
        allies = pygame.sprite.Group()
        axis = pygame.sprite.Group()
        game_sprites.add(allies)
        game_sprites.add(axis)

        sherman = Player(WIN_WIDTH, WIN_HEIGHT, pygame.image.load(sherman_b_d).convert_alpha())
        allies.add(sherman)
        sherman_head = Player(WIN_WIDTH, WIN_HEIGHT, pygame.image.load(sherman_h_d).convert_alpha())
        allies.add(sherman_head)

        panzer = Enemy(WIN_WIDTH, WIN_HEIGHT, pygame.image.load(panzer_no_t).convert_alpha())
        axis.add(panzer)

        game_sprites.update()

        player_shells = pygame.sprite.Group()

        pygame.mixer.music.load(war_sounds)
        pygame.mixer.music.play(-1)

        game_window.blit(sherman.image, (sherman.x, sherman.y))
        game_window.blit(sherman_head.image, (sherman.x, sherman.y))
        game_window.blit(current_map, (0,0))
        pygame.display.update()

        while True:

            TRANS_U = False
            TRANS_R = False
            TRANS_L = False
            TRANS_D = False
            canTrans = True

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
            angle = 0.0
            if UA_Down:
                if LA_Down:
                    sherman_head.image = shul
                    angle = 1.5
                elif RA_Down:
                    sherman_head.image = shur
                    angle = 2.5
                else:
                    sherman_head.image = shu
                    angle = 2.0
            elif DA_Down:
                if LA_Down:
                    sherman_head.image = shdl
                    angle = 4.5
                elif RA_Down:
                    sherman_head.image = shdr
                    angle = 3.5
                else:
                    sherman_head.image = shd
                    angle = 4.0
            elif LA_Down:
                sherman_head.image = shl
                angle = 1.0
            elif RA_Down:
                sherman_head.image = shr
                angle = 3.0

#******************MAP BOUNDS************************
            if sherman.x < 0:
                sherman.x = 0
            if sherman.x > 780:
                sherman.x = 780
            if sherman.y < 0:
                sherman.y = 0
            if sherman.y > 780:
                sherman.y = 780
#******************* 8-point Movement*********************************

#******************* MAP HANDLING*********************************
            if sherman.x >= 0 and sherman.x <= 10 and sherman.y >= 300 and sherman.y <= 500:
                TRANS_L = True
            if sherman.x >= 300 and sherman.x <= 500 and sherman.y >= 0 and sherman.y <= 10:
                TRANS_U = True
            if sherman.x >= 770 and sherman.x <= 780 and sherman.y >= 300 and sherman.y <= 500:
                TRANS_R = True
            if sherman.x >= 300 and sherman.x <= 500 and sherman.y >= 770 and sherman.y <= 780:
                TRANS_D = True


#******************* INTRO_MAP ANIMATED ***********************
            game_window.fill(BLACK) #flicker to clean screen

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

                if just_entered:
                    if sherman.x >= 300 and sherman.x <= 500 and sherman.y >= 0 and sherman.y <= 10:
                        canTrans = False
                    else:
                        canTrans = True
                        just_entered = False


                if TRANS_U == True and canTrans:
                    current_map = city_square
                    sherman.y = 900
                    just_entered = True
                    pygame.mixer.music.pause()
#****************************************************************
            elif current_map == city_square:
                game_window.blit(city_square, (0,0))
                game_window.blit(panzer.image, (panzer.x, panzer.y))

                if just_entered:
                    if sherman.x >= 0 and sherman.x <= 10 and sherman.y >= 300 and sherman.y <= 500:
                        canTrans = False
                    elif sherman.x >= 300 and sherman.x <= 500 and sherman.y >= 0 and sherman.y <= 10:
                        canTrans = False
                    elif sherman.x >= 770 and sherman.x <= 780 and sherman.y >= 300 and sherman.y <= 500:
                        canTrans = False
                    elif sherman.x >= 300 and sherman.x <= 500 and sherman.y >= 770 and sherman.y <= 780:
                        canTrans = False
                    else:
                        canTrans = True
                        just_entered = False

                if TRANS_D == True and canTrans:
                    current_map = intro_map
                    sherman.y = 0
                    just_entered = True
                    pygame.mixer.music.load(war_sounds)
                    pygame.mixer.music.play(-1)
                elif TRANS_L == True and canTrans:
                    current_map = city_west
                    sherman.x = 900
                    just_entered = True
                elif TRANS_R == True and canTrans:
                    current_map = city_east
                    sherman.x = 0
                    just_entered = True
                elif TRANS_U == True and canTrans:
                    current_map = city_north
                    sherman.y = 900
                    just_entered = True
#****************************************************************
            elif current_map == city_east:
                game_window.fill(GREEN)

                if just_entered:
                    if sherman.x >= 0 and sherman.x <= 10 and sherman.y >= 300 and sherman.y <= 500:
                        canTrans = False
                    else:
                        canTrans = True
                        just_entered = False

                if TRANS_L == True and canTrans:
                    current_map = city_square
                    sherman.x = 900
                    just_entered = True
#****************************************************************
            elif current_map == city_west:
                game_window.fill(RED)

                if just_entered:
                    if sherman.x >= 770 and sherman.x <= 780 and sherman.y >= 300 and sherman.y <= 500:
                        canTrans = False
                    else:
                        canTrans = True
                        just_entered = False

                if TRANS_R == True:
                    current_map = city_square
                    sherman.x = 0
                    just_entered = True
#****************************************************************
            elif current_map == city_north:
                game_window.fill(PURPLE)

                if just_entered:
                    if sherman.x >= 300 and sherman.x <= 500 and sherman.y >= 770 and sherman.y <= 780:
                        canTrans = False
                    else:
                        canTrans = True
                        just_entered = False

                if TRANS_D == True and canTrans:
                    current_map = city_square
                    sherman.y = 0
                    just_entered = True

#***************************************************************************
            game_window.blit(sherman.image, (sherman.x, sherman.y))
            game_window.blit(sherman_head.image, (sherman.x, sherman.y))
            pygame.display.update()


#**************************GAME*LOOP*********************************#

#*******************************************************************#
def show_start_screen(window, image):
    title_text = "Press -SPACE- to begin"

    window.fill(BLACK)
    window.blit(image, (0, 0))
    pygame.display.update()
    pygame.mixer.music.load(intro_song)
    pygame.mixer.music.play(loops = -1)
    textRender(window, TITLE, 300, WIN_WIDTH / 2, 50, WHITE)
    textRender(window, title_text, 60, WIN_WIDTH / 2, WIN_HEIGHT - 60, WHITE)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.pause()
                    return
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

def textRender(surface, text, size, x, y, color):
    font_match = pygame.font.match_font('stencil')
    font = pygame.font.Font(font_match, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)
    pygame.display.update()
    # textRender from COMP 388 notes, draws text on screen


main()
