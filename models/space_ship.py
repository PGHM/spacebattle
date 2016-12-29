from engine.geometry import rotate
from math import cos, sin, pi

class SpaceShip:

    def __init__(self, length, width, color):
        self.length = length
        self.width = width
        self.ship_color = color

        self.apex_point = [0, -1*length/2]
        self.left_wing_point = [-1*width/2, length/2 ]
        self.right_wing_point = [width/2, length/2 ]

    def get_point_list(self):
        return [self.apex_point, self.left_wing_point, self.right_wing_point]

    def get_apex_point_relative_to(self, point_x):
        point_list = self.get_point_list()
        return (point_list[0][0] + point_x[0] , point_list[0][1] + point_x[1])

    def get_color(self):
        return self.ship_color

    def update_points(self, angle_diff):
        points = rotate(self.get_point_list(), angle_diff)
        self.apex_point = points[0]
        self.left_wing_point = points[1]
        self.right_wing_point = points[2]
