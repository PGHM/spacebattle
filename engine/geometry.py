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
    return [point[0] + amount * cos(direction),
            point[1] + amount * sin(direction)]

def distance(point1, point2):
    return hypot(point1[0] - point2[0], point1[1] - point2[1])

def reached_edge(position, main_surface):
    x_out_of_bounds = position[0] < 0 or position[0] > main_surface.get_width()
    y_out_of_bounds = position[1] < 0 or position[1] > main_surface.get_height()
    return x_out_of_bounds or y_out_of_bounds

def point_in_polygon(point, poly):
    x, y = point
    n = len(poly)
    inside = False

    p1x,p1y = poly[0]
    for i in range(n+1):
        p2x,p2y = poly[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xints = (y-p1y) * (p2x-p1x) / (p2y-p1y) + p1x
                    if p1x == p2x or x <= xints:
                        inside = not inside
        p1x, p1y = p2x, p2y

    return inside
