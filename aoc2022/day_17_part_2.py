import enum
import itertools


class ShapeType(enum.Enum):
    MINUS = "-"
    PLUS = "+"
    L = "L"
    PIPE = "|"
    BLOCK = "■"


class Shape:
    def __init__(self, type_, height, col_from=2):
        self.type_ = type_
        self.height = height
        self.col_from = col_from

    @property
    def za_povecat_max_heights(self):
        return {
            ShapeType.MINUS: [0, 0, 0, 0],
            ShapeType.PLUS: [1, 2, 1],
            ShapeType.L: [0, 0, 2],
            ShapeType.PIPE: [3],
            ShapeType.BLOCK: [1, 1],
        }[self.type_]

    @property
    def za_nivelaciju_oblika(self):
        increases = {
            ShapeType.MINUS: [0, 0, 0, 0],
            ShapeType.PLUS: [1, 0, 1],
            ShapeType.L: [0, 0, 0],
            ShapeType.PIPE: [0],
            ShapeType.BLOCK: [0, 0],
        }[self.type_]
        return [self.height + increase for increase in increases]

    @property
    def width(self):
        return len(self.za_nivelaciju_oblika)

    def move_left(self):
        if self.col_from > 0:
            self.col_from -= 1

    def move_right(self):
        if self.col_from + self.width < 7:
            self.col_from += 1

    def move_down(self):
        self.height -= 1


def solution(input_rel_uri):
    with open(input_rel_uri, encoding="utf-8") as ifile:
        jet_pattern_str = ifile.read().strip()
        jet_pattern = itertools.cycle(jet_pattern_str)
    shape_types = itertools.cycle(
        [ShapeType.MINUS, ShapeType.PLUS, ShapeType.L, ShapeType.PIPE, ShapeType.BLOCK]
    )
    max_heights = [0, 0, 0, 0, 0, 0, 0]
    for n in range(18_000_000):
        shape = Shape(next(shape_types), max(max_heights) + 4)
        for _ in range(3):
            if next(jet_pattern) == "<":
                shape.move_left()
            else:
                shape.move_right()
            shape.move_down()

        jet_push_direction = next(jet_pattern)
        if jet_push_direction == "<":
            shape.move_left()
        else:
            shape.move_right()

        maybe_shape = Shape(shape.type_, shape.height, shape.col_from)
        maybe_shape.move_down()
        if overlap(maybe_shape, max_heights):
            for i in range(shape.width):
                max_heights[shape.col_from + i] = (
                    shape.height + shape.za_povecat_max_heights[i]
                )
            continue
        else:
            shape = maybe_shape

        while True:
            maybe_shape = Shape(shape.type_, shape.height, shape.col_from)
            jet_push_direction = next(jet_pattern)
            if jet_push_direction == "<":
                maybe_shape.move_left()
            else:
                maybe_shape.move_right()
            if not overlap(maybe_shape, max_heights):
                shape = maybe_shape

            maybe_shape = Shape(shape.type_, shape.height, shape.col_from)
            maybe_shape.move_down()
            if overlap(maybe_shape, max_heights):
                for i in range(shape.width):
                    max_heights[shape.col_from + i] = (
                        shape.height + shape.za_povecat_max_heights[i]
                    )
                break
            else:
                shape = maybe_shape
    return max(max_heights)


def overlap(shape, heights):
    return any(
        hs <= hh
        for hs, hh in zip(
            shape.za_nivelaciju_oblika,
            heights[shape.col_from : shape.col_from + shape.width],
        )
    )


if __name__ == "__main__":
    print(solution(f"input/{__file__[-16:][:6]}.txt"))
