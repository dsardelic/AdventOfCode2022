import unittest

from aoc2022 import day_25_part_1


class TestDay25Part1(unittest.TestCase):
    def test_solution(self):
        data = [
            ["input/day_25_example.txt", "2=-1=0"],
            ["input/day_25.txt", "20-1-0=-2=-2220=0011"],
        ]
        for input_file_rel_uri, exp_solution in data:
            with self.subTest(input_file=input_file_rel_uri):
                self.assertEqual(
                    day_25_part_1.solution(input_file_rel_uri), exp_solution
                )

    def test_decimal_number_to_snafu_number(self):
        data = [
            [1, "1"],
            [2, "2"],
            [3, "1="],
            [4, "1-"],
            [5, "10"],
            [6, "11"],
            [7, "12"],
            [8, "2="],
            [9, "2-"],
            [10, "20"],
            [15, "1=0"],
            [20, "1-0"],
            [2022, "1=11-2"],
            [12345, "1-0---0"],
            [314159265, "1121-1110-1=0"],
        ]
        for decimal_number, exp_snafu_number in data:
            with self.subTest(
                decimal_number=decimal_number, exp_snafu_number=exp_snafu_number
            ):
                self.assertEqual(
                    day_25_part_1.decimal_number_to_snafu_number(decimal_number),
                    exp_snafu_number,
                )

    def test_snafu_number_to_decimal_number(self):
        data = [
            ["1=-0-2", 1747],
            ["12111", 906],
            ["2=0=", 198],
            ["21", 11],
            ["2=01", 201],
            ["111", 31],
            ["20012", 1257],
            ["112", 32],
            ["1=-1=", 353],
            ["1-12", 107],
            ["12", 7],
            ["1=", 3],
            ["122", 37],
        ]
        for snafu_number, exp_decimal_number in data:
            with self.subTest(
                snafu_number=snafu_number, exp_decimal_number=exp_decimal_number
            ):
                self.assertEqual(
                    day_25_part_1.snafu_number_to_decimal_number(snafu_number),
                    exp_decimal_number,
                )
