import pygame
from pygame import Rect

def main():
    """ Set up the game and run the main game loop """
    pygame.init()      # Prepare the pygame module for use
    surface_height = 700   # Desired physical surface size, in pixels.
    surface_width = 700    # Desired physical surface size, in pixels.

    # Create surface of (width, height), and its window.
    main_surface = pygame.display.set_mode((surface_height, surface_width))

    # Set up some data to describe a small rectangle and its color
    small_box = Rect(surface_width / 2, surface_height / 2,50 ,50)
    some_color = (0, 0, 0)        # A color is a mix of (Red, Green, Blue)
    some_other_color = (255,255,255)

    while True:
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop

        # Update your game objects and data structures here...

        # We draw everything from scratch on each frame.
        # So first fill everything with the background color

        main_surface.fill(some_color, small_box)
        main_surface.fill(some_other_color, small_box)

        # Overpaint a smaller rectangle on the main surface

        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()

    pygame.quit()     # Once we leave the loop, close the window.

main()