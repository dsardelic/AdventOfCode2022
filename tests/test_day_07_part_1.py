import unittest

from aoc2022 import day_07_part_1


class TestDay07Part1(unittest.TestCase):
    def test_solution(self):
        data = [
            ["input/day_07_example.txt", 95437],
            ["input/day_07.txt", 1449447],
        ]
        for input_file_rel_uri, exp_solution in data:
            with self.subTest(input_file=input_file_rel_uri):
                self.assertEqual(
                    day_07_part_1.solution(input_file_rel_uri), exp_solution
                )
