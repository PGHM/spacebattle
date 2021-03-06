import pygame as pg
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, ENEMY_SPAWN_EVENT, CLOCK_TICK
from models.player import Player
from models.map import Map
from engine.control import handle_key_up, handle_key_down
from models.space_ship import GalaxyFighter
from math import pi

def print_game_over(main_surface):
    myfont = pg.font.SysFont("monospace", 100)
    label = myfont.render("GAME OVER!", 1, (255, 0, 0))
    main_surface.blit(label, (WINDOW_WIDTH / 2 - label.get_width() / 2 , WINDOW_HEIGHT / 2 - label.get_height() / 2))
    pg.display.flip()

def reset_game():
    space_ship = GalaxyFighter(50, 30, (255, 255, 255))
    player = Player(space_ship)
    game_map = Map(player)
    return player, game_map

def main():
    """ Set up the game and run the main game loop """
    pg.init()      # Prepare the pygame module for use
    surface_height = WINDOW_HEIGHT   # Desired physical surface size, in pixels.
    surface_width = WINDOW_WIDTH    # Desired physical surface size, in pixels.

    clock = pg.time.Clock()

    # Create surface of (width, height), and its window.
    main_surface = pg.display.set_mode((surface_width, surface_height))

    bg_color = (0, 0, 0)  # A color is a mix of (Red, Green, Blue)
    player, game_map = reset_game()

    while True:
        clock.tick(CLOCK_TICK)

        ev = pg.event.poll()    # Look for any event
        keys = pg.key.get_pressed()

        if ev.type == pg.QUIT or keys[pg.K_ESCAPE]:  # Window close button clicked?
            break                   #   .   .. leave game loop

        if player == None and keys[pg.K_RETURN]:
                player, game_map = reset_game()

        elif ev.type == ENEMY_SPAWN_EVENT:
            game_map.spawn_enemies()


        # This block should contain key mapping that requires Player object
        if player != None:
            if keys[pg.K_LEFT]:
                player.change_direction(-0.075)
            if keys[pg.K_RIGHT]:
                player.change_direction(0.075)
            if keys[pg.K_UP]:
                game_map.move_objects((player.direction_angle + pi) % (2*pi),
                        player.get_speed())

            if ev.type == pg.KEYDOWN:
                if ev.key == pg.K_SPACE:
                    game_map.bullets.append(player.fire())

        game_map.update()

        # We draw everything from scratch on each frame.
        # So first fill everything with the background color

        main_surface.fill(bg_color)
        game_map.draw()
        if player == None:
            game_map.hud.print_game_over()
        else:
            player.draw()

        # Now the surface is ready, tell pygame to display it!
        pg.display.flip()

        # This block must be after all drawing
        if player != None and player.health <= 0:
            player = None
            continue

    pg.quit()     # Once we leave the loop, close the window.

main()
