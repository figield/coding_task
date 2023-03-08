import unittest

from tasks import ox


class TestMatrixTools(unittest.TestCase):

    def test_diagonal_1(self):
        matrix = [[1, 0, 0],
                  [0, 1, 0],
                  [0, 0, 1]]
        given = ox.check_diagonal_1(matrix, 1)
        expected = True
        self.assertEqual(expected, given)

    def test_diagonal_2(self):
        matrix = [[0, 0, 1],
                  [0, 1, 0],
                  [1, 0, 0]]
        given = ox.check_diagonal_2(matrix, 1)
        expected = True
        self.assertEqual(expected, given)

    def test_rows(self):
        matrix = [[1, 1, 1],
                  [0, 1, 0],
                  [1, 0, 0]]
        given = ox.check_rows(matrix, 1)
        expected = True
        self.assertEqual(expected, given)

    def test_columns(self):
        matrix = [[1, 0, 0],
                  [1, 0, 0],
                  [1, 0, 0]]
        given = ox.check_columns(matrix, 1)
        expected = True
        self.assertEqual(expected, given)

    def test_all_rules(self):
        matrix = [[0, 0, 1],
                  [0, 1, 0],
                  [1, 0, 0]]
        given = ox.check_result(matrix, 1)
        expected = True
        self.assertEqual(expected, given)
