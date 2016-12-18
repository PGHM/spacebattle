# Player model

import pygame as pg

class Player:

    def __init__(self):
        self.health = 100

        self.position_x = 100
        self.position_y = 100

        self.direction_angle = 0

        self.ship_color = (0,100,100)

    def get_position(self):
        return [position_x, position_y]

    def get_direction(self):
        return direction_angle

    def change_diretion(self, angle_diff):
        direction_angle += angle_diff

    def draw(self   ):
        main_surface = pg.display.get_surface()
        pg.draw.polygon(main_surface, self.ship_color, ((200, 300), (300, 150), (200, 0)))



