from typing import List, Tuple


def read_input() -> List[Tuple[int, int, str]]:
    participant_count = int(input())
    result = []
    for _ in range(participant_count):
        data = input().strip().split()
        result.append((int(data[1]), -int(data[2]), data[0]))
    return result


if __name__ == '__main__':
    arr = read_input()
    print(arr)
