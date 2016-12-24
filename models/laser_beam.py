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
        self.damage = 50
        self.direction = direction
        self.starting_pos = starting_pos
        self.pos_tail = starting_pos
        self.pos_front = move(self.pos_tail, self.direction, self.beam_length)
        self.main_surface = pg.display.get_surface()

    def get_hit_box_point(self):
        return self.pos_front

    def draw(self):
        pg.draw.line(self.main_surface, self.color, self.pos_tail, self.pos_front, 3)

    def update_position(self):
        self.pos_tail = move(self.pos_tail, self.direction, self.speed)
        self.pos_front = move(self.pos_front, self.direction, self.speed)
