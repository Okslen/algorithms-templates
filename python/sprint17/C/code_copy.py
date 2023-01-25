def is_subseq(subseq: str, seq: str, n: int = 0) -> bool:
    for letter in subseq:
        n = seq.find(letter, n) + 1
        if n == 0:
            return False
    return True


if __name__ == '__main__':
    subseq, seq = input(), input()
    print(is_subseq(subseq, seq))
