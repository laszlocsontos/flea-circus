import sys

import numpy as np


def generate_transition_matrix(grid_size: int) -> np.ndarray:
    dimension = grid_size ** 2
    return np.zeros((dimension, dimension,))


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
