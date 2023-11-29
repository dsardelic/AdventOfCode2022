import unittest

from aoc2022 import day_17_part_1


class TestDay17Part1(unittest.TestCase):
    def test_solution(self):
        data = [
            ["input/day_17_example.txt", 3068],
            ["input/day_17.txt", 3048],
        ]
        for input_file_rel_uri, exp_solution in data:
            with self.subTest(input_file=input_file_rel_uri):
                self.assertEqual(
                    day_17_part_1.solution(input_file_rel_uri), exp_solution
                )
