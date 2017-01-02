from random import randint
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, NO_SPAWN_RADIUS
from engine.geometry import distance

class Enemy:

    def get_int_coordinates(self):
        return (int(self.position[0]),int(self.position[1]))
        
    def calculate_spawn_position(self, player_position):
        spawn_too_close = True
        while spawn_too_close:
            self.position = (randint(0, WINDOW_WIDTH), randint(0,
                WINDOW_HEIGHT))
            spawn_too_close = distance(self.position, player_position) < NO_SPAWN_RADIUS
