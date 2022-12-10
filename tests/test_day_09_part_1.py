import unittest

from aoc2022 import day_09_part_1


class TestDay09Part1(unittest.TestCase):
    def test_solution(self):
        data = [
            ["input/day_09_example1.txt", 13],
            ["input/day_09.txt", 5683],
        ]
        for input_file_rel_uri, exp_solution in data:
            with self.subTest(input_file=input_file_rel_uri):
                self.assertEqual(
                    day_09_part_1.solution(input_file_rel_uri), exp_solution
                )
