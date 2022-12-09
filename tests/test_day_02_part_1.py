import unittest

from aoc2022 import day_02_part_1


class TestDay01Part1(unittest.TestCase):
    def test_solution(self):
        data = [
            ["input/day_02_example.txt", 15],
            ["input/day_02.txt", 9759],
        ]
        for input_file_rel_uri, exp_solution in data:
            with self.subTest(input_file=input_file_rel_uri):
                self.assertEqual(
                    day_02_part_1.solution(input_file_rel_uri), exp_solution
                )
