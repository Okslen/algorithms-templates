def fibonacci(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':

    def read_input():
        return int(input())

    print(fibonacci(read_input()))
