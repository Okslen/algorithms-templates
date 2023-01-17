from typing import Tuple

NOT_RESULT = -1


def binary_search_day(arr: Tuple[int, ...], price: int, left, right) -> int:
    if right <= left:
        return NOT_RESULT
    middle = (right + left) // 2
    if (price <= arr[middle] and
       price > arr[middle - 1] if middle != 0 else True):
        return middle + 1
    if arr[middle] < price:
        return binary_search_day(arr, price, middle + 1, right)
    return binary_search_day(arr, price, left, middle)


def two_bicycle(arr: Tuple[int, ...], price: int) -> Tuple[int, int]:
    first_day = binary_search_day(arr, price, 0, len(arr))
    return first_day, binary_search_day(
        arr, price * 2, first_day, len(arr)
    ) if first_day != NOT_RESULT else NOT_RESULT


def read_input() -> Tuple[Tuple[int, ...], int]:
    _ = input()
    arr = tuple(map(int, input().strip().split()))
    price = int(input())
    return arr, price


if __name__ == '__main__':
    print(*two_bicycle(*read_input()))
