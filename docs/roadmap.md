# Fabric Cutting Optimization Tool

This document outlines the high level plan and design notes for building a fabric layout optimization tool using **Python**, **Shapely**, and **Genetic Algorithms**.

## 1. Repository Structure and Tooling
- `src/` will contain the main source code.
- `tests/` will hold unit tests.
- `docs/` stores documentation such as this roadmap.
- Consider adding CI to run tests automatically in the future.

## 2. Problem Modeling
- Fabric pieces and patterns are represented as `shapely.geometry.Polygon` objects.
- Each pattern can be rotated and positioned on the fabric.
- Overlap and boundary checks rely on Shapely methods like `intersects` and `within`.

## 3. Fitness Function
- The primary goal is to minimize fabric waste.
- Waste is computed as the fabric area minus the area covered by pieces.
- Additional constraints such as distance between pieces or limited rotation angles can be incorporated.

## 4. Genetic Algorithm Overview
1. **Encoding** – a chromosome contains placement data for each piece (position and rotation).
2. **Population Initialization** – generate random valid layouts.
3. **Selection** – choose parents based on fitness, e.g. roulette wheel or tournament.
4. **Crossover** – combine parent layouts, possibly by exchanging sections.
5. **Mutation** – randomly adjust a piece’s position or rotation while keeping the layout valid.
6. **Termination** – stop after a number of generations or when waste drops below a threshold.

## 5. Interface and Visualization
- Start with a command line interface to provide fabric dimensions and pattern sizes.
- Visualize layouts with a library such as `matplotlib` to inspect results.

## 6. Testing and Validation
- Write unit tests for geometric calculations and GA operations.
- Create a few sample fabric sizes and pattern sets to verify expected behavior.

## 7. Future Extensions
- Support non-rectangular pieces and more complex constraints.
- Improve performance with multiprocessing or alternative heuristics.
- Extend the tool with features like defect mapping or report generation.

