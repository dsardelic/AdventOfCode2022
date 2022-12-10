def solution(input_rel_uri):
    with open(input_rel_uri, encoding="utf-8") as ifile:
        return sum(get_signal_strengths(ifile.read().strip().split("\n")))


def get_signal_strengths(instructions):
    signal_strengths = []
    cycle_thresholds = [20, 60, 100, 140, 180, 220]
    register = 1
    cycle = 1
    cycle_threshold_index = 0
    instruction_index = 0
    instruction_in_progress = False
    increment = None

    while True:
        if cycle == cycle_thresholds[cycle_threshold_index]:
            signal_strengths.append(register * cycle_thresholds[cycle_threshold_index])
            cycle_threshold_index += 1
            if cycle_threshold_index == len(cycle_thresholds):
                return signal_strengths

        if instruction_in_progress:
            register += increment
            instruction_in_progress = False
        elif instructions[instruction_index] == "noop":
            instruction_index += 1
        else:
            increment = int(instructions[instruction_index].split(" ")[1])
            instruction_index += 1
            instruction_in_progress = True
        cycle += 1


if __name__ == "__main__":
    print(solution(f"input/{__file__[-16:][:6]}.txt"))
