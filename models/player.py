# Player model

import pygame as pg
from models.laser_beam import LaserBeam
from engine.geometry import move
from engine import audio_player
from math import pi

class Player:

    def __init__(self, space_ship):
        self.main_surface = pg.display.get_surface()

        self.health = 100

        self.position_x = self.main_surface.get_width() / 2
        self.position_y = self.main_surface.get_height() / 2
        
        #TODO: this could come as a parameter?
        self.direction_angle = 3 * pi / 2 # ship starts with apex pointing up
        
        self.space_ship = space_ship

    def get_position(self):
        return [self.position_x, self.position_y]

    def get_direction(self):
        return self.direction_angle
    
    def get_speed(self):
        return self.space_ship.speed

    def change_direction(self, angle_diff):
        self.direction_angle = (self.direction_angle + angle_diff) % (2*pi)
        self.space_ship.update_points(angle_diff)

    def fire(self):
        audio_player.play_laser_beam_sound()
        return LaserBeam((255, 0, 0), self.space_ship.get_apex_point_relative_to(self.get_position()), self.direction_angle)

    def draw(self):
        point_list = self.space_ship.get_point_list();

        p1 = (point_list[0][0] + self.position_x , point_list[0][1] + self.position_y)
        p2 = (point_list[1][0] + self.position_x , point_list[1][1] + self.position_y)
        p3 = (point_list[2][0] + self.position_x , point_list[2][1] + self.position_y)

        pg.draw.polygon(self.main_surface, self.space_ship.get_color(), (p1, p2, p3), 2)
