T = int(input())
NAB = [[int(_) for _ in input().split()] for _ in range(T)]

M = 1000000007


def calc(n: int, a: int, b: int) -> int:
    t = n - a - b
    x4 = (t + 1) * (t + 2) // 2 if t >= 0 else 0
    x3 = x4 * 2
    x2 = (n - a + 1) * (n - b + 1) - x3
    x1 = x2 * x2
    result = (n - a + 1) ** 2 * (n - b + 1) ** 2 - x1
    return result % M


for n, a, b in NAB:
    print(calc(n, a, b))
