import unittest

from aoc2022 import day_11_part_1


class TestDay11Part1(unittest.TestCase):
    def test_solution(self):
        data = [
            ["input/day_11_example.txt", 10605],
            ["input/day_11.txt", 99840],
        ]
        for input_file_rel_uri, exp_solution in data:
            with self.subTest(input_file=input_file_rel_uri):
                self.assertEqual(
                    day_11_part_1.solution(input_file_rel_uri), exp_solution
                )
