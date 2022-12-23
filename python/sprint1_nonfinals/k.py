from itertools import zip_longest
from typing import List, Tuple


def get_sum(number_list: List[int], k: int) -> List[int]:
    result = []
    reminder = 0
    for i, j in zip_longest(number_list[::-1],
                            [int(i) for i in str(k)[::-1]],
                            fillvalue=0):
        amount = i + j + reminder
        result.append(amount % 10)
        reminder = amount // 10
    if reminder:
        result.append(reminder)
    return result[::-1]


def read_input() -> Tuple[List[int], int]:
    _ = int(input())
    number_list = list(map(int, input().strip().split()))
    k = int(input())
    return number_list, k


number_list, k = read_input()
print(" ".join(map(str, get_sum(number_list, k))))
