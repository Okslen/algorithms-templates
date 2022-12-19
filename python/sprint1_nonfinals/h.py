from itertools import zip_longest
from typing import Tuple

BASE = 2


def get_sum(first_number: str, second_number: str, base: int) -> str:
    result = ''
    reminder = 0
    for i, j in zip_longest(first_number[::-1],
                            second_number[::-1],
                            fillvalue=0):
        amount = int(i) + int(j) + reminder
        result = str(amount % base) + result
        reminder = amount // base
    result = str(reminder) + result
    return result.lstrip('0')


def read_input() -> Tuple[str, str]:
    first_number = input().strip()
    second_number = input().strip()
    return first_number, second_number


first_number, second_number = read_input()
print(get_sum(first_number, second_number, BASE))
