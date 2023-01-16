from typing import List, Tuple

def two_bicycle(arr: Tuple[int, ...], price: int, left, right):
    pass


def read_input() -> Tuple[Tuple[int, ...], int]:
    days_count = input()
    arr = tuple(map(int, input().strip().split()))
    price = int(input())
    return arr, price
