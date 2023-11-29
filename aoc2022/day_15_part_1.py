import re


def solution(input_rel_uri, y):
    with open(input_rel_uri, encoding="utf-8") as ifile:
        sensored_data_str = ifile.read().strip().split("\n")
    sensored_data = [
        re.match(
            (
                r"Sensor at x=(-?\d+), y=(-?\d+): "
                r"closest beacon is at x=(-?\d+), y=(-?\d+)"
            ),
            line,
        )
        for line in sensored_data_str
    ]
    sensors = [(int(match.group(1)), int(match.group(2))) for match in sensored_data]
    beacons = [(int(match.group(3)), int(match.group(4))) for match in sensored_data]
    return range_len_at(y, sensors, beacons)


def range_len_at(y, sensors, beacons):
    no_beacons_x = set()
    for sensor, beacon in zip(sensors, beacons):
        distance = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
        if (offset_y := abs(sensor[1] - y)) <= distance:
            no_beacons_x |= set(
                range(
                    sensor[0] - (distance - offset_y),
                    sensor[0] + (distance - offset_y) + 1,
                )
            )
    beacons_y = set(beacon_x for beacon_x, beacon_y in beacons if beacon_y == y)
    return len(no_beacons_x - beacons_y)


if __name__ == "__main__":
    # print(solution(f"input/{__file__[-16:][:6]}_example.txt", 10))
    print(solution(f"input/{__file__[-16:][:6]}.txt", 2000000))
