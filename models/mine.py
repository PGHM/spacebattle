import pygame as pg
from random import randint
from models.enemy import Enemy
from engine.geometry import distance, move

class Mine(Enemy):

    def __init__(self, player_position):
        self.radius = randint(20, 35)
        self.calculate_spawn_position(player_position)
        self.main_surface = pg.display.get_surface()
        self.color = (0, 0, 255)
        self.direction = 0
        self.speed = 0
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

    def update_position(self, direction, speed):
        self.position = move(self.position, direction, speed)
    
    def draw(self):
        pg.draw.circle(self.main_surface, self.color, self.position,
                self.radius) 
