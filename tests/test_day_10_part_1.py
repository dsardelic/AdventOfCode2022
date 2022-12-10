import unittest

from aoc2022 import day_10_part_1


class TestDay10Part1(unittest.TestCase):
    def test_solution(self):
        data = [
            ["input/day_10_example.txt", 13140],
            ["input/day_10.txt", 15140],
        ]
        for input_file_rel_uri, exp_solution in data:
            with self.subTest(input_file=input_file_rel_uri):
                self.assertEqual(
                    day_10_part_1.solution(input_file_rel_uri), exp_solution
                )
