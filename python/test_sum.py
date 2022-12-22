import timeit
from itertools import zip_longest

BASE = 2
first = '100110010'
second = '100101'
iteration = 100000


def get_sum_sum(first_number: str, second_number: str, base: int) -> str:
    result = []
    reminder = 0
    for couple in zip_longest(
        map(int, first_number[::-1]),
        map(int, second_number[::-1]),
        fillvalue=0
    ):
        amount = sum(couple) + reminder
        result.append(str(amount % base))
        reminder = amount // base
    if reminder:
        result.append(str(reminder))
    return ''.join(result[::-1])


def get_sum_plus_map(first_number: str, second_number: str, base: int) -> str:
    result = []
    reminder = 0
    for i, j in zip_longest(
        map(int, first_number[::-1]),
        map(int, second_number[::-1]),
        fillvalue=0
    ):
        amount = i + j + reminder
        result.append(str(amount % base))
        reminder = amount // base
    if reminder:
        result.append(str(reminder))
    return ''.join(result[::-1])


def get_sum_plus(first_number: str, second_number: str, base: int) -> str:
    result = []
    reminder = 0
    for i, j in zip_longest(first_number[::-1],
                            second_number[::-1],
                            fillvalue=0):
        amount = int(i) + int(j) + reminder
        result.append(str(amount % base))
        reminder = amount // base
    if reminder:
        result.append(str(reminder))
    return ''.join(result[::-1])


def get_sum_plus_str(first_number: str, second_number: str, base: int) -> str:
    result = ''
    reminder = 0
    for i, j in zip_longest(first_number[::-1],
                            second_number[::-1],
                            fillvalue=0):
        amount = int(i) + int(j) + reminder
        result = str(amount % base) + result
        reminder = amount // base
    if reminder:
        return str(reminder) + result
    return result


def main(iteration=iteration):
    print('get_sum_sum:', timeit.Timer(
        'f(first, second, BASE)',
        'from __main__ import first, second, BASE, get_sum_sum as f'
    ).timeit(iteration))
    print('get_sum_plus_map:', timeit.Timer(
        'f(first, second, BASE)',
        'from __main__ import first, second, BASE, get_sum_plus_map as f'
    ).timeit(iteration))
    print('get_sum_plus:', timeit.Timer(
        'f(first, second, BASE)',
        'from __main__ import first, second, BASE, get_sum_plus as f'
    ).timeit(iteration))
    print('get_sum_plus_str:', timeit.Timer(
        'f(first, second, BASE)',
        'from __main__ import first, second, BASE, get_sum_plus_str as f'
    ).timeit(iteration))


if __name__ == '__main__':
    main()
