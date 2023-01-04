def transposition(matrix):
    return zip(*matrix)


if __name__ == '__main__':

    def read_input():
        row_count = int(input())
        _ = int(input())
        return (input().strip().split() for _ in range(row_count))

    for row in transposition(read_input()):
        print(*row)
