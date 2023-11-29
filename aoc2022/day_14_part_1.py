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
        cave_slice_row_index = float("-inf")
        min_y, max_y = float("inf"), float("-inf")
        rock_points = set()
        for rock_structure in ifile.read().strip().split("\n"):
            for pair_point1, pair_point2 in itertools.pairwise(
                rock_structure.split(" -> ")
            ):
                point1 = Point(*literal_eval(pair_point1)).reverse()
                point2 = Point(*literal_eval(pair_point2)).reverse()
                cave_slice_row_index = max(cave_slice_row_index, point1.x, point2.x)
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
    cave_slice_col_count = max_y - min_y + 1
    points = [
        [PointType.AIR for _ in range(cave_slice_col_count)]
        for _ in range(cave_slice_row_index + 1)
    ]
    redirects = [
        [(1, 0) for _ in range(cave_slice_col_count)]
        for _ in range(cave_slice_row_index + 1)
    ]
    rock_points = [translate_point(rock_point, -min_y) for rock_point in rock_points]
    for rock_point in rock_points:
        points[rock_point.x][rock_point.y] = PointType.ROCK
        redirects[rock_point.x][rock_point.y] = ("x", "x")
    for rock_point in rock_points:
        update_redirects(redirects, rock_point, points)

    sediment = []
    drop_sand(
        translate_point(Point(0, 500), -min_y),
        points,
        redirects,
        max_obstacle_row_in_col(points),
        sediment,
    )
    return len(sediment)


def drop_sand(starting_point, points, redirects, max_obstacle_rows_in_col, sediment):
    curr_sand_point = starting_point
    while True:
        if forever_falling_reached(curr_sand_point, max_obstacle_rows_in_col, points):
            return
        if redirects[curr_sand_point.x][curr_sand_point.y] == (0, 0):
            points[curr_sand_point.x][curr_sand_point.y] = PointType.SAND
            sediment.append(curr_sand_point)
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


def forever_falling_reached(sand_point, max_obstacle_rows_in_col, cave_slice):
    return (
        not valid_coordinates(sand_point.x, sand_point.y, cave_slice)
        or sand_point.x > max_obstacle_rows_in_col[sand_point.y]
    )


def translate_point(point, offset_y):
    return Point(point.x, point.y + offset_y)


def valid_coordinates(x, y, cave_slice):
    return 0 <= x < len(cave_slice) and 0 <= y < len(cave_slice[0])


def move_sand_grain(point, offset):
    return Point(point.x + offset[0], point.y + offset[1])


def max_obstacle_row_in_col(cave_slice):
    cols = [
        [cave_slice[x][y] for x in range(len(cave_slice))]
        for y in range(len(cave_slice[0]))
    ]
    return [
        -1
        if PointType.ROCK not in col
        else len(col) - col[::-1].index(PointType.ROCK) - 1
        for col in cols
    ]


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
