import math
import timeit

number = 1024
iteration = 1000000


def is_power_of_four_set(number: int) -> bool:
    return number in set((4**i for i in range(7)))


def is_power_of_four_log(number: int) -> bool:
    return not bool(math.log2(number) / 2 % 1)


def is_power_of_four_division(number: int) -> bool:
    if not number:
        return False
    if number == 1:
        return True
    while not number % 4 and number != 4:
        number = number / 4
    return not bool(number % 4)


def main(iteration=iteration):
    print('is_power_of_four_set:', timeit.Timer(
        'f(number)',
        'from __main__ import number, is_power_of_four_set as f'
    ).timeit(iteration))
    print('is_power_of_four_log:', timeit.Timer(
        'f(number)',
        'from __main__ import number, is_power_of_four_log as f'
    ).timeit(iteration))
    print('is_power_of_four_division:', timeit.Timer(
        'f(number)',
        'from __main__ import number, is_power_of_four_division as f'
    ).timeit(iteration))


if __name__ == '__main__':
    main()
