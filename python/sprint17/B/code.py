from typing import List

LETTERS = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
           '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}


def letter_combinations(
    n: int, prefix: str, numbers: str, result: List[str]
) -> List[str]:
    if n == 0:
        result.append(prefix)
        return result
    else:
        for number in numbers:
            for letter in LETTERS[number]:
                prefix = letter
            letter_combinations(n - 1, prefix + letter, numbers, result)
    return result


if __name__ == '__main__':
    prefix = input()
    print(letter_combinations(len(prefix), '', prefix, []), sep='\n')
