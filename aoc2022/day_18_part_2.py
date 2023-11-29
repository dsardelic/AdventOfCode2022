import collections
from ast import literal_eval


def solution(input_rel_uri):
    with open(input_rel_uri, encoding="utf-8") as ifile:
        cubes = [literal_eval(f"({row})") for row in ifile.read().strip().split("\n")]
    min_boundaries = [min(coord) - 1 for coord in zip(*cubes)]
    max_boundaries = [max(coord) + 1 for coord in zip(*cubes)]
    area = 0
    visited_points = set(cubes)
    queue = collections.deque([min_boundaries])
    while queue:
        for point in neighboring_points(queue.popleft()):
            if within_boundaries(point, min_boundaries, max_boundaries):
                if point in cubes:
                    area += 1
                if point not in visited_points:
                    visited_points.add(point)
                    queue.append(point)
    return area


def neighboring_points(point):
    return (
        (point[0] + offset_x, point[1] + offset_y, point[2] + offset_z)
        for offset_x, offset_y, offset_z in (
            (-1, 0, 0),
            (1, 0, 0),
            (0, -1, 0),
            (0, 1, 0),
            (0, 0, -1),
            (0, 0, 1),
        )
    )


def within_boundaries(point, min_boundaries, max_boundaries):
    return all(
        min_coord <= coord <= max_coord
        for min_coord, coord, max_coord in zip(min_boundaries, point, max_boundaries)
    )


if __name__ == "__main__":
    print(solution(f"input/{__file__[-16:][:6]}.txt"))
