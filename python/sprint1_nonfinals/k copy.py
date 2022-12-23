from typing import Tuple


def get_sum(number: int, k: int) -> str:
    amount = number + k
    return " ".join(str(amount))


def read_input() -> Tuple[int, int]:
    _ = int(input())
    number = int(''.join(input().strip().split()))
    k = int(input())
    return number, k


number_list, k = read_input()
print(get_sum(number_list, k))
