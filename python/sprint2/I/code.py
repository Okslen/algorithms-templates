from typing import List, Tuple, Union

OVERSIZE_MESSAGE = 'error'


class MyQueueSized:
    def __init__(self, max_size: int) -> None:
        self.queue: List[Union[str, None]] = [None] * max_size
        self.head: int = 0
        self.tail: int = 0
        self.current_size: int = 0
        self.max_size: int = max_size

    def is_empty(self) -> bool:
        return self.current_size == 0

    def push(self, added: str) -> Union[None, str]:
        if self.current_size == self.max_size:
            return OVERSIZE_MESSAGE
        self.queue[self.tail] = added
        self.tail = (self.tail + 1) % self.max_size
        self.current_size += 1
        return None

    def pop(self) -> Union[str, None]:
        if self.is_empty():
            return None
        deleted = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.current_size -= 1
        return deleted

    def peek(self) -> Union[str, None]:
        if self.is_empty():
            return None
        return self.queue[self.head]

    def size(self) -> int:
        return self.current_size


if __name__ == '__main__':

    def read_input() -> Tuple[int, List[List[str]]]:
        commands_count = int(input())
        max_size = int(input())
        input_commands = []
        for _ in range(commands_count):
            input_commands.append(input().strip().split())
        return max_size, input_commands

    max_size, input_commands = read_input()

    instance = MyQueueSized(max_size)

    AVAILABLE_COMMANDS = {'push': instance.push, 'pop': instance.pop,
                          'peek': instance.peek, 'size': instance.size}

    def main(commands):
        for command in commands:
            if len(command) == 1:
                print(AVAILABLE_COMMANDS[command[0]]())
            else:
                pushing = (AVAILABLE_COMMANDS[command[0]](command[1]))
                if pushing:
                    print(pushing)

    main(input_commands)
