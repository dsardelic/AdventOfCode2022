import unittest

from aoc2022 import day_08_part_2


class TestDay08Part2(unittest.TestCase):
    def test_solution(self):
        data = [
            ["input/day_08_example.txt", 8],
            ["input/day_08.txt", 284648],
        ]
        for input_file_rel_uri, exp_solution in data:
            with self.subTest(input_file=input_file_rel_uri):
                self.assertEqual(
                    day_08_part_2.solution(input_file_rel_uri), exp_solution
                )
