from typing import List

N, X = [int(_) for _ in input().split()]
VP = [[int(_) for _ in input().split()] for _ in range(N)]

def solve(N: int, X: int, VP: List[List[int]]):
    t = 0
    i = 0
    for v, p in VP:
        i += 1
        t += v * p
        if t > X * 100:
            print(i)
            return
    print(-1)

solve(N, X, VP)
