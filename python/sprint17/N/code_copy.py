from typing import List, Optional, Union


def merge(arr1: List[int], arr2: List[int]) -> List[Optional[int]]:
    result: List[Union[None, int]] = [None] * (len(arr1) + len(arr2))
    a1, a2, k = 0, 0, 0
    while a1 < len(arr1) and a2 < len(arr2):
        if arr1[a1] <= arr2[a2]:
            result[k] = arr1[a1]
            a1 += 1
        else:
            result[k] = arr2[a2]
            a2 += 1
        k += 1
    while a1 < len(arr1):
        result[k] = arr1[a1]
        a1 += 1
        k += 1
    while a2 < len(arr2):
        result[k] = arr2[a2]
        a2 += 1
        k += 1
    return [result[0], result[-1]]


def main(segments: List[List[int]], result: List[int] = []) -> List[List[int]]:
    for i in range(1, len(segments)):
        arr1 = segments[i - 1]
        arr2 = segments[i]
        if set.intersection(set(range(arr1[0], arr1[1] + 1)),
                            set(range(arr2[0], arr2[1] + 1))):
            segments[i] = (merge(arr1, arr2))
        else:
            result.append(arr1)
    result.append(segments[i])
    return result


def read_input() -> List[List[int]]:
    count = int(input())
    result = []
    for i in range(count):
        result.append([int(i) for i in input().strip().split()])
    return result


if __name__ == '__main__':
    for i in main(sorted(read_input())):
        print(*i)
