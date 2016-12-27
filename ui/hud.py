
from constants import WINDOW_WIDTH, WINDOW_HEIGHT
import pygame as pg
class HUD:

    def __init__(self, main_surface):

        self.main_surface = main_surface
        self.xxl_font = pg.font.SysFont("monospace", 100)
        self.default_font = pg.font.SysFont("monospace", 15)



    def print_game_over(self): 
        label = self.xxl_font.render("GAME OVER!", 1, (255, 0, 0))
        self.main_surface.blit(label, (WINDOW_WIDTH / 2 - label.get_width() / 2 , WINDOW_HEIGHT / 2 - label.get_height() / 2))

    def print_score(self, score):
        label = self.default_font.render('Score: {}'.format(score), 1, (0, 255, 0))
        self.main_surface.blit(label, (10, 10))

    def print_health(self, health):
        if health < 0:
            health = 0
        label = self.default_font.render('Health: {}'.format(health), 1, (255, 0, 0))
        self.main_surface.blit(label, (WINDOW_WIDTH - label.get_width() - 10 , 10))