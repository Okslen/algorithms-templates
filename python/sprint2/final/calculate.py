# 80297898
from typing import List, Union

BINARY_OPERATORS = set(('+', '-', '*', '/'))


class Stack:
    def __init__(self) -> None:
        self.items: List[Union[int, None]] = []

    def push(self, item: int):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if self.items else None


def get_result(first_arg: int, second_arg: int, operator: str) -> int:
    if operator == '+':
        return first_arg + second_arg
    if operator == '-':
        return first_arg - second_arg
    if operator == '*':
        return first_arg * second_arg
    return first_arg // second_arg


def calculate(impression: List[str]) -> int:
    arguments = Stack()
    for element in impression:
        if element in BINARY_OPERATORS:
            arguments.push(
                get_result(
                    second_arg=arguments.pop(),
                    first_arg=arguments.pop(),
                    operator=element
                )
            )
        else:
            arguments.push(int(element))
    return arguments.pop()


if __name__ == '__main__':

    def read_input() -> List[str]:
        return input().strip().split()

    print(calculate(read_input()))
