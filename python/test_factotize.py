import timeit
from typing import List

number = 1298074214633706835075030044377087
iteration = 1


def factorize_square(number: int) -> List[int]:
    square = int(number**(1/2))
    result = []
    lp = [0] * (square + 1)
    primes = []
    for i in range(2, square + 1):
        if lp[i] == 0:
            lp[i] = i
            primes.append(i)
            while number % i == 0:
                result.append(i)
                number = number / i
        if number < i:
            break
        for p in primes:
            x = p * i
            if (p > lp[i]) or (x > square):
                break
            lp[x] = p
    if number != 1:
        result.append(int(number))
    return result


def factorize_divizion(number: int) -> List[int]:
    result = []
    i = 2
    while i * i < number:
        while number % i == 0:
            result.append(i)
            number = number / i
        i += 1
    if number != 1:
        result.append(int(number))
    return result


def main(iteration=iteration):
    print('factorize_square:', timeit.Timer(
        'f(number)',
        'from __main__ import number, factorize_square as f'
    ).timeit(iteration))
    print('factorize_divizion:', timeit.Timer(
        'f(number)',
        'from __main__ import number, factorize_divizion as f'
    ).timeit(iteration))


if __name__ == '__main__':
    main()
