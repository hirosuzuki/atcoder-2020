#from typing import Dict
from functools import lru_cache

import sys
sys.setrecursionlimit(100000)

X, Y = [int(_) for _ in input().split()]

def solve(X: int, Y: int):

    @lru_cache(maxsize = 1000000)
    def calc(y: int) -> int:
        r = abs(X - y)
        if y == 1:
            return r
        elif y % 2 == 1:
            return min(r, calc((y + 1) // 2) + 2, calc((y - 1) // 2) + 2)
        else:
            return min(r, calc(y // 2) + 1)
    
    print(calc(Y))

solve(X, Y)
