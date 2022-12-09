def solution(input_rel_uri):
    with open(input_rel_uri, encoding="utf-8") as ifile:
        return sum(
            overlap(sections_range_str_group)
            for sections_range_str_group in ifile.read().strip().split("\n")
        )


def overlap(sections_range_str_group):
    set1, set2 = [
        set(get_range(sections_range_str))
        for sections_range_str in sections_range_str_group.split(",")
    ]
    if set1.intersection(set2):
        return True
    return False


def get_range(sections_range_str):
    section_lo, section_hi = [int(section) for section in sections_range_str.split("-")]
    return range(section_lo, section_hi + 1)


if __name__ == "__main__":
    print(solution(f"input/{__file__[-16:][:6]}.txt"))
