from constants import (INITIAL_ROCK_SPAWN_RATE, INITIAL_ENEMY_SPAWN_RATE,
        ENEMY_SPAWN_EVENT, ROCK_SPAWN_EVENT)
import pygame as pg
from models.mine import Mine
from models.star import Star
from engine.geometry import reached_edge

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
        if len(self.enemies) % 2 == 0:
            self.enemies.append(Star())
        else:
            self.enemies.append(Mine())

    def update(self):
        for bullet in self.bullets:
            bullet.update_position()

            if reached_edge(bullet.get_hit_box_point(),
                    pg.display.get_surface()):
                self.bullets.remove(bullet)
        
        for enemy in self.enemies:
            enemy.update_position()
            if reached_edge(enemy.position,
                    pg.display.get_surface()):
                self.enemies.remove(enemy)
                continue

            enemy.damage(self.bullets)
            if enemy.health <= 0:
                self.enemies.remove(enemy)

            if enemy.is_point_inside_hit_box(
                    self.player.space_ship.get_apex_point_relative_to(self.player.get_position())):
                self.player.health -= enemy.collision_damage
                self.enemies.remove(enemy)


    def draw(self):
        for bullet in self.bullets:
            bullet.draw()

        for enemy in self.enemies:
            enemy.draw()