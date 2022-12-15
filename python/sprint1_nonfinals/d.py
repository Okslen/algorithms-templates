from typing import List


def get_weather_randomness(n: int, temperatures: List[int]) -> int:
    count = 0
    temperatures.append(-274)
    i = 0
    current_day = temperatures[0]
    is_yesterday_colder = True
    while i < n:
        next_day = temperatures[i + 1]
        is_tommorom_colder = current_day > next_day

        if not is_tommorom_colder:
            if current_day == next_day:
                is_yesterday_colder = is_tommorom_colder
            else:
                is_yesterday_colder = not is_tommorom_colder
        else:
            if is_yesterday_colder:
                count += 1
                is_yesterday_colder = not is_tommorom_colder
        current_day = next_day
        i += 1
    return count


def read_input() -> List[int]:
    # n = int(input())
    # n = n
    # temperatures = list(map(int, input().strip().split()))
    n = 10
    temperatures = list(map(
        int, '-159 -248 8 -23 -45 -131 -169 -184 159 -241'.strip().split()))
    return n, temperatures


n, temperatures = read_input()
print(get_weather_randomness(n, temperatures))
