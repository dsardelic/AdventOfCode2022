SEQUENCE_LENGTH = 4


def solution(input_rel_uri):
    with open(input_rel_uri, encoding="utf-8") as ifile:
        buffer = ifile.read().strip()
    if len(set(buffer[:SEQUENCE_LENGTH])) == SEQUENCE_LENGTH:
        return SEQUENCE_LENGTH
    for i in range(1, len(buffer) - SEQUENCE_LENGTH):
        if len(set(buffer[i : i + SEQUENCE_LENGTH])) == SEQUENCE_LENGTH:
            return SEQUENCE_LENGTH + i
    return None


if __name__ == "__main__":
    print(solution(f"input/{__file__[-16:][:6]}.txt"))
