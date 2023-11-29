import unittest

from aoc2022 import day_14_part_2


class TestDay14Part2(unittest.TestCase):
    def test_solution(self):
        data = [
            ["input/day_14_example.txt", 93],
            ["input/day_14.txt", 24813],
        ]
        for input_file_rel_uri, exp_solution in data:
            with self.subTest(input_file=input_file_rel_uri):
                self.assertEqual(
                    day_14_part_2.solution(input_file_rel_uri), exp_solution
                )
