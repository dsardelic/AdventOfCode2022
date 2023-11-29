def solution(input_rel_uri):
    with open(input_rel_uri, encoding="utf-8") as ifile:
        return decimal_number_to_snafu_number(
            sum(
                snafu_number_to_decimal_number(snafu_number)
                for snafu_number in ifile.read().strip().split("\n")
            )
        )


def decimal_number_to_snafu_number(decimal_number):
    return base5_str_to_snafu_number(decimal_number_to_base5_str(decimal_number))


def decimal_number_to_base5_str(decimal_number):
    if not decimal_number:
        return "0"
    digits = []
    while decimal_number:
        digits.append(int(decimal_number % 5))
        decimal_number //= 5
    return "".join(str(digit) for digit in digits[::-1])


def base5_str_to_snafu_number(base5_str):
    balanced_base5_digits = []
    carry = 0
    for base5_digit_str in base5_str[::-1]:
        match (base5_digit := int(base5_digit_str) + carry):
            case 0 | 1 | 2:
                balanced_base5_digits.append(base5_digit)
                carry = 0
            case 3:
                balanced_base5_digits.append(-2)
                carry = 1
            case 4:
                balanced_base5_digits.append(-1)
                carry = 1
            case 5:
                balanced_base5_digits.append(0)
                carry = 1
    if carry:
        balanced_base5_digits.append(carry)
    return "".join(
        base5_digit_to_snafu_digit(digit) for digit in balanced_base5_digits[::-1]
    )


def base5_digit_to_snafu_digit(base5_digit):
    match base5_digit:
        case -2:
            return "="
        case -1:
            return "-"
        case _:
            return str(base5_digit)


def snafu_number_to_decimal_number(b5_digits):
    return sum(
        snafu_digit_to_balanced_base5_digit(digit) * 5**i
        for i, digit in enumerate(b5_digits[::-1])
    )


def snafu_digit_to_balanced_base5_digit(snafu_digit):
    match snafu_digit:
        case "=":
            return -2
        case "-":
            return -1
        case _:
            return int(snafu_digit)


if __name__ == "__main__":
    print(solution(f"input/{__file__[-16:][:6]}.txt"))
