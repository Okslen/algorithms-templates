from typing import List, Tuple, Optional


def two_sum(
    length: int, arr: List[int], target_sum: int
) -> Optional[Tuple[int, int]]:
    arr.sort()
    arr = tuple(arr)
    left = 0
    right = length-1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target_sum:
            return (arr[left], arr[right])
        if current_sum < target_sum:
            left += 1
        else:
            right -= 1
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


# arr, target_sum = read_input()
length, arr, target_sum = 10, [18, 3, 2, 8, 5, 6, 7, 4, 9, 10], 7
print_result(two_sum(length, arr, target_sum))
