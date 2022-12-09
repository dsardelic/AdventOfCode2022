from enum import Enum


class Choice(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


mappings = {
    "A": Choice.ROCK,
    "B": Choice.PAPER,
    "C": Choice.SCISSORS,
    "X": Choice.ROCK,
    "Y": Choice.PAPER,
    "Z": Choice.SCISSORS,
}


def outcome_points(opponent_choice, my_choice):
    if opponent_choice == my_choice:
        return 3
    match opponent_choice, my_choice:
        case Choice.ROCK, Choice.PAPER:
            return 6
        case Choice.PAPER, Choice.SCISSORS:
            return 6
        case Choice.SCISSORS, Choice.ROCK:
            return 6
    return 0


def score(opponent_choice, my_choice):
    return outcome_points(opponent_choice, my_choice) + my_choice.value


def solution(input_rel_uri):
    with open(input_rel_uri, encoding="utf-8") as ifile:
        return sum(
            score(*[mappings[letter] for letter in line.split()])
            for line in ifile.read().strip().split("\n")
        )


if __name__ == "__main__":
    print(solution(f"input/{__file__[-16:][:6]}.txt"))
