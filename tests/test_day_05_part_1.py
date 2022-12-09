import unittest

from aoc2022 import day_05_part_1


class TestDay05Part1(unittest.TestCase):
    def test_solution(self):
        data = [
            ["input/day_05_example.txt", "CMZ"],
            ["input/day_05.txt", "TGWSMRBPN"],
        ]
        for input_file_rel_uri, exp_solution in data:
            with self.subTest(input_file=input_file_rel_uri):
                self.assertEqual(
                    day_05_part_1.solution(input_file_rel_uri), exp_solution
                )
