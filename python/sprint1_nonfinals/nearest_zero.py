# 80187326

from typing import List, Tuple


def get_zero_indexes(length: int, numbers: Tuple[int, ...]) -> Tuple[int, ...]:
    return tuple((index for index in range(length) if not numbers[index]))


def get_steps_count_before(
    steps_count: List[int], zero_indexes: Tuple[int, ...]
) -> List[int]:
    steps = 1
    for i in range(zero_indexes[0])[::-1]:
        steps_count[i] = steps
        steps += 1
    return steps_count


def get_steps_count_after(
    length: int, steps_count: List[int], zero_indexes: Tuple[int, ...]
) -> List[int]:
    steps = 1
    for i in range(zero_indexes[-1] + 1, length):
        steps_count[i] = steps
        steps += 1
    return steps_count


def get_steps_count_between(
    steps_count: List[int], zero_indexes: Tuple[int, ...]
) -> List[int]:
    for i in range(len(zero_indexes) - 1):
        first_index = zero_indexes[i] + 1
        second_index = zero_indexes[i + 1] - 1
        steps = 1
        while second_index >= first_index:
            steps_count[first_index], steps_count[second_index] = steps, steps
            steps += 1
            first_index += 1
            second_index -= 1
    return steps_count


def get_nearest_zero(length: int, numbers: Tuple[int, ...]) -> List[int]:
    zero_indexes = get_zero_indexes(length, numbers)
    return get_steps_count_after(
        length,
        get_steps_count_between(
            get_steps_count_before(
                [0] * length,
                zero_indexes),
            zero_indexes),
        zero_indexes)


def read_input() -> Tuple[int, Tuple[int, ...]]:
    length = int(input())
    numbers = tuple(map(int, input().strip().split()))
    return length, numbers


length, numbers = read_input()
print(' '.join(map(str, get_nearest_zero(length, numbers))))
