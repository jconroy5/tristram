import pygame

class Shell(pygame.sprite.Sprite):
    def __init__(coor_x, coor_y, color):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 1.0
        self.image = pygame.Surface((5, 5))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (coor_x, coor_y)
        self.x = coor_x
        self.y = coor_y

    def UP(self):
        self.y -= self.speed
    def UPRI(self):
        self.y -= self.speed
        self.x += self.speed
    def UPLE(self):
        self.y -= self.speed
        self.x -= self.speed
    def LE(self):
        self.x -= self.speed
    def RI(self):
        self.x += self.speed
    def DO(self):
        self.y += self.speed
    def DORI(self):
        self.y += self.speed
        self.x += self.speed
    def DOLE(self):
        self.y += self.speed
        self.x -= self.speed
