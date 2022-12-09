import unittest

from aoc2022 import day_03_part_1


class TestDay03Part1(unittest.TestCase):
    def test_solution(self):
        data = [
            ["input/day_03_example.txt", 157],
            ["input/day_03.txt", 7785],
        ]
        for input_file_rel_uri, exp_solution in data:
            with self.subTest(input_file=input_file_rel_uri):
                self.assertEqual(
                    day_03_part_1.solution(input_file_rel_uri), exp_solution
                )
