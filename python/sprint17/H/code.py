from typing import Callable, List


def is_first_bigger(first: str, second: str) -> bool:
    if len(first) == len(second):
        return first > second
    return first + second > second + first


def insertion_sort(numbers: List[str], comparator: Callable):
    for i in range(1, len(numbers)):
        inserted = numbers[i]
        j = i
        while j > 0 and comparator(inserted, numbers[j-1]):
            numbers[j] = numbers[j - 1]
            j -= 1
        numbers[j] = inserted
    return numbers


def read_input() -> List[str]:
    _ = input()
    return input().strip().split()


if __name__ == '__main__':
    print(*insertion_sort(read_input(), is_first_bigger), sep='')
