# 80303943
from typing import List, Optional, Tuple, Union

ERROR_MESSAGE = 'error'


class MyDequeSized:
    def __init__(self, max_size: int) -> None:
        self.__deque__: List[Union[int, None]] = [None] * max_size
        self.max_size: int = max_size
        self.head: int = 0
        self.tail: int = 0
        self.current_size: int = 0

    @property
    def is_empty(self) -> bool:
        return self.current_size == 0

    @property
    def is_full(self) -> bool:
        return self.current_size == self.max_size

    def get_previous_index(self, index):
        return (index + self.max_size - 1) % self.max_size

    def get_next_index(self, index):
        return (index + 1) % self.max_size

    def push_back(self, added: int) -> Union[None, str]:
        if self.is_full:
            return ERROR_MESSAGE
        self.__deque__[self.tail] = added
        self.tail = self.get_next_index(self.tail)
        self.current_size += 1
        return None

    def push_front(self, added: str) -> Union[None, str]:
        if self.is_full:
            return ERROR_MESSAGE
        self.head = self.get_previous_index(self.head)
        self.__deque__[self.head] = added
        self.current_size += 1
        return None

    def pop_front(self) -> Union[Optional[int], str]:
        if self.is_empty:
            return ERROR_MESSAGE
        deleted = self.__deque__[self.head]
        self.__deque__[self.head] = None
        self.head = self.get_next_index(self.head)
        self.current_size -= 1
        return deleted

    def pop_back(self) -> Union[Optional[int], str]:
        if self.is_empty:
            return ERROR_MESSAGE
        self.tail = self.get_previous_index(self.tail)
        deleted = self.__deque__[self.tail]
        self.__deque__[self.tail] = None
        self.current_size -= 1
        return deleted


def read_input() -> Tuple[int, Tuple[List[str], ...]]:
    commands_count = int(input())
    max_size = int(input())
    input_commands = tuple(
        input().strip().split() for _ in range(commands_count))
    return max_size, input_commands


if __name__ == '__main__':
    max_size, input_commands = read_input()
    instance = MyDequeSized(max_size)
    AVAILABLE_COMMANDS = set(('push_back', 'push_front',
                              'pop_back', 'pop_front'))

    def main(commands):
        for command in commands:
            if command[0] not in AVAILABLE_COMMANDS:
                return ERROR_MESSAGE
            if len(command) == 1:
                print(getattr(instance, command[0])())
            else:
                pushing = getattr(instance, command[0])(int(command[1]))
                if pushing:
                    print(pushing)

    main(input_commands)
