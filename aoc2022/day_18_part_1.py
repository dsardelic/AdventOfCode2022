from ast import literal_eval


def solution(input_rel_uri):
    with open(input_rel_uri, encoding="utf-8") as ifile:
        cubes = [literal_eval(f"({row})") for row in ifile.read().strip().split("\n")]
    return sum(
        candidate not in cubes
        for candidate in (
            (x + offset_x, y + offset_y, z + offset_z)
            for x, y, z in cubes
            for offset_x, offset_y, offset_z in (
                (-1, 0, 0),
                (1, 0, 0),
                (0, -1, 0),
                (0, 1, 0),
                (0, 0, -1),
                (0, 0, 1),
            )
        )
    )


if __name__ == "__main__":
    print(solution(f"input/{__file__[-16:][:6]}.txt"))
