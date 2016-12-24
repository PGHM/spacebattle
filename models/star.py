from random import randint
from engine.geometry import move
from constants import WINDOW_WIDTH, WINDOW_HEIGHT
from engine.geometry import distance
import pygame as pg

class Star:

    def __init__(self):
        self.radius = 15
        self.position = (randint(self.radius, WINDOW_WIDTH - self.radius),
                randint(self.radius, WINDOW_HEIGHT - self.radius))
        self.main_surface = pg.display.get_surface()
        self.color = (255, 255, 0)
        self.speed = 5
        self.direction = randint(0, 100)
        self.health = 100
        self.collision_damage = 50

    def damage(self, bullets):
        for bullet in bullets:
            if self.is_point_inside_hit_box(bullet.get_hit_box_point()):
                self.health -= bullet.damage
                bullets.remove(bullet)

    def is_point_inside_hit_box(self, point):
        return distance(point, self.position) <= self.radius

    def update_position(self):
        self.position = move(self.position, self.direction, self.speed)
    
    def draw(self):
        pg.draw.circle(self.main_surface, self.color, self.position,
                self.radius)
