from typing import Tuple


def get_excessive_letter(shorter: str, longer: str) -> str:
    for char in longer:
        if char not in shorter:
            return char
        shorter = shorter.replace(char, '', 1)
    return None


def read_input() -> Tuple[str, str]:
    shorter = input().strip()
    longer = input().strip()
    return shorter, longer


shorter, longer = read_input()
print(get_excessive_letter(shorter, longer))
