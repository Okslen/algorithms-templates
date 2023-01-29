# 81533264
from typing import List

NOT_FOUND = -1


def binary_broken_search(value: int, arr: List[int],
                         left: int, right: int) -> int:
    mid = (right + left) // 2
    if arr[mid] == value:
        return mid
    if right - left == 1:
        return NOT_FOUND

    if arr[left] < arr[mid]:  # left_is_sorted
        if arr[left] <= value < arr[mid]:  # value_in_left_sorted
            return binary_broken_search(value, arr, left, mid)
        return binary_broken_search(value, arr, mid + 1, right)

    if arr[mid] < arr[right - 1]:  # right_is_sorted
        if arr[mid] < value <= arr[right - 1]:  # value_in_right_sorted
            return binary_broken_search(value, arr, mid + 1, right)
        return binary_broken_search(value, arr, left, mid)

    return NOT_FOUND


def broken_search(arr: List[int], finding_value: int) -> int:
    return binary_broken_search(finding_value, arr, 0, len(arr))


def test():
    arr = [7, 8, 9, 10, 0, 1, 2, 3, 4, 5, 6,]
    assert broken_search(arr, 6) == 10


if __name__ == '__main__':
    test()
