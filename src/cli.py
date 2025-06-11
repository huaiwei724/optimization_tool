"""Command line interface for the optimization tool."""
import argparse
from shapely.geometry import box
from shapely.geometry import Polygon

from .layout import compute_waste


def parse_piece(spec: str) -> Polygon:
    w, h = map(float, spec.split('x'))
    return box(0, 0, w, h)


def main() -> None:
    parser = argparse.ArgumentParser(description="Fabric cutting optimization")
    parser.add_argument("fabric", help="Fabric widthxheight, e.g. 100x50")
    parser.add_argument("pieces", nargs="+", help="Piece sizes, e.g. 10x20")
    args = parser.parse_args()

    fw, fh = map(float, args.fabric.split('x'))
    fabric = box(0, 0, fw, fh)

    pieces = [parse_piece(p) for p in args.pieces]
    waste = compute_waste(fabric, pieces)
    print(f"Waste area: {waste}")


if __name__ == "__main__":
    main()
