from typing import List


def factorize(number: int) -> List[int]:
    result = []
    for i in set((2, 3, 5, 7, 11, 13, 17)):
        while number % i == 0:
            result.append(i)
            number = int(number / i)
    lp = [0] * (number + 1)
    primes = []
    for i in range(2, number + 1):
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
            if (p > lp[i]) or (x > number):
                break
            lp[x] = p
    return result


result = factorize(int(input()))
print(" ".join(map(str, result)))
