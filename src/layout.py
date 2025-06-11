from typing import List
from shapely.geometry import Polygon
from shapely.ops import cascaded_union


def compute_waste(fabric: Polygon, pieces: List[Polygon]) -> float:
    """Return the unused fabric area."""
    union = cascaded_union(pieces)
    covered_area = union.intersection(fabric).area
    return fabric.area - covered_area
