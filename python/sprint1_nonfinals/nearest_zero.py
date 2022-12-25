from typing import List, Tuple


def get_nearest_zero(length: int, numbers: Tuple[int]) -> List[int]:
    nearest_zero = [0] * length
    return nearest_zero


def read_input() -> Tuple[int, Tuple[int]]:
    length = int(input())
    numbers = tuple(map(int, input().strip().split()))
    return length, numbers


length, numbers = read_input()
print(' '.join(map(str, get_nearest_zero(length, numbers))))
