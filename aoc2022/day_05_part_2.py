import re


def solution(input_rel_uri):
    with open(input_rel_uri, encoding="utf-8") as ifile:
        stacks_data, instructions = ifile.read().rstrip().split("\n\n")
    stacks = create_stacks(stacks_data)
    for instruction in instructions.split("\n"):
        execute_instruction(instruction, stacks)
    return "".join(stack[-1] for stack in stacks)


def create_stacks(stacks_data):
    stacks_map = stacks_data.split("\n")
    stack_count = (len(stacks_map[0]) + 1) // 4
    stacks = [[] for _ in range(stack_count)]
    for row in stacks_map[:-1]:
        for stack_index in range(stack_count):
            if (crate := row[1 + 4 * stack_index]) != " ":
                stacks[stack_index].insert(0, crate)
    return stacks


def execute_instruction(instruction, stacks):
    quantity, stack_from, stack_to = (
        int(token)
        for token in re.match(r"move (\d+) from (\d) to (\d)", instruction).groups()
    )
    crates = stacks[stack_from - 1][-quantity:]
    stacks[stack_from - 1][-quantity:] = []
    stacks[stack_to - 1].extend(crates)


if __name__ == "__main__":
    print(solution(f"input/{__file__[-16:][:6]}.txt"))
