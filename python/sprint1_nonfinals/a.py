def evaluate_function(a: int, b: int, c: int, x: int) -> int:
    return x*(a*x+b)+c


a, x, b, c = map(int, input().strip().split())
print(evaluate_function(a, b, c, x))
