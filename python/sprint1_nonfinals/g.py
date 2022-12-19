BASE = 2


def to_binary(number: int, base: int) -> str:
    if number < base:
        return str(number)
    result = []
    quotient = number // base
    result.append(str(number % base))
    while quotient >= base:
        divisible = quotient
        quotient = divisible // base
        result.append(str(divisible % base))
    result.append(str(quotient))
    return ''.join(result[::-1])


def read_input() -> int:
    return int(input().strip())


print(to_binary(read_input(), BASE))
