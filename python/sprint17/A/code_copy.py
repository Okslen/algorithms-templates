from typing import List

OPEN_BRACKET = '('
CLOSE_BRACKET = ')'


def brackets_generator(n: int, prefix: str = '', open_count: int = 0,
                       close_count: int = 0, result: List[str] = []
                       ) -> List[str]:
    if n == close_count:
        result.append(prefix)
        return result
    if open_count < n:
        brackets_generator(
            n, prefix + OPEN_BRACKET, open_count + 1, close_count, result)
    if open_count > close_count:
        brackets_generator(
            n, prefix + CLOSE_BRACKET, open_count, close_count + 1, result)
    return result


def read_input() -> int:
    return int(input())


if __name__ == '__main__':
    print(*brackets_generator(read_input()), sep='\n')
