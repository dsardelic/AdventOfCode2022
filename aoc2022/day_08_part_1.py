def solution(input_rel_uri):
    with open(input_rel_uri, encoding="utf-8") as ifile:
        heights = [
            [int(height) for height in line]
            for line in ifile.read().strip().split("\n")
        ]
    return len(
        set().union(
            visibles_in_rows(heights, range(len(heights[0]))),
            visibles_in_rows(heights, range(len(heights[0]) - 1, -1, -1)),
            visibles_in_cols(heights, range(len(heights))),
            visibles_in_cols(heights, range(len(heights) - 1, -1, -1)),
        )
    )


def visibles_in_rows(heights, col_range):
    visibles = set()
    for i, row in enumerate(heights):
        row_visibles = set()
        curr_max_visible_height = -1
        for j in col_range:
            curr_height = row[j]
            if curr_height > curr_max_visible_height:
                row_visibles.add((i, j))
                curr_max_visible_height = curr_height
        visibles |= row_visibles
    return visibles


def visibles_in_cols(heights, row_range):
    visibles = set()
    for j in range(len(heights[0])):
        col_visibles = set()
        curr_max_visible_height = -1
        for i in row_range:
            curr_height = heights[i][j]
            if curr_height > curr_max_visible_height:
                col_visibles.add((i, j))
                curr_max_visible_height = curr_height
        visibles |= col_visibles
    return visibles


if __name__ == "__main__":
    print(solution(f"input/{__file__[-16:][:6]}.txt"))
