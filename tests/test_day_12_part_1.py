import unittest

from aoc2022 import day_12_part_1


class TestDay12Part1(unittest.TestCase):
    def test_solution(self):
        data = [
            ["input/day_12_example.txt", 31],
            ["input/day_12.txt", 528],
        ]
        for input_file_rel_uri, exp_solution in data:
            with self.subTest(input_file=input_file_rel_uri):
                self.assertEqual(
                    day_12_part_1.solution(input_file_rel_uri), exp_solution
                )
