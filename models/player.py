# Player model

import pygame as pg



class Player:

    def __init__(self, space_ship):
        self.main_surface = pg.display.get_surface()

        self.health = 100

        self.position_x = self.main_surface.get_width() / 2
        self.position_y = self.main_surface.get_height() / 2

        self.direction_angle = 0

        self.space_ship = space_ship

    def get_position(self):
        return [self.position_x, self.position_y]

    def get_direction(self):
        return direction_angle

    def change_diretion(self, angle_diff):
        direction_angle += angle_diff

    def draw(self):
        pg.draw.polygon(self.main_surface, self.space_ship.get_color(),self.space_ship.get_point_list(self.get_position()))