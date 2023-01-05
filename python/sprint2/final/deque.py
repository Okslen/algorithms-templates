# 80291451
from typing import List, Optional, Tuple, Union

ERROR_MESSAGE = 'error'


class MyDequeSized:
    def __init__(self, max_size: int) -> None:
        self.deque: List[Union[int, None]] = [None] * max_size
        self.max_size: int = max_size
        self.head: int = 0
        self.tail: int = 0
        self.current_size: int = 0

    def is_empty(self) -> bool:
        return self.current_size == 0

    def is_full(self) -> bool:
        return self.current_size == self.max_size

    def push_back(self, added: int) -> Union[None, str]:
        if self.is_full():
            return ERROR_MESSAGE
        self.deque[self.tail] = added
        self.tail = (self.tail + 1) % self.max_size
        self.current_size += 1
        return None

    def push_front(self, added: str) -> Union[None, str]:
        if self.is_full():
            return ERROR_MESSAGE
        self.head = (self.head + self.max_size - 1) % self.max_size
        self.deque[self.head] = added
        self.current_size += 1
        return None

    def pop_front(self) -> Union[Optional[int], str]:
        if self.is_empty():
            return ERROR_MESSAGE
        deleted = self.deque[self.head]
        self.deque[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.current_size -= 1
        return deleted

    def pop_back(self) -> Union[Optional[int], str]:
        if self.is_empty():
            return ERROR_MESSAGE
        self.tail = (self.tail + self.max_size - 1) % self.max_size
        deleted = self.deque[self.tail]
        self.deque[self.tail] = None
        self.current_size -= 1
        return deleted


if __name__ == '__main__':

    def read_input() -> Tuple[int, Tuple[List[str], ...]]:
        commands_count = int(input())
        max_size = int(input())
        input_commands = tuple(
            input().strip().split() for _ in range(commands_count))
        return max_size, input_commands

    max_size, input_commands = read_input()

    instance = MyDequeSized(max_size)

    AVAILABLE_COMMANDS = {
        'push_back': instance.push_back, 'push_front': instance.push_front,
        'pop_back': instance.pop_back, 'pop_front': instance.pop_front,
    }

    def main(commands):
        for command in commands:
            if command[0] not in AVAILABLE_COMMANDS:
                return ERROR_MESSAGE
            if len(command) == 1:
                print(AVAILABLE_COMMANDS[command[0]]())
            else:
                pushing = (AVAILABLE_COMMANDS[command[0]](int(command[1])))
                if pushing:
                    print(pushing)

    main(input_commands)
