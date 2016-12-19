import pygame as pg
from math import sin
from math import cos
from math import pi


class LaserBeam:

    def __init__(self, color, starting_pos, direction):
        self.beam_length = 20
        self.speed = 10

        self.color = color
        # self.damage = damage
        self.direction = direction
        self.starting_pos = starting_pos
        self.pos_tail = starting_pos

        #TODO: make a method for move, rotate etc. basic geometric transformations
        self.pos_front = [starting_pos[0] + self.beam_length *
                cos(self.direction), starting_pos[1] + self.beam_length * sin(self.direction)]
       
        self.main_surface = pg.display.get_surface()

    def draw(self):
        if self.reached_edge():
            return False
        pg.draw.line(self.main_surface, self.color, self.pos_tail, self.pos_front, 3)
        return True 

    def update_position(self):
        tail_x = self.pos_tail[0] + self.speed * cos(self.direction)
        tail_y = self.pos_tail[1] + self.speed * sin(self.direction)

        front_x = self.pos_tail[0] + self.beam_length * cos(self.direction)
        front_y = self.pos_tail[1] + self.beam_length * sin(self.direction)

        self.pos_tail = (tail_x, tail_y)
        self.pos_front = (front_x, front_y )

    def reached_edge(self):
        x_out_of_bounds = self.pos_front[0] < 0 or self.pos_front[0] > self.main_surface.get_width()
        y_out_of_bounds = self.pos_front[1] < 0 or self.pos_front[1] > self.main_surface.get_height()

        if x_out_of_bounds or y_out_of_bounds:
            return True
        return False
