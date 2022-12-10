import unittest

from aoc2022 import day_09_part_2


class TestDay09Part2(unittest.TestCase):
    def test_solution(self):
        data = [
            ["input/day_09_example1.txt", 1],
            ["input/day_09_example2.txt", 36],
            ["input/day_09.txt", 2372],
        ]
        for input_file_rel_uri, exp_solution in data:
            with self.subTest(input_file=input_file_rel_uri):
                self.assertEqual(
                    day_09_part_2.solution(input_file_rel_uri), exp_solution
                )
