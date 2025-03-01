from typing import List, Tuple


def get_neighbours(matrix: List[List[int]], row: int, col: int) -> List[int]:
    result = []
    if row != 0:
        result.append(matrix[row - 1][col])
    if row != len(matrix) - 1:
        result.append(matrix[row + 1][col])
    if col != 0:
        result.append(matrix[row][col - 1])
    if col != len(matrix[0]) - 1:
        result.append(matrix[row][col + 1])
    result.sort()
    return result


def read_input() -> Tuple[List[List[int]], int, int]:
    n, m = int(input()), int(input())
    m = m
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().strip().split())))
    row, col = int(input()), int(input())
    return matrix, row, col


# matrix, row, col = read_input()
matrix, row, col = ((1, 2, 3), (0, 2, 6), (7, 4, 1), (2, 7, 0)), 3, 0
for i in matrix:
    print(i)

print(" ".join(map(str, get_neighbours(matrix, row, col))))
