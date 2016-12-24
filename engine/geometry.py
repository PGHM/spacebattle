from math import cos, sin, pi, hypot

def rotate(polygon, angle):
    rotated_points = []
    cos_result = cos(angle)
    sin_result = sin(angle)
    for point in polygon:
        x = point[0] * cos_result - point[1] * sin_result
        y = point[0] * sin_result + point[1] * cos_result
        rotated_points.append((x, y))
    return rotated_points

def move(point, direction, amount):
    return [int(point[0] + amount * cos(direction)),
            int(point[1] + amount * sin(direction))]

def distance(point1, point2):
    return hypot(point1[0] - point2[0], point1[1] - point2[1])
