from enum import Enum


class Choice(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class Outcome(Enum):
    WIN = 6
    DRAW = 3
    LOSS = 0


mappings = {
    "A": Choice.ROCK,
    "B": Choice.PAPER,
    "C": Choice.SCISSORS,
    "X": Outcome.LOSS,
    "Y": Outcome.DRAW,
    "Z": Outcome.WIN,
}


def my_choice(opponent_choice, outcome):
    if outcome == Outcome.WIN:
        return {
            Choice.PAPER: Choice.SCISSORS,
            Choice.ROCK: Choice.PAPER,
            Choice.SCISSORS: Choice.ROCK,
        }[opponent_choice]
    if outcome == Outcome.LOSS:
        return {
            Choice.PAPER: Choice.ROCK,
            Choice.ROCK: Choice.SCISSORS,
            Choice.SCISSORS: Choice.PAPER,
        }[opponent_choice]
    return opponent_choice


def score(opponent_choice, outcome):
    return outcome.value + my_choice(opponent_choice, outcome).value


def solution(input_rel_uri):
    with open(input_rel_uri, encoding="utf-8") as ifile:
        return sum(
            score(*[mappings[letter] for letter in line.split()])
            for line in ifile.read().strip().split("\n")
        )


if __name__ == "__main__":
    print(solution(f"input/{__file__[-16:][:6]}.txt"))
