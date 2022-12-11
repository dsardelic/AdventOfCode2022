import dataclasses


@dataclasses.dataclass(frozen=True, slots=True)
class Position:
    x: int
    y: int


def solution(input_rel_uri):
    with open(input_rel_uri, encoding="utf-8") as ifile:
        return len(get_trail(ifile.read().strip().split("\n")))


def get_trail(motions):
    tail_trail = {Position(0, 0)}
    knots_count = 10
    knots = [Position(0, 0)] * knots_count
    for motion in motions:
        direction, step_count_str = motion.split(" ")
        for _ in range(int(step_count_str)):
            knots[0] = move_head(knots[0], direction)
            for i in range(1, knots_count):
                knots[i] = move_tail(knots[i], knots[i - 1])
                if i == knots_count - 1:
                    tail_trail.add(knots[i])
    return tail_trail


def move_head(head, direction):
    offsets = {
        "R": (0, 1),
        "L": (0, -1),
        "U": (-1, 0),
        "D": (1, 0),
    }
    return Position(
        head.x + offsets[direction][0],
        head.y + offsets[direction][1],
    )


def move_tail(tail, head):
    if abs(tail.x - head.x) == 2 and abs(tail.y - head.y) == 2:
        return Position(
            tail.x + 1 if head.x > tail.x else tail.x - 1,
            tail.y + 1 if head.y > tail.y else tail.y - 1,
        )
    if abs(tail.x - head.x) == 2:
        return Position(
            tail.x + 1 if head.x > tail.x else tail.x - 1,
            head.y,
        )
    if abs(tail.y - head.y) == 2:
        return Position(
            head.x,
            tail.y + 1 if head.y > tail.y else tail.y - 1,
        )
    return tail


if __name__ == "__main__":
    print(solution(f"input/{__file__[-16:][:6]}.txt"))
