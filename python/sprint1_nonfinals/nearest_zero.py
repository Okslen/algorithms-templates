from typing import List, Tuple


def get_zero_indexes(length: int, numbers: Tuple[int]) -> List[int]:
    return [index for index in range(length) if not numbers[index]]


def get_nearest_zero(length: int, numbers: Tuple[int]) -> List[int]:
    return get_zero_indexes(length, numbers)


def read_input() -> Tuple[int, Tuple[int]]:
    length = int(input())
    numbers = tuple(map(int, input().strip().split()))
    return length, numbers


length, numbers = read_input()
print(' '.join(map(str, get_nearest_zero(length, numbers))))
