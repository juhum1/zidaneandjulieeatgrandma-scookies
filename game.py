import pygame
import enemies

pygame.init()
size = width, height = 1280, 720
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Game")
clock = pygame.time.Clock()
running = True

while running:
    fps = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    currency = 100


pygame.quit()