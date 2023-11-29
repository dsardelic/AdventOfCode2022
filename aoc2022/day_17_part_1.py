import enum
import itertools


class FieldType(enum.Enum):
    AIR = "."
    FALLING_ROCK = "@"
    LANDED_ROCK = "#"

    def __repr__(self):
        return self.value


class ShapeType(enum.Enum):
    MINUS = "-"
    PLUS = "+"
    L = "L"
    PIPE = "|"
    BLOCK = "■"

    def __repr__(self):
        return self.value


class Shape:
    def __init__(self, shape_type, x=None, y=None):
        self.type_ = shape_type
        self.x = x
        self.y = y

    @property
    def width(self):
        return {
            ShapeType.MINUS: 4,
            ShapeType.PLUS: 3,
            ShapeType.L: 3,
            ShapeType.PIPE: 1,
            ShapeType.BLOCK: 2,
        }[self.type_]

    @property
    def height(self):
        return {
            ShapeType.MINUS: 1,
            ShapeType.PLUS: 3,
            ShapeType.L: 3,
            ShapeType.PIPE: 4,
            ShapeType.BLOCK: 2,
        }[self.type_]

    @property
    def rock_points_offsets(self):
        return {
            ShapeType.MINUS: {(0, 0), (0, 1), (0, 2), (0, 3)},
            ShapeType.PLUS: {(0, 1), (-1, 0), (-1, 1), (-1, 2), (-2, 1)},
            ShapeType.L: {(0, 2), (-1, 2), (-2, 0), (-2, 1), (-2, 2)},
            ShapeType.PIPE: {(0, 0), (-1, 0), (-2, 0), (-3, 0)},
            ShapeType.BLOCK: {(0, 0), (0, 1), (-1, 0), (-1, 1)},
        }[self.type_]

    @property
    def clear_chamber_rows_required(self):
        return 3 + self.height

    def offset_point(self, offset):
        return self.x + offset[0], self.y + offset[1]

    def translated_by(self, offset):
        return Shape(self.type_, *self.offset_point(offset))


class Chamber:
    def __init__(self):
        self.fields = []

    def get_height(self):
        for i, row in enumerate(self.fields[::-1]):
            if any(field == FieldType.LANDED_ROCK for field in row):
                return len(self.fields) - i
        return 0

    def remove_top_rows_with_air_only(self):
        while self.fields and all(field == FieldType.AIR for field in self.fields[-1]):
            del self.fields[-1]

    def field_at(self, point):
        return self.fields[point[0]][point[1]]

    def valid_boundaries_of(self, shape):
        return 0 <= shape.y <= 7 - shape.width and shape.x >= shape.height - 1

    def landed_rocks_overlap_with(self, shape):
        return any(
            self.field_at(shape.offset_point(rock_point_offset))
            == FieldType.LANDED_ROCK
            for rock_point_offset in shape.rock_points_offsets
        )

    def mark_landed(self, shape):
        for rock_point_offset in shape.rock_points_offsets:
            self.fields[shape.x + rock_point_offset[0]][
                shape.y + rock_point_offset[1]
            ] = FieldType.LANDED_ROCK

    def spawn_new(self, shape):
        shape.x = len(self.fields) - 1
        shape.y = 2

    def enlarge_to_fit(self, shape):
        self.remove_top_rows_with_air_only()
        self.fields.extend(
            [[FieldType.AIR] * 7 for _ in range(shape.clear_chamber_rows_required)]
        )

    def __str__(self):
        return (
            "\n".join(
                " ".join([field.value for field in row]) for row in self.fields[::-1]
            )
            + "\n"
            + "-" * 13
        )


def solution(input_rel_uri):
    with open(input_rel_uri, encoding="utf-8") as ifile:
        jet_pattern = itertools.cycle(ifile.read().strip())
    jet_offsets = {
        ">": (0, 1),
        "<": (0, -1),
    }
    shape_types = itertools.cycle(
        [ShapeType.MINUS, ShapeType.PLUS, ShapeType.L, ShapeType.PIPE, ShapeType.BLOCK]
    )
    chamber = Chamber()
    spawn_shape = True
    shape_count = 0
    while True:
        if spawn_shape:
            shape_count += 1
            shape = Shape(next(shape_types))
            chamber.enlarge_to_fit(shape)
            chamber.spawn_new(shape)
            spawn_shape = False
        jet_offset_str = next(jet_pattern)
        offset_shape = shape.translated_by(jet_offsets[jet_offset_str])
        if chamber.valid_boundaries_of(
            offset_shape
        ) and not chamber.landed_rocks_overlap_with(offset_shape):
            shape = offset_shape
        offset_shape = shape.translated_by((-1, 0))
        if chamber.valid_boundaries_of(offset_shape):
            if chamber.landed_rocks_overlap_with(offset_shape):
                chamber.mark_landed(shape)
                if shape_count == 2022:
                    return chamber.get_height()
                spawn_shape = True
            else:
                shape = offset_shape
        else:
            chamber.mark_landed(shape)
            if shape_count == 2022:
                return chamber.get_height()
            spawn_shape = True


if __name__ == "__main__":
    print(solution(f"input/{__file__[-16:][:6]}.txt"))
