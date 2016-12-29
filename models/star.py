from random import randint
from engine.geometry import move, distance
from models.enemy import Enemy
import pygame as pg

class Star(Enemy):

    def __init__(self, player_position):
        self.radius = 15
        self.calculate_spawn_position(player_position)
        self.main_surface = pg.display.get_surface()
        self.color = (255, 255, 0)
        self.speed = 5
        self.direction = randint(0, 360)
        self.max_health = 100
        self.health = self.max_health
        self.collision_damage = 50

    def damage(self, bullets):
        for bullet in bullets:
            if self.is_point_inside_hit_box(bullet.get_hit_box_point()):
                self.health -= bullet.damage
                bullets.remove(bullet)

    def is_point_inside_hit_box(self, point):
        return distance(point, self.position) <= self.radius

    def update_position(self, direction, speed):
        self.position = move(self.position, direction, speed)
    
    def draw(self):
        pg.draw.circle(self.main_surface, self.color, self.position,
                self.radius)
