from random import uniform
from engine.geometry import move, distance, rotate, point_in_polygon 
from models.enemy import Enemy
from math import pi
import pygame as pg

class Star(Enemy):

    def __init__(self, player_position):
        self.calculate_spawn_position(player_position)
        self.main_surface = pg.display.get_surface()
        self.color = (255, 255, 0)
        self.speed = 5
        self.rotation_speed = 0.1
        self.direction = uniform(0, 2*pi)
        self.max_health = 100
        self.health = self.max_health
        self.collision_damage = 50

        #TODO: fix the star shape
        self.point_list = [
                (0, -20),
                (5, 0),
                (20, 0),
                (10, 5),
                (15, 20),
                (0, 10),
                (-15, 20),
                (-10, 5),
                (-20, 0),
                (-5, 0)]

    def damage(self, bullets):
        for bullet in bullets:
            if self.is_point_inside_hit_box(bullet.get_hit_box_point()):
                self.health -= bullet.damage
                bullets.remove(bullet)

    def is_point_inside_hit_box(self, point):
        return point_in_polygon(point, self.get_moved_points())

    def update_position(self, direction, speed):
        self.position = move(self.position, direction, speed)
   
    def get_moved_points(self):
        moved_points = []
        for point in self.point_list:
            moved_points.append((point[0] + self.position[0], point[1] +
                self.position[1]))
        return moved_points

    def draw(self):
        self.point_list = rotate(self.point_list, self.rotation_speed)
        pg.draw.polygon(self.main_surface, self.color,
                self.get_moved_points(), 0)
