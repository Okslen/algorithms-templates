def is_palindrome(line: str) -> bool:
    table = str.maketrans('ab', 'ab', """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ """,)
    line = line.lower().translate(table)
    return line == line[::-1]


print(is_palindrome('zo'.strip(',')))
