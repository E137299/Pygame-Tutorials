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

'''
Create a surface displaying a color
'''
color_surface = pygame.Surface((200,200))
color_surface.fill("pink") #assign color to surface with the name of a color in a catalog
# color_surface.fill((120,120,240)) # assign a tuple containing RGB values
# color_surface.fill("#EE30FF") # assign a hexidecimal color value

'''
Create a circular surface 
'''
circle_radius = 75
circle_surface = pygame.Surface((circle_radius * 2, circle_radius * 2), pygame.SRCALPHA) # creates a rectangular surface
# circle_surface.fill("Black")
pygame.draw.circle(circle_surface, (255, 0, 0, 128), (circle_radius, circle_radius), circle_radius) # draws circle on surface



'''
Create a surface displaying an image
'''
mario_surface = pygame.image.load("2.0 Create Surfaces/mario.png").convert_alpha()


'''
Create a surface displaying text
'''
# Create font
font = pygame.font.Font(None,100)
text_surface = font.render("Text Surface", False,"Green")
# text_surface.fill("Pink")



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    #Blit images onto screen
    screen.blit(color_surface, (50,50))
    screen.blit(mario_surface,(300,50))
    screen.blit(text_surface,(50,400))
    screen.blit(circle_surface,(550,350))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
