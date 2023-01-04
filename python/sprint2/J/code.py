from typing import List, Union

EMPTY_MESSAGE = 'error'


class Node:
    def __init__(self, value: int, next=None) -> None:
        self.value: int = value
        self.next: Union[Node, None] = next

    def get_node_by_index(node, index):
        while index:
            node = node.next
            index -= 1
        return node


class NodeQueue:
    def __init__(self) -> None:
        self.current_size: int = 0
        self.head: Union[Node, None] = None
        self.tail: Union[Node, None] = None

    def put(self, value: int):
        new_tail = Node(value)
        if not self.head:
            self.head = new_tail
        elif not self.tail:
            self.head.next = new_tail
        else:
            self.tail.next = new_tail
        self.tail = new_tail
        self.current_size += 1

    def get(self) -> Union[int, str]:
        if not self.head:
            return EMPTY_MESSAGE
        old_head = self.head
        self.head = old_head.next if old_head.next else None
        self.tail = None if self.tail == self.head else self.tail
        self.current_size -= 1
        return old_head.value

    def size(self) -> int:
        return self.current_size


if __name__ == '__main__':

    def read_input() -> List[List[str]]:
        commands_count = int(input())
        input_commands = []
        for _ in range(commands_count):
            input_commands.append(input().strip().split())
        return input_commands

    isinstance = NodeQueue()

    AVAILIBLE_COMMANDS = {
        'put': isinstance.put, 'get': isinstance.get, 'size': isinstance.size
    }

    def main(input_commands):
        for command in input_commands:
            if len(command) == 1:
                print(AVAILIBLE_COMMANDS[command[0]]())
            else:
                result = AVAILIBLE_COMMANDS[command[0]](int(command[1]))
                print(result) if result else None

    main(read_input())
