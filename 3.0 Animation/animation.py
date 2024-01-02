'''
Tutorial demonstrates how to create a game window with Python Pygame.

Any pygame program that you create will have this basic code
'''

import pygame, sys, random


pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Tutorial")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

clock = pygame.time.Clock()

'''
ANIMATION: Option 1
'''
circle_radius = 75
red_circle = pygame.Surface((circle_radius * 2, circle_radius * 2), pygame.SRCALPHA) # creates a rectangular surface
pygame.draw.circle(red_circle, (255, 0, 0, 128), (circle_radius, circle_radius), circle_radius) # draws circle on surface
red_x = 0 #coordinate of the left side of circle
red_y = 0 #coordinate of the top side of circle

'''
ANIMATION: Option 2
'''
circle_radius = 75
blue_circle = pygame.Surface((circle_radius * 2, circle_radius * 2), pygame.SRCALPHA) # creates a rectangular surface
pygame.draw.circle(blue_circle, (0, 0, 255,128),(circle_radius, circle_radius), circle_radius) # draws circle on surface
blue_rect = blue_circle.get_rect(center = (300,300))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    #ANIMATION: Option 1
    red_x +=1
    red_y +=0.5

    #ANIMATION: Option 2
    blue_rect.centerx += random.randint(-1,1)
    blue_rect.centery += random.randint(-1, 1)


    #Blit images onto screen
    screen.blit(red_circle,(red_x,red_y))
    screen.blit(blue_circle, blue_rect)


    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
