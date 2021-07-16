class Point:
    point = ()
    def __init__ (self, pointA, pointB):
        self.point = (pointA, pointB)

def manhattanDistance(a, b):
    """Return Manhattan Distance of Two Coordinates

    Using formuala |Xa - Xb| + |Ya - Yb|
    """
    return abs(a.point[0] - b.point[0]) + abs(a.point[1] - b.point[1])
