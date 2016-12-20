from constants import INITIAL_ROCK_SPAWN_RATE, INITIAL_ENEMY_SPAWN_RATE

class Map:

    def __init__(self, player, clock):
        self.player = player
        self.clock = clock
        self.rocks = []
        self.enemies = []
        self.bullets = []
        self.enemy_spawn_rate = INITIAL_ENEMY_SPAWN_RATE
        self.rock_spawn_rate = INITIAL_ROCK_SPAWN_RATE

    def update(self):
        for bullet in self.bullets:
            bullet.update_position()

            if bullet.reached_edge():
                self.bullets.remove(bullet)

#        for enemy in self.enemies:
#            enemy.health -= enemy.damage(self.bullets)
#            if enemy.health < 0:
#                enemy.destroy()

    def draw(self):
        for bullet in self.bullets:
            bullet.draw()
