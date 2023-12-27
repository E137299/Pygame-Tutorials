'''
Tutorial demonstrates how to create a game window with Python Pygame.

Any pygame program that you create will have this basic code
'''

import pygame
import sys


pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Tutorial")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

clock = pygame.time.Clock()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    # Draw something on the screen (e.g., a blue rectangle)
    pygame.draw.rect(screen, BLUE, (300, 200, 200, 100))  # (x, y, width, height)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
