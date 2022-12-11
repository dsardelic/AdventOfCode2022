import functools


def solution(input_rel_uri):
    with open(input_rel_uri, encoding="utf-8") as ifile:
        heights = [
            [int(height) for height in line]
            for line in ifile.read().strip().split("\n")
        ]
    return max(
        scenic_score(heights, x, y)
        for x, row in enumerate(heights)
        for y, _ in enumerate(row)
    )


def scenic_score(heights, x, y):
    return functools.reduce(
        int.__mul__,
        (
            viewing_distance(heights[x][y], view_direction(heights, x, y))
            for view_direction in [view_right, view_left, view_down, view_up]
        ),
    )


def view_right(heights, x, y):
    return heights[x][y + 1 :]


def view_left(heights, x, y):
    return heights[x][:y][::-1]


def view_down(heights, x, y):
    return [heights[x][y] for x in range(x + 1, len(heights))]


def view_up(heights, x, y):
    return [heights[x][y] for x in range(x)][::-1]


def viewing_distance(max_height, view):
    if not view:
        return 0
    curr_viewing_distance = 0
    for height in view:
        curr_viewing_distance += 1
        if height >= max_height:
            break
    return curr_viewing_distance


if __name__ == "__main__":
    print(solution(f"input/{__file__[-16:][:6]}.txt"))
