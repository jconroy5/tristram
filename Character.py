import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, winWidth, winHeight, color):
        pygame.sprite.Sprite._init_(self)
        self.image = pygame.Surface
        self.hp = 10.0
        self.speed = 1.0
        self.damage = 1.0
        self.image = pygame.Surface((30,30))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (winWidth / 2, winHeight / 2)

    def get_hp(self):
        return self.hp

    def get_speed(self):
        return self.speed

    def get_damage(self):
        return self.damage

    # def draw_set_player(window, x_rect, y_rect ):

    # def move_player(self, speed):

class Enemy(object):

    def __init__(self, hp, speed, damage):
        self.hp = hp
        self.speed = speed
        self.damage = damage

    def get_hp(self):
        return self.hp

    def get_speed(self):
        return self.speed

    def get_damage(self):
        return self.damage
