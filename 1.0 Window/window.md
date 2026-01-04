# Creating a Window

<br></br>
#### <span style="color:red;">pygame.init()</span>
A function in the Pygame library that initializes all the Pygame modules required for your game or application to work. This function initializes various modules like display, sound, joystick, etc. It sets up the necessary resources and prepares Pygame to handle its functionalities. 

<br></br>
#### <span style="color:red;">screen = pygame.display.set_mode((screen_width, screen_height))</span>
Initializes a window or screen for display. Any drawings, shapes, images, or text you want to display in your game will be rendered onto this surface (screen) using various Pygame functions like pygame.draw, blit, or other graphical operations.

<br></br>
#### <span style="color:red;">clock = pygame.time.Clock()</span>
Creates an object of the Clock class from the Pygame library. This clock object is commonly used to control the frame rate of your game.

<br></br>
#### <span style="color:red;">for event in pygame.event.get():</span>
In Pygame, events are actions or occurrences that the program can detect and respond to. These events can include things like mouse movements, keyboard inputs, window resizing, etc.

The pygame.event.get() function retrieves all the events that have occurred since the last time it was called. The for event in pygame.event.get(): loop then iterates through each of these events, allowing you to examine and respond to each event individually.

<br></br>
#### <span style="color:red;">if event.type == pygame.QUIT:</span>
A conditional statement inside a Pygame event loop. It checks whether the current event that is being processed is of type pygame.QUIT.

In Pygame, pygame.QUIT is an event type that occurs when the user attempts to close the game window by clicking the close button in the window's title bar.

<br></br>
#### <span style="color:red;">screen.fill(WHITE)</span>
Sets the background color of the window

<br></br>
#### <span style="color:red;">pygame.display.flip()</span>
In Pygame, when you make changes to what is shown on the screen (drawing shapes, updating positions of game elements, etc.), those changes are made to a portion of the computer's memory that represents the display. However, these changes are not immediately shown on the actual screen. The flip() function updates the entire display with all the changes that have been made since the last flip.

<br></br>
#### <span style="color:red;">clock.tick()</span>
a method used in Pygame to control the frame rate of your game loop.