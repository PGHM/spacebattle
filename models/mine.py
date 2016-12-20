from constants import WINDOW_WIDTH, WINDOW_HEIGHT
from random import randint
from engine.geometry import distance
import pygame as pg

class Mine:

    def __init__(self):
        self.radius = randint(20, 35)
        self.position = (randint(self.radius, WINDOW_WIDTH - self.radius),
                randint(self.radius, WINDOW_HEIGHT - self.radius))
        self.main_surface = pg.display.get_surface()
        self.color = (255, 255, 0)
        self.health = 100

    def damage(self, bullets):
        for bullet in bullets:
            if (distance(bullet.get_hit_box_point(), self.position) <=
                    self.radius):
                self.health -= bullet.damage
                bullets.remove(bullet)

    def update_position(self):
        pass # mines do not move
    
    def draw(self):
        pg.draw.circle(self.main_surface, self.color, self.position,
                self.radius) 
