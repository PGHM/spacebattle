import pygame as pg
from math import sin
from math import cos
from math import pi
from engine.geometry import move

class LaserBeam:

    def __init__(self, color, starting_pos, direction):
        self.beam_length = 20
        self.speed = 10

        self.color = color
        # self.damage = damage
        self.direction = direction
        self.starting_pos = starting_pos
        self.pos_tail = starting_pos

        self.pos_front = move(self.pos_tail, self.direction, self.beam_length)
        self.main_surface = pg.display.get_surface()

    def draw(self):
        pg.draw.line(self.main_surface, self.color, self.pos_tail, self.pos_front, 3)

    def update_position(self):
        self.pos_tail = move(self.pos_tail, self.direction, self.speed)
        self.pos_front = move(self.pos_front, self.direction, self.speed)

    def reached_edge(self):
        x_out_of_bounds = self.pos_front[0] < 0 or self.pos_front[0] > self.main_surface.get_width()
        y_out_of_bounds = self.pos_front[1] < 0 or self.pos_front[1] > self.main_surface.get_height()

        return x_out_of_bounds or y_out_of_bounds
