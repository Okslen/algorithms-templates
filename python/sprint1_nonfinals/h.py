from itertools import zip_longest
from typing import Tuple

BASE = 2


def get_sum(first_number: str, second_number: str, base: int) -> str:
    # if first_number == 0 and second_number == 0:
    #     return '0'
    result = []
    reminder = 0
    for couple in zip_longest(
        map(int, first_number[::-1]),
        map(int, second_number[::-1]),
        fillvalue=0
    ):
        amount = sum(couple) + reminder
        result.append(str(amount % base))
        reminder = amount // base
    if reminder:
        result.append(str(reminder))
    return ''.join(result[::-1])


def read_input() -> Tuple[str, str]:
    first_number = '0'.strip()
    second_number = '0'.strip()
    return first_number, second_number


first_number, second_number = read_input()
print(get_sum(first_number, second_number, BASE))
