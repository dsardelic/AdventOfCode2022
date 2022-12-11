import collections
import dataclasses
import functools
from typing import Callable, Deque, List


@dataclasses.dataclass(slots=True)
class Monkey:
    items: Deque[int]
    operation: Callable
    test: Callable
    recipient_indices: List[int]
    inspections: int = 0

    def throw_item(self):
        self.inspections += 1
        item_to_throw = self.operation(self.items.pop()) // 3
        return item_to_throw, self.recipient_indices[self.test(item_to_throw)]

    def receive_item(self, item):
        self.items.appendleft(item)


def solution(input_rel_uri):
    with open(input_rel_uri, encoding="utf-8") as ifile:
        monkey_data = ifile.read().strip().split("\n\n")
    monkeys = initialize_monkeys(monkey_data)
    do_monkey_business(monkeys)
    return functools.reduce(
        int.__mul__,
        (
            monkey.inspections
            for monkey in sorted(
                monkeys, key=lambda monkey: monkey.inspections, reverse=True
            )[:2]
        ),
    )


# pylint: disable=eval-used
def initialize_monkeys(monkey_data):
    monkeys = []
    for monkey_data_group in monkey_data:
        lines = monkey_data_group.split("\n")
        starting_items = eval(
            "[" + lines[1].strip().split("Starting items: ")[1] + "][::-1]"
        )
        operation = eval(
            "lambda old: " + lines[2].strip().split("Operation: new = ")[1]
        )
        test = eval(
            "lambda x: not x % " + lines[3].strip().split("Test: divisible by ")[1]
        )
        recipient_indices = [
            int(lines[5].strip().split("If false: throw to monkey ")[1]),
            int(lines[4].strip().split("If true: throw to monkey ")[1]),
        ]
        monkeys.append(
            Monkey(
                collections.deque(starting_items), operation, test, recipient_indices
            )
        )
    return monkeys


def do_monkey_business(monkeys):
    for _ in range(20):
        for monkey in monkeys:
            for _ in range(len(monkey.items)):
                item, recipient_index = monkey.throw_item()
                monkeys[recipient_index].receive_item(item)


if __name__ == "__main__":
    print(solution(f"input/{__file__[-16:][:6]}.txt"))
