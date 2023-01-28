from typing import Dict, List


def quick_sort_wardrobe(arr: List[int],
                        colors: Dict[int, str]
                        ) -> List[int]:
    colors_count = [0] * len(colors)
    for color in arr:
        colors_count[color] += 1
    result = []
    for i in range(len(colors_count)):
        result.extend([i]*colors_count[i])
    return result


def read_input() -> List[int]:
    _ = input()
    return [int(i) for i in input().strip().split()]


if __name__ == '__main__':
    COLORS = {0: 'pink', 1: 'yellow', 2: 'raspberry'}
    print(*quick_sort_wardrobe(read_input(), COLORS))
