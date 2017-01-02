from constants import (INITIAL_ROCK_SPAWN_RATE, INITIAL_ENEMY_SPAWN_RATE,
        ENEMY_SPAWN_EVENT, ROCK_SPAWN_EVENT)
import pygame as pg
from models.mine import Mine
from models.star import Star
from engine.geometry import reached_edge, move
from ui.hud import HUD

class Map:

    def __init__(self, player):
        self.player = player
        self.hud = HUD(pg.display.get_surface())
        self.rocks = []
        self.enemies = []
        self.bullets = []
        self.score = 0;
        self.enemy_spawn_rate = INITIAL_ENEMY_SPAWN_RATE
        self.rock_spawn_rate = INITIAL_ROCK_SPAWN_RATE
        pg.time.set_timer(ENEMY_SPAWN_EVENT, self.enemy_spawn_rate)

    def spawn_enemies(self):
        if len(self.enemies) % 2 == 0:
            self.enemies.append(Star(self.player.get_position()))
        else:
            self.enemies.append(Mine(self.player.get_position()))

    def update(self):
        for bullet in self.bullets:
            bullet.update_position(bullet.direction, bullet.speed)

            if reached_edge(bullet.get_hit_box_point(),
                    pg.display.get_surface()):
                self.bullets.remove(bullet)
        
        for enemy in self.enemies:
            enemy.update_position(enemy.direction, enemy.speed)
            if reached_edge(enemy.position,
                    pg.display.get_surface()):
                self.enemies.remove(enemy)
                continue

            enemy.damage(self.bullets)
            if enemy.health <= 0:
                self.score += enemy.max_health
                self.enemies.remove(enemy)
                continue

            if enemy.is_point_inside_hit_box(
                    self.player.space_ship.get_apex_point_relative_to(self.player.get_position())):
                self.player.health -= enemy.collision_damage
                self.enemies.remove(enemy)
                continue

    def draw(self):
        for bullet in self.bullets:
            bullet.draw()

        for enemy in self.enemies:
            enemy.draw()

        self.draw_hud()

    def draw_hud(self):
        self.hud.print_score(self.score)
        self.hud.print_health(self.player.health)

    def move_objects(self, direction, speed):
        for enemy in self.enemies:
            enemy.update_position(direction, speed)

        for bullet in self.bullets:
            bullet.update_position(direction, speed)
