# 81655980
from typing import List


class Participant:
    name: str
    tasks: int
    fine: int

    def __init__(self, name: str, tasks: str, fine: str) -> None:
        self.name = name
        self.tasks = int(tasks)
        self.fine = int(fine)

    def __lt__(self, other) -> bool:
        return (self.tasks > other.tasks if self.tasks != other.tasks else
                self.fine < other.fine if self.fine != other.fine else
                self.name < other.name)

    def __le__(self, other) -> bool:
        return self == other or self.__lt__(other)

    def __repr__(self) -> str:
        return f'({self.name}, задач {self.tasks}, штраф {self.fine})'


def get_pivot(arr: List[Participant], left: int, right: int) -> Participant:
    min, median, max = arr[left], arr[(left + right) // 2], arr[right]
    while not min <= median <= max:
        if median < min:
            min, median = median, min
        if max < median:
            median, max = max, median
    return median


def in_place_quick_sort(arr: List[Participant], begin: int, end: int) -> None:
    if end - begin < 1:
        return
    pivot = get_pivot(arr, begin, end)
    left, right = begin, end
    while left != right:
        if arr[left] < pivot:
            left += 1
        elif pivot < arr[right]:
            right -= 1
        else:
            arr[left], arr[right] = arr[right], arr[left]
    index_pivot = arr.index(pivot, begin, end + 1)
    in_place_quick_sort(arr, begin, index_pivot - 1)
    in_place_quick_sort(arr, index_pivot + 1, end)


def read_input() -> List[Participant]:
    participant_count = int(input())
    return [Participant(*input().strip().split())
            for _ in range(participant_count)]


if __name__ == '__main__':
    participants = read_input()
    in_place_quick_sort(participants, 0, len(participants) - 1)
    for participant in participants:
        print(participant.name)
