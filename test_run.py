import run
import unittest

from unittest.mock import patch


def always_return_zero(min_value, max_value):
    return 0


def return_max_value(min_value, max_value):
    return max_value


def return_specific_values(values):
    for value in values:
        yield value


class TestRunHorseRace(unittest.TestCase):

    def test_run_specific_order(self):
        """
        Test that horses use the rng to decide their order
        """

        order = [3, 2, 1, 0]
        horses = {'first': 10,
                  'second': 5,
                  'third': 30,
                  'fourth': 2}

        expected_result = list(horses.items())

        with patch('run.random.randint') as mock:
            mock.side_effect = return_specific_values(order)
            actual_result = run.run(horses)

        self.assertEqual(expected_result, actual_result, 'Horse order should be as rng')


    def test_run_same_pos(self):
        """
        Two horses arrive in the same position. They should be ordered by power.
        """
        horses = {'lighting_legs': 1000,
                  'dusty_mule': 3}

        expected_result = [('lighting_legs', 1000),
                           ('dusty_mule', 3)]
        
        with patch('run.random.randint') as mock:
            mock.side_effect = always_return_zero
            actual_result = run.run(horses)

        self.assertEqual(expected_result, actual_result, '')


    def test_sample_case(self):
        """
        Test for the input data sample. Order the horses by power.
        """
        horses = {'k1': 15, 'k2': 16, 'k3': 40, 'k5': 45,
                  'k6': 47, 'k7': 67, 'k8': 77, 'k9': 4,
                  'k10': 20, 'k11': 13, 'k12': 19, 
                  'k13': 30, 'k14': 77, 'k15': 14}

        sort_by_last_item = lambda t: t[-1]

        expected_result = list(horses.items())
        expected_result.sort(reverse=True, key=sort_by_last_item)

        with patch('run.random.randint') as mock:
            mock.side_effect = return_max_value
            actual_result = run.run(horses)

        self.assertEqual(expected_result, actual_result, 'Horses should be ordered by power')

