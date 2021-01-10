from typing import List, Dict

N, C = [int(_) for _ in input().split()]
ABC = [[int(_) for _ in input().split()] for _ in range(N)]

def solve(N: int, C: int, ABC: List[List[int]]):
    xs: Dict[int, int] = {}
    for a, b, c in ABC:
        if a not in xs:
            xs[a] = 0
        xs[a] += c
        if (b + 1) not in xs:
            xs[b + 1] = 0
        xs[b + 1] -= c
    result = 0
    t = 0
    c = 0
    for k in sorted(xs):
        result += (k - t) * min(c, C)
        c += xs[k]
        t = k
    print(result)

solve(N, C, ABC)
