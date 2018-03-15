import pygame, importlib

class Character:
    #Base class for player character

    window = pygame.display.set_mode((800, 600))

    def __init__(self, hp, speed, damage):
        self.hp = 3.0
        self.speed = 1.0
        self.damage = 1.0

    def drawCharacter(self):
        pygame.draw.rect(window, WHITE, (200, 200, 100, 50))
