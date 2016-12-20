from constants import (INITIAL_ROCK_SPAWN_RATE, INITIAL_ENEMY_SPAWN_RATE,
        ENEMY_SPAWN_EVENT, ROCK_SPAWN_EVENT)
import pygame as pg
from models.mine import Mine

class Map:

    def __init__(self, player):
        self.player = player
        self.rocks = []
        self.enemies = []
        self.bullets = []
        self.enemy_spawn_rate = INITIAL_ENEMY_SPAWN_RATE
        self.rock_spawn_rate = INITIAL_ROCK_SPAWN_RATE
        pg.time.set_timer(ENEMY_SPAWN_EVENT, self.enemy_spawn_rate)

    def spawn_enemies(self):
        self.enemies.append(Mine())

    def update(self):
        for bullet in self.bullets:
            bullet.update_position()

            if bullet.reached_edge():
                self.bullets.remove(bullet)
        
        for enemy in self.enemies:
            enemy.update_position()
#            enemy.health -= enemy.damage(self.bullets)
#            if enemy.health < 0:
#                enemy.destroy()

    def draw(self):
        for bullet in self.bullets:
            bullet.draw()

        for enemy in self.enemies:
            enemy.draw()
