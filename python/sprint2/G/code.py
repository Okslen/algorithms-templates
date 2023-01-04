from typing import List


class StackMax:
    def __init__(self):
        self.items = []

    def push(self, item: int):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if self.items else 'error'

    def peek(self):
        return self.items[-1] if self.items else None


class StackMaxEffective:
    def __init__(self):
        self.items = []
        self.max = StackMax()

    def get_max(self):
        print(self.max.peek())

    def push(self, item: int):
        self.items.append(item)
        if not self.max.items or item >= self.max.peek():
            self.max.push(item)

    def peek(self):
        return self.items[-1] if self.items else 'error'

    def pop(self):
        if self.peek() == self.max.peek():
            self.max.pop()
        self.items.pop() if self.items else print('error')


if __name__ == '__main__':

    def read_input() -> List[List[str]]:
        commands_count = int(input())
        commands = []
        for _ in range(commands_count):
            commands.append(input().strip().split())
        return commands

    instance = StackMaxEffective()

    COMMANDS = {
        'push': instance.push,
        'pop': instance.pop,
        'get_max': instance.get_max
    }
    for command in read_input():
        if len(command) == 1:
            COMMANDS[command[0]]()
        else:
            COMMANDS[command[0]](int(command[1]))
