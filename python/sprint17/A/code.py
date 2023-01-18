from typing import List


def brackets_generator(n: int, result: List[str]) -> List[str]:
    if n == 0:
        print(result)
        return result
    result.append('(')
    brackets_generator(n - 1, result)
    result.append(')')
    brackets_generator(n - 1, result)


def read_input() -> int:
    return int(input())


if __name__ == '__main__':
    print(brackets_generator(read_input(), []))
