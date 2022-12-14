import functools
import itertools


def solution(input_rel_uri):
    with open(input_rel_uri, encoding="utf-8") as ifile:
        flattened_packets = [
            flattened(packet)
            for packet in sorted(
                [
                    eval(packet_str)
                    for packet_str in ifile.read()
                    .strip()
                    .replace("[]", "[-1]")
                    .replace("\n\n", "\n")
                    .split("\n")
                ],
                key=functools.cmp_to_key(in_the_right_order),
            )
        ]
        i, index2, index6 = 0, 0, 0
        while not (index2 and index6):
            if flattened_packets[i]:
                if not index2 and flattened_packets[i][0] >= 2:
                    index2 = i + 1
                if not index6 and flattened_packets[i][0] >= 6:
                    index6 = i + 2
                    break
            i += 1
        return index2 * index6


def flattened(packet):
    def flatten():
        for item in packet:
            try:
                yield from flattened(item)
            except TypeError:
                yield item

    return list(flatten())


def in_the_right_order(left, right):
    match left, right:
        case None, None:
            return 0
        case None, _:
            return -1
        case _, None:
            return 1
        case int(), int():
            return left - right
        case int(), list():
            return in_the_right_order([left], right)
        case list(), int():
            return in_the_right_order(left, [right])
        case [], []:
            return 0
        case list(), list():
            left, right = [
                list(item) for item in zip(*itertools.zip_longest(left, right))
            ]
            return (
                order_of_1st_element
                if (order_of_1st_element := in_the_right_order(left[0], right[0]))
                else in_the_right_order(left[1:], right[1:])
            )


if __name__ == "__main__":
    print(solution(f"input/{__file__[-16:][:6]}.txt"))
