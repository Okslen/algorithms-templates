def get_longest_word(line: str) -> str:
    line = line.split()
    longest_word = line[0]
    len_longest_word = len(longest_word)
    for word in line:
        len_word = len(word)
        if len_word > len_longest_word:
            longest_word = word
            len_longest_word = len_word
    return longest_word


def read_input() -> str:
    # _ = input()
    # line = input().strip()
    line = 'i love segment tree'.strip()
    return line


def print_result(result: str) -> None:
    print(result)
    print(len(result))


print_result(get_longest_word(read_input()))
