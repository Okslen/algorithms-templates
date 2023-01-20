from typing import List

OPEN_BRACKET = '('
CLOSE_BRACKET = ')'


def is_correct_brackets_seq(seq: str) -> bool:
    open_brackets = []
    for bracket in seq:
        if bracket == OPEN_BRACKET:
            open_brackets.append(bracket)
        elif len(open_brackets) == 0 or open_brackets.pop() != OPEN_BRACKET:
            return False
    return len(open_brackets) == 0


def brackets_generator(n: int, prefix: str, result: List[str]) -> List[str]:
    if n == 0:
        if is_correct_brackets_seq(prefix):
            result.append(prefix)
        return result
    else:
        brackets_generator(n - 1, prefix + OPEN_BRACKET, result)
        brackets_generator(n - 1, prefix + CLOSE_BRACKET, result)
    return result


def read_input() -> int:
    return int(input())


if __name__ == '__main__':
    print(*brackets_generator(read_input()*2, '', []), sep='\n')
