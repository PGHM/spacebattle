import pygame
from pygame import Rect


def main():
    """ Set up the game and run the main game loop """
    pygame.init()      # Prepare the pygame module for use
    surface_height = 700   # Desired physical surface size, in pixels.
    surface_width = 700    # Desired physical surface size, in pixels.

    # Create surface of (width, height), and its window.
    main_surface = pygame.display.set_mode((surface_height, surface_width))

    some_color = (0, 0, 255)  # A color is a mix of (Red, Green, Blue)
    some_other_color = (255, 255, 255)
    # Set up some data to describe a small rectangle and its color
    triangle_points = (0,200),(100,0),(200,200)




    while True:
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop

        # Update your game objects and data structures here...

        # We draw everything from scratch on each frame.
        # So first fill everything with the background color

        main_surface.fill(some_color)
        pygame.draw.polygon(main_surface, some_other_color, triangle_points, 0)

        # Overpaint a smaller rectangle on the main surface

        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()

    pygame.quit()     # Once we leave the loop, close the window.

main()