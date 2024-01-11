'''
Tutorial demonstrates how to create a game window with Python Pygame.

Any pygame program that you create will have this basic code
'''

import pygame, sys, random

class Jelly(pygame.sprite.Sprite):
    def __init__(self, num, x, y):
        super(Jelly, self).__init__()
        self.id = num
        self.index = 0
        self.files = ["4.0 Classes/jelly1.png","4.0 Classes/jelly2.png","4.0 Classes/jelly3.png"]
        self.images = [pygame.image.load(filename).convert_alpha() for filename in self.files]
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(center = (x,y))

        self.deltax = random.choice([-1,1])
        self.deltay = random.choice([-1,1])

    def move(self, count):
        if self.rect.left <= -0 or self.rect.right >= 800:
            self.deltax *= -1
        if self.rect.top <= -100 or self.rect.bottom >= 600:
            self.deltay *= -1

        for other in jellyfish:
            if jelly != other and jelly.rect.colliderect(other.rect):
                print("Before:",jelly.deltax,jelly.deltay)
                jelly.deltax *= -1
                print("After:",jelly.deltax,jelly.deltay)
                while jelly.rect.colliderect(other.rect):
                    self.rect.centerx += self.deltax
                    

        self.rect.centerx += self.deltax
        self.rect.centery += self.deltay

        if count%20 == 0:
            self.index = (self.index+1)%3
            self.image = self.images[self.index]





# Initialize Pygame and give access to all the methods in the package
pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Tutorial")

clock = pygame.time.Clock()


jellyfish = pygame.sprite.Group()
for num in range(3):
    jellyfish.add(Jelly(num, random.randint(75,725),random.randint(75,525)))


count = 0
running = True
while running:
    count += 1
    # Event handling
    for event in pygame.event.get(): # pygame.event.get()
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color (e.g., white)
    screen.fill("#122a72")

    for jelly in jellyfish:
        jelly.move(count)
        

    jellyfish.draw(screen)



    # Update the display
    pygame.display.flip()

    # Set a frame rate to 60 frames per second
    clock.tick(60)

# Quit Pygame properly
pygame.quit()
sys.exit()
