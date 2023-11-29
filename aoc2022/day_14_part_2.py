import dataclasses
import enum
import itertools
from ast import literal_eval


class PointType(enum.Enum):
    ROCK = "#"
    AIR = "."
    SAND = "o"

    def __repr__(self):
        return self.value


@dataclasses.dataclass(frozen=True, slots=True, order=True)
class Point:
    x: int
    y: int

    def reverse(self):
        return type(self)(self.y, self.x)


def solution(input_rel_uri):
    with open(input_rel_uri, encoding="utf-8") as ifile:
        max_x = float("-inf")
        min_y, max_y = float("inf"), float("-inf")
        rock_points = set()
        for rock_structure in ifile.read().strip().split("\n"):
            for pair_point1, pair_point2 in itertools.pairwise(
                rock_structure.split(" -> ")
            ):
                point1 = Point(*literal_eval(pair_point1)).reverse()
                point2 = Point(*literal_eval(pair_point2)).reverse()
                max_x = max(max_x, point1.x, point2.x)
                min_y = min(min_y, point1.y, point2.y)
                max_y = max(max_y, point1.y, point2.y)
                if point1.x == point2.x:
                    rock_points |= {
                        Point(point1.x, y)
                        for y in range(
                            min(point1.y, point2.y), max(point1.y, point2.y) + 1
                        )
                    }
                elif point1.y == point2.y:
                    rock_points |= {
                        Point(x, point1.y)
                        for x in range(
                            min(point1.x, point2.x), max(point1.x, point2.x) + 1
                        )
                    }
    max_x, min_y, max_y = add_cave_slice_bottom(rock_points, max_x, min_y, max_y, 500)
    cave_slice_col_count = max_y - min_y + 1
    points = [
        [PointType.AIR for _ in range(cave_slice_col_count)] for _ in range(max_x + 1)
    ]
    redirects = [
        [(1, 0) for _ in range(cave_slice_col_count)] for _ in range(max_x + 1)
    ]
    rock_points = [translate_point(rock_point, -min_y) for rock_point in rock_points]
    for rock_point in rock_points:
        points[rock_point.x][rock_point.y] = PointType.ROCK
        redirects[rock_point.x][rock_point.y] = ("x", "x")
    for rock_point in rock_points:
        update_redirects(redirects, rock_point, points)

    drop_sand(translate_point(Point(0, 500), -min_y), points, redirects)
    return sum(
        point == PointType.SAND for point in itertools.chain.from_iterable(points)
    )


def add_cave_slice_bottom(rock_points, max_x, min_y, max_y, start_y):
    max_x += 2
    min_y = min(min_y - 5, start_y - max_x)
    max_y = max(max_y + 5, start_y + max_x)
    rock_points |= set((Point(max_x, y) for y in range(min_y, max_y + 1)))
    return max_x, min_y, max_y


def drop_sand(starting_point, points, redirects):
    curr_sand_point = starting_point
    while True:
        if redirects[curr_sand_point.x][curr_sand_point.y] == (0, 0):
            points[curr_sand_point.x][curr_sand_point.y] = PointType.SAND
            if curr_sand_point == starting_point:
                return
            update_redirects(redirects, curr_sand_point, points)
            curr_sand_point = starting_point
        else:
            maybe_new_sand_point = move_sand_grain(
                curr_sand_point, redirects[curr_sand_point.x][curr_sand_point.y]
            )
            if not valid_coordinates(
                maybe_new_sand_point.x, maybe_new_sand_point.y, points
            ):
                return
            curr_sand_point = maybe_new_sand_point


def translate_point(point, offset_y):
    return Point(point.x, point.y + offset_y)


def valid_coordinates(x, y, cave_slice):
    return 0 <= x < len(cave_slice) and 0 <= y < len(cave_slice[0])


def move_sand_grain(point, offset):
    return Point(point.x + offset[0], point.y + offset[1])


def point_is_blocked(point, points):
    return points[point.x][point.y] in [PointType.ROCK, PointType.SAND]


def update_redirects(redirects, point_to, points):
    def redirect_diag_left(x, y):
        if not valid_coordinates(x + 1, y - 1, redirects) or (
            valid_coordinates(x + 1, y - 1, redirects)
            and not point_is_blocked(Point(x + 1, y - 1), points)
        ):
            redirects[x][y] = (1, -1)
            return "success"
        return None

    def redirect_diag_right(x, y):
        if not valid_coordinates(x + 1, y + 1, redirects) or (
            valid_coordinates(x + 1, y + 1, redirects)
            and not point_is_blocked(Point(x + 1, y + 1), points)
        ):
            redirects[x][y] = (1, 1)
            return "success"
        return None

    def stop_redirect(x, y):
        redirects[x][y] = (0, 0)

    x = point_to.x
    y = point_to.y

    if valid_coordinates(x - 1, y, redirects) and redirects[x - 1][y] == (1, 0):
        _ = (
            redirect_diag_left(x - 1, y)
            or redirect_diag_right(x - 1, y)
            or stop_redirect(x - 1, y)
        )

    if valid_coordinates(x - 1, y + 1, redirects) and redirects[x - 1][y + 1] == (
        1,
        -1,
    ):
        _ = redirect_diag_right(x - 1, y + 1) or stop_redirect(x - 1, y + 1)

    if valid_coordinates(x - 1, y - 1, redirects) and redirects[x - 1][y - 1] == (1, 1):
        stop_redirect(x - 1, y - 1)


if __name__ == "__main__":
    print(solution(f"input/{__file__[-16:][:6]}.txt"))
