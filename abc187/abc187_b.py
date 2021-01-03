from typing import List

N = int(input())
XY = [[int(_) for _ in input().split()] for _ in range(N)]

def solve(N: int, XY: List[List[int]]):
    result = 0
    for i in range(N):
        for j in range(i + 1, N):
            x1, y1 = XY[i]
            x2, y2 = XY[j]
            if abs(y2 - y1) <= abs(x2 - x1):
                result += 1            
    print(result)

solve(N, XY)
