def solution(input_rel_uri):
    with open(input_rel_uri, encoding="utf-8") as ifile:
        return max(
            sum(int(calories) for calories in calories_group.split("\n"))
            for calories_group in ifile.read().rstrip().split("\n\n")
        )


if __name__ == "__main__":
    print(solution(f"input/{__file__[-16:][:6]}.txt"))
