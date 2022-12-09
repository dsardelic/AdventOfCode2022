import unittest

from aoc2022 import day_06_part_2


class TestDay06Part2(unittest.TestCase):
    def test_solution(self):
        data = [
            ["input/day_06_example1.txt", 19],
            ["input/day_06_example2.txt", 23],
            ["input/day_06_example3.txt", 23],
            ["input/day_06_example4.txt", 29],
            ["input/day_06_example5.txt", 26],
            ["input/day_06.txt", 2472],
        ]
        for input_file_rel_uri, exp_solution in data:
            with self.subTest(input_file=input_file_rel_uri):
                self.assertEqual(
                    day_06_part_2.solution(input_file_rel_uri), exp_solution
                )
