from typing import List

LETTERS = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
           '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}


def letter_combinations(
    numbers: str, index: int = 0, prefix: str = '', result: List[str] = []
) -> List[str]:
    if index == len(numbers):
        result.append(prefix)
        return result
    letters = LETTERS[numbers[index]]
    for letter in letters:
        letter_combinations(numbers, index + 1, prefix + letter, result)
    return result


if __name__ == '__main__':
    print(*letter_combinations(input()))
