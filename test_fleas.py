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

    def test_generate_next_states(self):
        self.assertEqual([3, 7], generate_next_states(6, 3))

    def test_generate_transition_matrix(self):
        np.testing.assert_array_almost_equal(generate_transition_matrix(3), TRANSITION_MATRIX)

    def test_calc_occupation_densities(self):
        initial_state = np.zeros(TRANSITION_MATRIX.shape)
        initial_state[3][3] = 1
        initial_state[5][5] = 1
        np.testing.assert_array_almost_equal(calc_occupation_densities(initial_state, TRANSITION_MATRIX, 1), DENSITIES)

    def test_calc_unoccupied_squares(self):
        self.assertAlmostEqual(64 / 9, calc_unoccupied_squares(DENSITIES), 6)


if __name__ == '__main__':
    unittest.main()
