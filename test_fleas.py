import unittest

from fleas import *

TRANSITION_MATRIX = np.array([
    [0, 1 / 2, 0, 1 / 2, 0, 0, 0, 0, 0],
    [1 / 3, 0, 1 / 3, 0, 1 / 3, 0, 0, 0, 0],
    [0, 1 / 2, 0, 0, 0, 1 / 2, 0, 0, 0],
    [1 / 3, 0, 0, 0, 1 / 3, 0, 1 / 3, 0, 0],
    [0, 1 / 4, 0, 1 / 4, 0, 1 / 4, 0, 1 / 4, 0],
    [0, 0, 1 / 3, 0, 1 / 3, 0, 0, 0, 1 / 3],
    [0, 0, 0, 1 / 2, 0, 0, 0, 1 / 2, 0],
    [0, 0, 0, 0, 1 / 3, 0, 1 / 3, 0, 1 / 3],
    [0, 0, 0, 0, 0, 1 / 2, 0, 1 / 2, 0]
])

DENSITIES = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1 / 3, 0, 0, 0, 1 / 3, 0, 1 / 3, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1 / 3, 0, 1 / 3, 0, 0, 0, 1 / 3],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
])


class FleaTests(unittest.TestCase):

    def test_generate_transition_matrix(self):
        np.testing.assert_array_almost_equal(generate_transition_matrix(3), TRANSITION_MATRIX)

    def test_calc_occupation_densities(self):
        np.testing.assert_array_almost_equal(calc_occupation_densities(TRANSITION_MATRIX, 1), DENSITIES)

    def test_calc_unoccupied_squares(self):
        self.assertAlmostEqual(64 / 9, calc_unoccupied_squares(DENSITIES), 6)


if __name__ == '__main__':
    unittest.main()
