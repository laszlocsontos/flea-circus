import sys
from typing import List

import numpy as np


def generate_next_states(state: int, grid_size: int) -> List[int]:
    next_states = []
    # decompose state number to the coordinate of the grid
    x, y = state // grid_size, state % grid_size
    if x > 0:
        next_states.append((x - 1, y))
    if x < grid_size - 1:
        next_states.append((x + 1, y))
    if y > 0:
        next_states.append((x, y - 1))
    if y < grid_size - 1:
        next_states.append((x, y + 1))
    # convert back to state numbers
    return [(3 * x + y) for x, y in next_states]


def generate_transition_matrix(grid_size: int) -> np.ndarray:
    dimension = grid_size ** 2
    transition_matrix = np.zeros((dimension, dimension))
    for i in range(dimension):
        states = generate_next_states(i, grid_size)
        probability = 1 / len(states)
        for j in states:
            transition_matrix[i][j] = probability
    return transition_matrix


def calc_occupation_densities(transition_matrix: np.ndarray, steps: int) -> np.ndarray:
    return np.zeros(transition_matrix.shape)


def calc_unoccupied_squares(densities: np.ndarray) -> float:
    return 0


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(f'Usage: {sys.argv[0]} <grid size> <iterations>')
        sys.exit(1)

    grid_size = int(sys.argv[1])
    transition_matrix = generate_transition_matrix(grid_size)

    steps = int(sys.argv[2])
    densities = calc_occupation_densities(transition_matrix, steps)

    unoccupied = calc_unoccupied_squares(densities)
    print("{:.6f}".format(unoccupied))
