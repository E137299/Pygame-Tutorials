import pygame, sys, random, math, time

# --------------------------------------------------
# Raindrop Sprite Class
# --------------------------------------------------
# This class defines ONE raindrop.
# Multiple Raindrop objects will be stored inside a sprite group.
class Raindrop(pygame.sprite.Sprite):
    def __init__(self):
        # Initialize the Sprite parent class
        # This step is REQUIRED so the object can be managed by sprite groups
        super(Raindrop, self).__init__()

        # Load the raindrop image with transparency
        self.image = pygame.image.load("graphics/raindrop.png").convert_alpha()

        # Resize the image
        self.image = pygame.transform.scale(self.image, (20,20))

        # Create a rect to track position and size
        # The rect is what Pygame uses to draw the sprite
        self.rect = self.image.get_rect(
            center=(random.randint(20,1180), random.randint(-550,800))
        )
    
    def fall(self):
        """
        Moves the raindrop downward.
        This method will be called once per frame from the main loop.
        """
        # If the raindrop goes off the bottom of the screen,
        # reset it to a random position near the top
        if self.rect.bottom > 700:
            self.rect = self.image.get_rect(
                center=(random.randint(20,1180), random.randint(-550,800))
            )

        # Move the raindrop down by 4 pixels
        self.rect.centery += 4


# --------------------------------------------------
# Apple Sprite Class
# --------------------------------------------------
class Apple(pygame.sprite.Sprite):
    def __init__(self):
        super(Apple, self).__init__()

        self.image = pygame.image.load("graphics/apple.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50,50))

        self.rect = self.image.get_rect(
            center=(random.randint(20,1180), random.randint(-550,-20))
        )
    
    def fall(self):
        """
        Moves the apple downward.
        """
        if self.rect.bottom > 700:
            # Reset apple to the top once it falls off screen
            self.rect = self.image.get_rect(
                center=(random.randint(20,1180), random.randint(-550,-20))
            )

        self.rect.centery += 4


# --------------------------------------------------
# Pygame Initialization
# --------------------------------------------------
pygame.init()

screen_width = 1200
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Agario")

# Clock controls the frame rate
clock = pygame.time.Clock()


# --------------------------------------------------
# SPRITE GROUPS
# --------------------------------------------------

# Create a sprite group to store ALL Apple objects
# A sprite group is like a list, but with built-in game features
apples = pygame.sprite.Group()

# Create and add 10 Apple sprites to the group
for i in range(10):
    apples.add(Apple())

# Create a sprite group to store ALL Raindrop objects
rain = pygame.sprite.Group()

# Create and add 100 Raindrop sprites to the group
for i in range(100):
    rain.add(Raindrop())

# --------------------------------------------------
# Gropus containing groups
# --------------------------------------------------
# Groups can only contain SPRITES, not other groups.
# This is why the following code would not work:
#
# falling_objects = pygame.sprite.Group()
# falling_objects.add(apples)   
# falling_objects.add(rain)     


# --------------------------------------------------
# Main Game Loop
# --------------------------------------------------
running = True
while running:

    # ------------------------------
    # Event Handling
    # ------------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen each frame
    screen.fill((0,0,0))

    # ------------------------------
    # Update Sprites via Groups
    # ------------------------------

    # Loop through each Apple sprite in the apples group
    # and call its fall() method
    for apple in apples:
        apple.fall()
    
    # Loop through each Raindrop sprite in the rain group
    for drop in rain:
        drop.fall()

    # Loop through each object in the falling objects group (all raindrops and apples)
    # for object in falling_objects:
    #     objects.fall()

    # ------------------------------
    # Draw Sprite Groups
    # ------------------------------

    # Draws every Apple sprite in the apples group
    # Pygame automatically blits apple.image at apple.rect
    apples.draw(screen)

    # Draws every Raindrop sprite in the rain group
    rain.draw(screen)

    # Draws every object in the falling object group
    falling_objects.draw(screen)

    # ------------------------------
    # Display Update
    # ------------------------------
    pygame.display.flip()
    clock.tick(60)


# --------------------------------------------------
# Clean Exit
# --------------------------------------------------
pygame.quit()
sys.exit()
