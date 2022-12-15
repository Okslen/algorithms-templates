from typing import List, Tuple, Optional


def two_sum(
    length: int, arr: List[int], target_sum: int
) -> Optional[Tuple[int, int]]:
    aux = set()
    for element in arr:
        if target_sum - element in aux:
            return element, target_sum - element
        aux.add(element)
    return None


def read_input() -> Tuple[List[int], int]:
    length = int(input())
    arr = list(map(int, input().strip().split()))
    target_sum = int(input())
    return length, arr, target_sum


def print_result(result: Optional[Tuple[int, int]]) -> None:
    if result is None:
        print(None)
    else:
        print(" ".join(map(str, result)))


length, arr, target_sum = read_input()
print_result(two_sum(length, arr, target_sum))
