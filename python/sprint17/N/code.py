from typing import List


def merge(segments: List[List[int]]) -> List[List[int]]:
    if len(segments) < 2:
        return segments
    result: List[List[int]] = []
    segments = sorted(segments)
    for i in range(1, len(segments)):
        if segments[i - 1][1] >= segments[i][0]:
            segments[i][0] = min(segments[i - 1][0], segments[i][0])
            segments[i][1] = max(segments[i - 1][1], segments[i][1])
        else:
            result.append(segments[i - 1])
    result.append(segments[i])
    return result


def read_input() -> List[List[int]]:
    count = int(input())
    result = []
    for i in range(count):
        result.append([int(i) for i in input().strip().split()])
    return result


if __name__ == '__main__':
    for i in merge(read_input()):
        print(*i)
