from math import cos, sin, pi

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
    return [point[0] + amount * cos(direction),
            point[1] + amount * sin(direction)]
