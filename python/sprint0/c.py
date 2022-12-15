from typing import List, Tuple


def moving_average(
    length: int, arr: List[int], window_size: int
) -> List[float]:
    current_sum = sum(arr[:window_size])
    result = [current_sum/window_size]
    for i in range(length-window_size):
        current_sum += arr[i+window_size] - arr[i]
        result.append(current_sum/window_size)
    return result


def read_input() -> Tuple[int, List[int], int]:
    length = int(input())
    arr = list(map(int, input().strip().split()))
    window_size = int(input())
    return length, arr, window_size


length, arr, window_size = 10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3
print(" ".join(map(str, moving_average(length, arr, window_size))))
