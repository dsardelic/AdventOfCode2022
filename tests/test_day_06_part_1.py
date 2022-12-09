import unittest

from aoc2022 import day_06_part_1


class TestDay06Part1(unittest.TestCase):
    def test_solution(self):
        data = [
            ["input/day_06_example1.txt", 7],
            ["input/day_06_example2.txt", 5],
            ["input/day_06_example3.txt", 6],
            ["input/day_06_example4.txt", 10],
            ["input/day_06_example5.txt", 11],
            ["input/day_06.txt", 1034],
        ]
        for input_file_rel_uri, exp_solution in data:
            with self.subTest(input_file=input_file_rel_uri):
                self.assertEqual(
                    day_06_part_1.solution(input_file_rel_uri), exp_solution
                )
