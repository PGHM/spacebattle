# Player model

import pygame as pg
from models.laser_beam import LaserBeam


class Player:

    def __init__(self, space_ship):
        self.main_surface = pg.display.get_surface()

        self.health = 100

        self.position_x = self.main_surface.get_width() / 2
        self.position_y = self.main_surface.get_height() / 2
        self.direction_angle = 0

        self.space_ship = space_ship

        self.bullets = []
    def get_position(self):
        return [self.position_x, self.position_y]

    def get_direction(self):
        return self.direction_angle

    def change_direction(self, angle_diff):
        self.direction_angle += angle_diff
        self.space_ship.update_points(angle_diff)


    def fire(self):
        new_laser_beam = LaserBeam((255,0,0), self.space_ship.get_apex_point_relative_to(self.get_position()), self.direction_angle)
        self.bullets.append(new_laser_beam)

    def draw(self):
      
        point_list = self.space_ship.get_point_list();

        p1 = (point_list[0][0] + self.position_x , point_list[0][1] + self.position_y)
        p2 = (point_list[1][0] + self.position_x , point_list[1][1] + self.position_y)
        p3 = (point_list[2][0] + self.position_x , point_list[2][1] + self.position_y)

        pg.draw.polygon(self.main_surface, self.space_ship.get_color(),(p1,p2,p3), 2)

        for bullet in self.bullets:
            if bullet.draw():
                bullet.update_position()
            else:
                self.bullets.remove(bullet)