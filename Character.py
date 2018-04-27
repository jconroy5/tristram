import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, winWidth, winHeight, image):
        pygame.sprite.Sprite.__init__(self)
        self.hp = 10.0
        self.speed = 0.5
        self.damage = 1.0
        self.image = image
        self.rect = self.image.get_rect()
        self.x = (winWidth / 2) - 61
        self.y = (winHeight / 2) - 61
        self.rect.center = (self.x + 61, self.y + 61)


    #def moveBody(self, direction):

    #def moveHead(self, direction):

    def get_hp(self):
        return self.hp

    def get_speed(self):
        return self.speed

    def get_damage(self):
        return self.damage

    # def draw_set_player(window, x_rect, y_rect ):

    # def move_player(self, speed):

class Enemy(pygame.sprite.Sprite):

    def __init__(self, winWidth, winHeight, image):
        pygame.sprite.Sprite.__init__(self)
        self.hp = 10.0
        self.speed = 0.5
        self.damage = 1.0
        self.image = image
        self.rect = self.image.get_rect()
        self.x = (winWidth / 2) - 61
        self.y = (winHeight / 2) - 61
        self.rect.center = (self.x + 61, self.y + 61)


    def get_hp(self):
        return self.hp

    def get_speed(self):
        return self.speed

    def get_damage(self):
        return self.damage
