def solution(input_rel_uri):
    with open(input_rel_uri, encoding="utf-8") as ifile:
        return filled_crt_buffer(ifile.read().strip().split("\n"))


def filled_crt_buffer(instructions):
    buffer = ""
    register = 1
    instruction_index = 0
    instruction_in_progress = False
    increment = None
    cycle = 1

    while cycle <= 240:
        if (cycle - 1) % 40 in [register - 1, register, register + 1]:
            buffer += "#"
        else:
            buffer += "."
        if instruction_in_progress:
            register += increment
            instruction_in_progress = False
        elif instructions[instruction_index] == "noop":
            instruction_index += 1
        else:
            increment = int(instructions[instruction_index].split(" ")[1])
            instruction_index += 1
            instruction_in_progress = True
        if not cycle % 40:
            buffer += "\n"
        cycle += 1

    return buffer


if __name__ == "__main__":
    print(solution(f"input/{__file__[-16:][:6]}.txt"))
