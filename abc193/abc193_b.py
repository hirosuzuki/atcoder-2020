from typing import List

N = int(input())
APX = [[int(_) for _ in input().split()] for _ in range(N)]

def solve(N: int, APX: List[List[int]]):
    result = -1
    for a, p, x in APX:
        if x > a:
            if result == -1 or result > p:
                result = p
    print(result)

solve(N, APX)

