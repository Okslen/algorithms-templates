import timeit

range_to = 1000000
iteration = 100


def change_var_by_const(iteration):
    var_one = True
    var_two = False
    for i in range(range_to):
        if var_one:
            var_one = False
            var_two = True
        else:
            var_one = True
            var_two = False


def change_var_by_var(iteration):
    var_one = True
    var_two = False
    for i in range(range_to):
        if var_one:
            var_one = not var_one
            var_two = not var_two
        else:
            var_one = not var_one
            var_two = not var_two


def main(iteration=iteration):
    print('change_var_by_const:', timeit.Timer(
        'f(iteration)',
        'from __main__ import iteration,change_var_by_const as f'
    ).timeit(iteration))
    print('change_var_by_var:', timeit.Timer(
        'f(iteration)',
        'from __main__ import iteration,change_var_by_var as f'
    ).timeit(iteration))


if __name__ == '__main__':
    main()
