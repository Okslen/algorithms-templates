from typing import List

CORRECT_BRACKETS = {'{': '}', '[': ']', '(': ')'}
CLOSE_BRACKETS = ('}', ']', ')')


class StackBracketSeq():
    def __init__(self) -> None:
        self.items: List[str] = []

    def push(self, bracket: str) -> None:
        self.items.append(bracket)

    def pop(self):
        return self.items.pop() if self.items else None


def is_correct_bracket_seq(seq: str) -> bool:
    stack_open_brackets = StackBracketSeq()
    if len(seq) % 2 != 0:  # если количество скобок нечетное
        return False
    for bracket in seq:
        if bracket in CORRECT_BRACKETS:
            stack_open_brackets.push(bracket)
        elif bracket in CLOSE_BRACKETS:
            if CORRECT_BRACKETS.get(stack_open_brackets.pop()) != bracket:
                return False
        else:
            return False
    return True


if __name__ == '__main__':

    def read_input() -> str:
        return input().strip()

    print(is_correct_bracket_seq(read_input()))
