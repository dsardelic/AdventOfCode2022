import unittest

from aoc2022 import day_15_part_1


class TestDay15Part1(unittest.TestCase):
    def test_solution(self):
        data = [
            ["input/day_15_example.txt", 10, 26],
            ["input/day_15.txt", 2000000, 5838453],
        ]
        for input_file_rel_uri, row, exp_solution in data:
            with self.subTest(input_file=input_file_rel_uri):
                self.assertEqual(
                    day_15_part_1.solution(input_file_rel_uri, row), exp_solution
                )
