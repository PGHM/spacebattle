from engine.geometry import rotate
from math import cos, sin, pi

class SpaceShip:

    def __init__(self, point_list, color):
        self.ship_color = color
        self.point_list = point_list

    #Apex point should always be the first point in point_list
    def get_apex_point_relative_to(self, point):
        return (self.point_list[0][0] + point[0] , self.point_list[0][1] + point[1])

    def get_color(self):
        return self.ship_color

    def update_points(self, angle_diff):
        self.point_list = rotate(self.point_list, angle_diff)

    def get_point_list(self):
        return self.point_list

class GalaxyFighter(SpaceShip):

    def __init__(self, length, width, color):
        apex_point = [0, -1*length/2]
        left_wing_point = [-1*width/2, length/2 ]
        right_wing_point = [width/2, length/2 ]
        point_list = [apex_point, left_wing_point, right_wing_point]

        super().__init__(point_list, color)

        self.speed = 5