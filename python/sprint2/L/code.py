def fibonacci(intern_count, digital_count):
    if intern_count == 0 or intern_count == 1:
        return 1
    module = 10 ** digital_count
    i = 2
    result_previous = 1
    result_pre_previous = 1
    while i != intern_count + 1:
        result = (result_previous + result_pre_previous) % module
        i += 1
        result_pre_previous = result_previous
        result_previous = result
    return result


if __name__ == '__main__':

    def read_input():
        return map(int, input().strip().split())

    intern_count, digital_count = read_input()
    print(fibonacci(intern_count, digital_count))
