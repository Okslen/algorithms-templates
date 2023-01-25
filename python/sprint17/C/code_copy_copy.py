def is_subseq(subseq: str, seq: str) -> bool:
    position = -1
    for letter in subseq:
        position = seq.find(letter, position + 1)
        if position == - 1:
            return False
    return True


if __name__ == '__main__':
    subseq, seq = input(), input()
    print(is_subseq(subseq, seq))
