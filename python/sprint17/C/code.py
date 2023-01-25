import sys

LEN_STR = 150000
SUBSEQ = input()
SEQ = input()


def is_subseq(find_start: int = 0, subseq_index: int = 0) -> bool:
    if subseq_index == len(SUBSEQ):
        return True
    find_start = SEQ.find(SUBSEQ[subseq_index], find_start) + 1
    if find_start == 0:
        return False
    return is_subseq(find_start, subseq_index + 1)


if __name__ == '__main__':
    sys.setrecursionlimit(LEN_STR)
    print(is_subseq())
