from typing import List
from itertools import zip_longest

def is_first_bigger(first: str, second: str) -> bool:
    for pair in zip_longest(first, second, fillvalue='9'):
        if pair[0] != pair[1]:
            return pair[0] > pair[1]
    return len(first) > len(second)


def insertion_sort(numbers: List[str]):
    for i in range(1, len(numbers)):
        inserted = numbers[i]
        j = i
        while j > 0 and is_first_bigger(inserted, numbers[j-1]):
            numbers[j] = numbers[j - 1]
            j -= 1
        numbers[j] = inserted
    return numbers


def read_input() -> List[str]:
    _ = input()
    return input().strip().split()


if __name__ == '__main__':
    print(*insertion_sort(read_input()), sep='')
