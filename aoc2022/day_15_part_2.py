import collections
import re


def solution(input_rel_uri, max_coord):
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
    return beacon_tuning_frequency(sensors, beacons, max_coord)


def beacon_tuning_frequency(sensors, beacons, max_coord):
    outer_edge_counts = collections.defaultdict(int)
    for beacon in beacons:
        outer_edge_counts[beacon] += 1
    for sensor, beacon in zip(sensors, beacons):
        distance = distance_between(sensor, beacon) + 1
        equidistant1_x = sensor[0] - distance
        equidistant1_y = sensor[1]
        if inside_restricted_area(equidistant1_x, equidistant1_y, max_coord):
            outer_edge_counts[(equidistant1_x, equidistant1_y)] += 1
        equidistant2_x = equidistant1_x
        equidistant2_y = equidistant1_y
        for _ in range(distance):
            equidistant1_x += 1
            equidistant1_y -= 1
            if inside_restricted_area(equidistant1_x, equidistant1_y, max_coord):
                outer_edge_counts[(equidistant1_x, equidistant1_y)] += 1
            equidistant2_x += 1
            equidistant2_y += 1
            if inside_restricted_area(equidistant2_x, equidistant2_y, max_coord):
                outer_edge_counts[(equidistant2_x, equidistant2_y)] += 1
        for _ in range(distance - 1):
            equidistant1_x += 1
            equidistant1_y += 1
            if inside_restricted_area(equidistant1_x, equidistant1_y, max_coord):
                outer_edge_counts[(equidistant1_x, equidistant1_y)] += 1
            equidistant2_x += 1
            equidistant2_y -= 1
            if inside_restricted_area(equidistant2_x, equidistant2_y, max_coord):
                outer_edge_counts[(equidistant2_x, equidistant2_y)] += 1
        equidistant1_x += 1
        equidistant1_y += 1
        if inside_restricted_area(equidistant1_x, equidistant1_y, max_coord):
            outer_edge_counts[(equidistant1_x, equidistant1_y)] += 1

    candidate_positions = [
        point
        for point, count in outer_edge_counts.items()
        if count >= 4
        and all(
            distance_between(point, sensor) > distance_between(sensor, beacon)
            for sensor, beacon in zip(sensors, beacons)
        )
    ]
    assert len(candidate_positions) == 1
    return 4000000 * candidate_positions[0][0] + candidate_positions[0][1]


def distance_between(obj1, obj2):
    return abs(obj1[0] - obj2[0]) + abs(obj1[1] - obj2[1])


def inside_restricted_area(x, y, max_coord):
    return 0 <= x <= max_coord and 0 <= y <= max_coord


if __name__ == "__main__":
    # print(solution(f"input/{__file__[-16:][:6]}_example.txt", 20))
    print(solution(f"input/{__file__[-16:][:6]}.txt", 4000000))
