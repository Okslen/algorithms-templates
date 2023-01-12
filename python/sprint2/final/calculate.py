# 80670009
from typing import List

BINARY_OPERATORS = {
    '+': lambda x, y: y + x,
    '-': lambda x, y: y - x,
    '*': lambda x, y: y * x,
    '/': lambda x, y: y // x,
}


class Stack:
    def __init__(self) -> None:
        self.__items: List[int] = []

    def push(self, item: int):
        self.__items.append(item)

    def pop(self):
        return self.__items.pop() if self.__items else None


def calculate(impression: List[str]) -> int:
    arguments = Stack()
    for element in impression:
        if element in BINARY_OPERATORS:
            arguments.push(
                BINARY_OPERATORS[element](
                    arguments.pop(),
                    arguments.pop()
                )
            )
        else:
            arguments.push(int(element))
    return arguments.pop()


def read_input() -> List[str]:
    return input().strip().split()


if __name__ == '__main__':
    print(calculate(read_input()))
