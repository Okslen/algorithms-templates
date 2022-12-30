# 80188586

from typing import Tuple

FIELD_SIZE = 4
PLAYERS_NUMBER = 2
EMPTY_CELL = '.'


def get_max_points(keys_count: int, numbers: Tuple[int, ...]) -> int:
    keys_count *= PLAYERS_NUMBER
    max_points = 0
    for i in set(numbers):
        if numbers.count(i) <= keys_count:
            max_points += 1
    return max_points


def read_input() -> Tuple[int, Tuple[int, ...]]:
    keys_count = int(input())
    numbers = []
    for i in range(FIELD_SIZE):
        numbers.append([int(i) for i in input() if i != EMPTY_CELL])
    return keys_count, tuple(i for row in numbers for i in row)


keys_count, numbers = read_input()
print(str(get_max_points(keys_count, numbers)))
