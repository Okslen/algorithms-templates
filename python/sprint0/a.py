from typing import Tuple


def get_sum(arr: Tuple) -> int:
    return sum(arr)


def read_input() -> Tuple[int, int]:
    return int(input()), int(input())


print(get_sum(read_input()))
