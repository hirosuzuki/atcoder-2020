from typing import List

H, W = [int(_) for _ in input().split()]
A = [[int(_) for _ in input().split()] for _ in range(H)]

def solve(H: int, W: int, A: List[List[int]]):
    minv = min(r for row in A for r in row)
    result = sum(r - minv for row in A for r in row)
    print(result)

solve(H, W, A)

