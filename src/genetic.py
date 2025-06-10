"""Simple genetic algorithm skeleton for fabric layout."""
from dataclasses import dataclass
from typing import List
import random
from shapely.geometry import Polygon

from .layout import compute_waste

@dataclass
class Individual:
    pieces: List[Polygon]
    fitness: float = 0.0

    def evaluate(self, fabric: Polygon) -> float:
        self.fitness = -compute_waste(fabric, self.pieces)
        return self.fitness


def mutate(individual: Individual, fabric: Polygon, mutation_rate: float = 0.1) -> None:
    """Randomly translate pieces within the fabric bounds."""
    for piece in individual.pieces:
        if random.random() < mutation_rate:
            dx = random.uniform(-1, 1)
            dy = random.uniform(-1, 1)
            piece.translate(dx, dy)
            if not piece.within(fabric):
                piece.translate(-dx, -dy)


def crossover(parent1: Individual, parent2: Individual) -> Individual:
    """Simple one-point crossover."""
    pivot = len(parent1.pieces) // 2
    new_pieces = parent1.pieces[:pivot] + parent2.pieces[pivot:]
    return Individual(new_pieces)


def select(population: List[Individual]) -> Individual:
    """Roulette wheel selection."""
    total_fitness = sum(ind.fitness for ind in population)
    pick = random.uniform(0, total_fitness)
    current = 0
    for ind in population:
        current += ind.fitness
        if current > pick:
            return ind
    return population[-1]
