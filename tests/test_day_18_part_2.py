import unittest

from aoc2022 import day_18_part_2


class TestDay18Part2(unittest.TestCase):
    def test_solution(self):
        data = [
            ["input/day_18_example.txt", 58],
            ["input/day_18.txt", 2006],
        ]
        for input_file_rel_uri, exp_solution in data:
            with self.subTest(input_file=input_file_rel_uri):
                self.assertEqual(
                    day_18_part_2.solution(input_file_rel_uri), exp_solution
                )
