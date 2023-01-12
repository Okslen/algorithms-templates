# 80675748
from typing import List, Optional, Tuple, Union

ERROR_MESSAGE = 'error'


class MyDequeSized:
    def __init__(self, max_size: int) -> None:
        self.__deque: List[Union[int, None]] = [None] * max_size
        self.__max_size: int = max_size
        self.__head: int = 0
        self.__tail: int = 0
        self.__current_size: int = 0

    @property
    def is_empty(self) -> bool:
        return self.__current_size == 0

    @property
    def is_full(self) -> bool:
        return self.__current_size == self.__max_size

    def get_previous_index(self, index: int) -> int:
        return (index + self.__max_size - 1) % self.__max_size

    def get_next_index(self, index: int) -> int:
        return (index + 1) % self.__max_size

    def push_back(self, added: int) -> Union[None, str]:
        if self.is_full:
            return ERROR_MESSAGE
        self.__deque[self.__tail] = added
        self.__tail = self.get_next_index(self.__tail)
        self.__current_size += 1
        return None

    def push_front(self, added: int) -> Union[None, str]:
        if self.is_full:
            return ERROR_MESSAGE
        self.__head = self.get_previous_index(self.__head)
        self.__deque[self.__head] = added
        self.__current_size += 1
        return None

    def pop_front(self) -> Union[Optional[int], str]:
        if self.is_empty:
            return ERROR_MESSAGE
        deleted = self.__deque[self.__head]
        self.__deque[self.__head] = None
        self.__head = self.get_next_index(self.__head)
        self.__current_size -= 1
        return deleted

    def pop_back(self) -> Union[Optional[int], str]:
        if self.is_empty:
            return ERROR_MESSAGE
        self.__tail = self.get_previous_index(self.__tail)
        deleted = self.__deque[self.__tail]
        self.__deque[self.__tail] = None
        self.__current_size -= 1
        return deleted


def read_input() -> Tuple[int, Tuple[List[str], ...]]:
    commands_count = int(input())
    max_size = int(input())
    input_commands = tuple(
        input().strip().split() for _ in range(commands_count))
    return max_size, input_commands


def main(max_size: int, input_commands: Tuple[List[str], ...]) -> None:
    instance = MyDequeSized(max_size)
    for command in input_commands:
        if getattr(instance, command[0], None) is None:
            print(ERROR_MESSAGE)
            break
        if len(command) == 1:
            print(getattr(instance, command[0])())
        else:
            pushing = getattr(instance, command[0])(int(command[1]))
            if pushing:
                print(pushing)


if __name__ == '__main__':
    main(*read_input())
