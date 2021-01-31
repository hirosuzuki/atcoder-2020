from typing import List

import sys
sys.setrecursionlimit(20000)

N = int(input())
A = [input() for _ in range(N)]

def solve(N: int, A: List[str]):
    x, y = 1, 1
    for c in A:
        if c == "AND":
            x, y = x + x + y, y
        elif c == "OR":
            x, y = x, x + y + y
    print(y)

solve(N, A)
