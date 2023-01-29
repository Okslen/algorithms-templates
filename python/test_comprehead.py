import timeit

range_to = 1000000
iteration = 100


def list_comprehension(iteration):
    return [i for i in range(range_to)]


def list_comprehension_by_generator(iteration):
    return list(i for i in range(range_to))


def tuple_comprehension_by_generator(iteration):
    return tuple(i for i in range(range_to))


def tuple_by_list_comprehension(iteration):
    return tuple(i for i in range(range_to))


def generator_comprehension(iteration):
    return tuple(i for i in range(range_to))


def main(iteration=iteration):
    functions = (
        'list_comprehension',
        'list_comprehension_by_generator',
        'tuple_comprehension_by_generator',
        'tuple_by_list_comprehension',
        'generator_comprehension'
    )
    for function in functions:
        print(f'{function}:', timeit.Timer(
            'f(iteration)',
            f'from __main__ import iteration,{function} as f'
        ).timeit(iteration))


if __name__ == '__main__':
    main()
