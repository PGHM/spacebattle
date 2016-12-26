from constants import WINDOW_WIDTH, WINDOW_HEIGHT
from random import randint
from engine.geometry import distance
import pygame as pg
from engine.geometry import move


class Mine:

    def __init__(self):
        self.radius = randint(20, 35)
        self.position = (randint(self.radius, WINDOW_WIDTH - self.radius),
                randint(self.radius, WINDOW_HEIGHT - self.radius))
        self.main_surface = pg.display.get_surface()
        self.color = (0, 0, 255)
        self.max_health = 100
        self.health = self.max_health
        self.collision_damage = 100

    def damage(self, bullets):
        for bullet in bullets:
            if self.is_point_inside_hit_box(bullet.get_hit_box_point()):
                self.health -= bullet.damage
                bullets.remove(bullet)

    def is_point_inside_hit_box(self, point):
        return distance(point, self.position) <= self.radius

    def update_position(self):
        pass # mines do not move
    
    def draw(self):
        pg.draw.circle(self.main_surface, self.color, self.position,
                self.radius) 
