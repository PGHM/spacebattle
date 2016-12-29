from random import randint
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, NO_SPAWN_RADIUS
from engine.geometry import distance

class Enemy:

    def calculate_spawn_position(self, player_position):
        spawn_too_close = True
        while spawn_too_close:
            self.position = (randint(self.radius, WINDOW_WIDTH - self.radius),
                    randint(self.radius, WINDOW_HEIGHT - self.radius))
            spawn_too_close = distance(self.position, player_position) < NO_SPAWN_RADIUS
