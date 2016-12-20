from constants import WINDOW_WIDTH, WINDOW_HEIGHT
from random import randint
import pygame as pg

class Mine:

    def __init__(self):
        self.radius = randint(5, 10)
        self.position = (randint(self.radius, WINDOW_WIDTH - self.radius),
                randint(self.radius, WINDOW_HEIGHT - self.radius))
        self.main_surface = pg.display.get_surface()
        self.color = (255, 255, 0)

    def update_position(self):
        pass # mines do not move
    
    def draw(self):
        pg.draw.circle(self.main_surface, self.color, self.position,
                self.radius) 
