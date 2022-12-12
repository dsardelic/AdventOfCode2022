def solution(input_rel_uri):
    with open(input_rel_uri, encoding="utf-8") as ifile:
        area = []
        for x, row in enumerate(ifile.read().strip().split("\n")):
            if "S" in row:
                row = row.replace("S", "a")
            if "E" in row:
                start_pos = (x, row.index("E"))
                row = row.replace("E", "z")
            area.append(row)
    return bfs(start_pos, area)


def are_valid_coordinates(x, y, area):
    return 0 <= x < len(area) and 0 <= y < len(area[0])


def neighbor_is_goal(curr_elevation, neighbor_elevation):
    return curr_elevation == "b" and neighbor_elevation == "a"


def shorter_path_found(curr_min_steps, neighbor_min_steps):
    return curr_min_steps <= neighbor_min_steps


def acceptable_elevation_difference_to_neighbor(curr_elevation, neighbor_elevation):
    return ord(curr_elevation) - ord(neighbor_elevation) <= 1


def bfs(start_pos, area):
    offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    min_steps = [[float("inf")] * len(area[0]) for _ in range(len(area))]
    min_steps[start_pos[0]][start_pos[1]] = 0
    explore_from_positions = {start_pos}
    while explore_from_positions:
        new_explore_from_positions = set()
        for curr_x, curr_y in explore_from_positions:
            curr_elevation = area[curr_x][curr_y]
            for offset in offsets:
                if are_valid_coordinates(
                    neighbor_x := curr_x + offset[0],
                    neighbor_y := curr_y + offset[1],
                    area,
                ):
                    neighbor_elevation = area[neighbor_x][neighbor_y]
                    curr_min_steps = min_steps[curr_x][curr_y]
                    neighbor_min_steps = min_steps[neighbor_x][neighbor_y]

                    if neighbor_is_goal(
                        curr_elevation, neighbor_elevation
                    ) and shorter_path_found(curr_min_steps, neighbor_min_steps):
                        return curr_min_steps + 1

                    if acceptable_elevation_difference_to_neighbor(
                        curr_elevation, neighbor_elevation
                    ) and shorter_path_found(curr_min_steps, neighbor_min_steps):
                        min_steps[neighbor_x][neighbor_y] = curr_min_steps + 1
                        new_explore_from_positions.add((neighbor_x, neighbor_y))

        explore_from_positions = new_explore_from_positions


if __name__ == "__main__":
    print(solution(f"input/{__file__[-16:][:6]}.txt"))
