from typing import List


class StackMax:
    def __init__(self):
        self.items = []

    def push(self, item: int):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if self.items else print('error')

    def get_max(self):
        print(max(self.items, default=None))


if __name__ == '__main__':

    def read_input() -> List[List[str]]:
        commands_count = int(input())
        commands = []
        for _ in range(commands_count):
            commands.append(input().strip().split())
        return commands

    instance = StackMax()

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
