import pygame as pg
from constants import WINDOW_WIDTH, WINDOW_HEIGHT
from models.player import Player
from engine.control import handle_key_up, handle_key_down
from pygame import Rect


def main():
    """ Set up the game and run the main game loop """
    pg.init()      # Prepare the pygame module for use
    surface_height = WINDOW_WIDTH   # Desired physical surface size, in pixels.
    surface_width = WINDOW_HEIGHT    # Desired physical surface size, in pixels.

    surface_height = 700   # Desired physical surface size, in pixels.
    surface_width = 700    # Desired physical surface size, in pixels.
    # Create surface of (width, height), and its window.
    main_surface = pg.display.set_mode((surface_height, surface_width))

    some_color = (0, 0, 255)  # A color is a mix of (Red, Green, Blue)
    some_other_color = (255, 255, 255)
    # Set up some data to describe a small rectangle and its color
    triangle_points = (0,200),(100,0),(200,200)




    player = Player()
    while True:
        ev = pg.event.poll()    # Look for any event
        if ev.type == pg.QUIT:  # Window close button clicked?
            break                   #   .   .. leave game loop
        elif ev.type == pg.KEYDOWN:
            handle_key_down(ev)
        elif ev.type == pg.KEYUP:
            handle_key_up(ev)

        # Update your game objects and data structures here...

        # We draw everything from scratch on each frame.
        # So first fill everything with the background color

        main_surface.fill(some_color)

        pg.draw.polygon(main_surface, some_other_color, triangle_points, 0)

        player.draw()
        # main_surface.fill(some_other_color, small_box)
        

        # Overpaint a smaller rectangle on the main surface

        # Now the surface is ready, tell pygame to display it!
        pg.display.flip()

    pg.quit()     # Once we leave the loop, close the window.

main()
