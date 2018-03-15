import pygame, importlib, Character
from Character import Character

class runGame:
    def __init__(self):
        pygame.init()

        GREEN = (0, 170, 100)
        WHITE = (255, 255, 255)

        window = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Tristram')
        window.fill(GREEN)

        sherman = Character(3.0, 1.0, 1.0)
        sherman.drawCharacter()
        pygame.display.flip()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
