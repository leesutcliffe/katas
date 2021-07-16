import pytest

from manhattan import manhattanDistance
from manhattan import Point

@pytest.fixture
def standard_tests():
    # return a list of tuples containing values for multiple grid references and expected result
    # where elements: 
    #   0 = coordinates for point A
    #   1 = coordinates for point B
    #   2 = Resulting Manhattan Distance
    # Result calculated using formula: |Xa - Xb| + |Ya - Yb|
    # E.g for points A:(1,3) B:(4,1)
    # |1 - 4| = 3
    # |3 - 1| = 2
    # Manhattan Distance = 3 + 2
    return [
        ((1,3), (4,1), 5),
        ((3,3), (4,8), 6),
        ((1,4), (6,1), 8),
    ]

def test_points(standard_tests):
    for a, b, expected in standard_tests:
        # asterix unpacks tuple into arguments
        assert manhattanDistance(Point(*a), Point(*b)) == expected, "Test points"

def test_swapped_points(standard_tests):
    for a, b, expected in standard_tests:
        # asterix unpacks tuple into arguments
        assert manhattanDistance(Point(*b), Point(*a)) == expected, "Test swapped points"

def test_rotated_points(standard_tests):
    for a, b, expected in standard_tests:
        pointA = Point(a[0], b[1])
        pointB = Point(b[0], a[1])
        assert manhattanDistance(pointA, pointB) == expected, "Test rotated points"
