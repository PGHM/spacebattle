import pygame as pg
from constants import WINDOW_WIDTH, WINDOW_HEIGHT
from models.player import Player
from models.map import Map
from engine.control import handle_key_up, handle_key_down
from models.space_ship import SpaceShip

def main():
    """ Set up the game and run the main game loop """
    pg.init()      # Prepare the pygame module for use
    surface_height = WINDOW_WIDTH   # Desired physical surface size, in pixels.
    surface_width = WINDOW_HEIGHT    # Desired physical surface size, in pixels.

    clock = pg.time.Clock()

    # Create surface of (width, height), and its window.
    main_surface = pg.display.set_mode((surface_height, surface_width))

    bg_color = (0, 0, 100)  # A color is a mix of (Red, Green, Blue)

    space_ship = SpaceShip(50,30, (255,0,0))
    player = Player(space_ship)
    game_map = Map(player, clock)

    while True:
        clock.tick(60)

        ev = pg.event.poll()    # Look for any event

        if ev.type == pg.QUIT:  # Window close button clicked?
            break                   #   .   .. leave game loop
        elif ev.type == pg.KEYDOWN:
            if ev.key == pg.K_SPACE:
                game_map.bullets.append(player.fire())
        elif ev.type == pg.KEYUP:
            pass

        keys = pg.key.get_pressed()

        if keys[pg.K_UP]:
            player.move_forward()
        if keys[pg.K_DOWN]:
            player.move_backwards()
        if keys[pg.K_LEFT]:
            player.change_direction(-0.1)
        if keys[pg.K_RIGHT]:
            player.change_direction(0.1)
        
        game_map.update()

        # We draw everything from scratch on each frame.
        # So first fill everything with the background color

        main_surface.fill(bg_color)
        player.draw()
        game_map.draw()

        # Now the surface is ready, tell pygame to display it!
        pg.display.flip()

    pg.quit()     # Once we leave the loop, close the window.

main()
