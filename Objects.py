import pygame

class Shell(pygame.sprite.Sprite):
    def __init__(self, coor_x, coor_y):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 0.5
        self.width = 6
        self.height = 10
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((200,200,200))
        self.rect = self.image.get_rect()
        self.x = coor_x - (self.width / 2) + 61
        self.y = coor_y - (self.height / 2) + 61

    def shell_motion(self, direction):
        if direction == 2.0:
            self.y -= self.speed
        elif direction == 2.5:
            self.y -= self.speed
            self.x += self.speed
        elif direction == 1.5:
            self.y -= self.speed
            self.x -= self.speed
        elif direction == 1.0:
            self.x -= self.speed
        elif direction == 3.0:
            self.x += self.speed
        elif direction == 4.0:
            self.y += self.speed
        elif direction == 3.5:
            self.y += self.speed
            self.x += self.speed
        elif direction == 4.5:
            self.y += self.speed
            self.x -= self.speed

        if self.x < 0 or self.x > 782 or self.y < 0 or self.y > 782:
            return True
        else:
            return False
