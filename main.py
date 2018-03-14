import pygame

pygame.init()

GREEN = (0, 170, 100)
WHITE = (255, 255, 255)

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Tristram')
window.fill(GREEN)
pygame.draw.rect(window, WHITE, (200, 200, 100, 50))
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#adding new test comment here#
#added comment anthony#
#branch update#
