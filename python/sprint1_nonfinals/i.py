import math


def is_power_of_four(number: int) -> bool:
    return not bool(math.log2(number) / 2 % 1)


print(is_power_of_four(int(input())))
