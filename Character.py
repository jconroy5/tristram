<<<<<<< current
class Player(object):

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
=======
import pygame, importlib, runGame

class Character:
    #Base class for player character

    def __init__(self, hp, speed, damage):
        self.hp = 3.0
        self.speed = 1.0
        self.damage = 1.0

    def drawCharacter(self, window, color):
        pygame.draw.rect(window, color, (200, 200, 100, 50))
>>>>>>> before discard
