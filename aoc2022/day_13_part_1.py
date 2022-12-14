import itertools


def solution(input_rel_uri):
    with open(input_rel_uri, encoding="utf-8") as ifile:
        return sum(
            i + 1
            for i, packet_str_group in enumerate(ifile.read().strip().split("\n\n"))
            if in_the_right_order(
                *(eval(packet_str) for packet_str in packet_str_group.split("\n"))
            )
        )


def in_the_right_order(left, right):
    match left, right:
        case None, None:
            return None
        case None, _:
            return True
        case _, None:
            return False
        case int(), int():
            return None if left == right else left < right
        case int(), list():
            return in_the_right_order([left], right)
        case list(), int():
            return in_the_right_order(left, [right])
        case [], []:
            return None
        case list(), list():
            left, right = [
                list(item) for item in zip(*itertools.zip_longest(left, right))
            ]
            return (
                order_of_1st_element
                if (order_of_1st_element := in_the_right_order(left[0], right[0]))
                is not None
                else in_the_right_order(left[1:], right[1:])
            )


if __name__ == "__main__":
    print(solution(f"input/{__file__[-16:][:6]}.txt"))
