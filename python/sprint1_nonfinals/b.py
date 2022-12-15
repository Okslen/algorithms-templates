def check_parity(a: int, b: int, c: int) -> bool:
    a_is_even = a % 2 == 0
    b_is_even = b % 2 == 0
    if b_is_even is not a_is_even:
        return False
    c_is_even = c % 2 == 0
    if c_is_even is not a_is_even:
        return False
    return True


def print_result(result: bool) -> None:
    if result:
        print("WIN")
    else:
        print("FAIL")


a, b, c = map(int, input().strip().split())
print_result(check_parity(a, b, c))
