from shapely.geometry import box
from src.layout import compute_waste


def test_compute_waste_simple():
    fabric = box(0, 0, 10, 10)
    piece = box(0, 0, 5, 5)
    waste = compute_waste(fabric, [piece])
    assert waste == 75
