def solution(input_rel_uri):
    with open(input_rel_uri, encoding="utf-8") as ifile:
        rucksacks = ifile.read().strip().split("\n")
    return sum(
        get_priority(find_common_item(rucksacks[i : i + 3]))
        for i in range(0, len(rucksacks), 3)
    )


def get_priority(item):
    if ord("a") <= ord(item) <= ord("z"):
        return ord(item) - ord("a") + 1
    if ord("A") <= ord(item) <= ord("Z"):
        return ord(item) - ord("A") + 27
    return None


def find_common_item(rucksacks):
    common_items = set(rucksacks[0]).intersection(
        *[set(rucksack) for rucksack in rucksacks]
    )
    # assert len(common_items) == 1
    return common_items.pop()


if __name__ == "__main__":
    print(solution(f"input/{__file__[-16:][:6]}.txt"))
