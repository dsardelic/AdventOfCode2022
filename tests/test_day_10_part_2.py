import unittest

from aoc2022 import day_10_part_2


class TestDay10Part2(unittest.TestCase):
    def test_solution(self):
        exp_solution1 = (
            "##..##..##..##..##..##..##..##..##..##..\n"
            "###...###...###...###...###...###...###.\n"
            "####....####....####....####....####....\n"
            "#####.....#####.....#####.....#####.....\n"
            "######......######......######......####\n"
            "#######.......#######.......#######.....\n"
        )
        exp_solution2 = (
            "###..###....##..##..####..##...##..###..\n"
            "#..#.#..#....#.#..#....#.#..#.#..#.#..#.\n"
            "###..#..#....#.#..#...#..#....#..#.#..#.\n"
            "#..#.###.....#.####..#...#.##.####.###..\n"
            "#..#.#....#..#.#..#.#....#..#.#..#.#....\n"
            "###..#.....##..#..#.####..###.#..#.#....\n"
        )
        data = [
            ["input/day_10_example.txt", exp_solution1],
            ["input/day_10.txt", exp_solution2],
        ]
        for input_file_rel_uri, exp_solution in data:
            with self.subTest(input_file=input_file_rel_uri):
                self.assertEqual(
                    day_10_part_2.solution(input_file_rel_uri), exp_solution
                )
