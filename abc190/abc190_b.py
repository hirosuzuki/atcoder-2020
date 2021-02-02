from typing import List

N, S, D = [int(_) for _ in input().split()]
XY = [[int(_) for _ in input().split()] for _ in range(N)]

def solve(N: int, S: int, D: int, XY: List[List[int]]):
    for x, y in XY:
        if x < S and y > D:
            print("Yes")
            return
    print("No")

solve(N, S, D, XY)
