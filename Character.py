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
