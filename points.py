import math

def closest_point ( points, origin ):
    closest = 0
    cp = origin

    for p in points:
        distance = math.sqrt( math.pow( p[0] - origin[0], 2 ) + math.pow( p[1] - origin[1], 2 ) )
        if distance < closest or cp == origin:
            cp = p
            closest = distance

    return cp

points = [
    (-2, 4),
    (0, -2),
    (-1, 0),
    (3, 5),
    (-2, -3),
    (3, 2)
]
origin = (0, 0)

print ( closest_point( points, origin ) )