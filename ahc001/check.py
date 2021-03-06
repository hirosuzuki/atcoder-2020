from typing import List, Tuple, Dict

from sys import setrecursionlimit, argv
setrecursionlimit(100000)

N = int(input())
XYR = [[int(_) for _ in input().split()] for _ in range(N)]
ABCD = [[int(_) for _ in input().split()] for _ in range(N)]

def solve(N: int, XYR: List[List[int]], ABCD: List[List[int]]):

    err = False

    for i in range(N):
       for j in range(i + 1, N):
           x0 = (ABCD[i][0] + ABCD[i][2])
           y0 = (ABCD[i][1] + ABCD[i][3])
           x1 = (ABCD[j][0] + ABCD[j][2])
           y1 = (ABCD[j][1] + ABCD[j][3])
           w0 = ABCD[i][2] - ABCD[i][0]
           h0 = ABCD[i][3] - ABCD[i][1]
           w1 = ABCD[j][2] - ABCD[j][0]
           h1 = ABCD[j][3] - ABCD[j][1]
           if abs(x0 - x1) < w0 + w1 and abs(y0 - y1) < h0 + h1:
               print("Error: Too Close", i, j)
               err = True

    ss = 0
    for i in range(N):
        x, y, r = XYR[i]
        a, b, c, d = ABCD[i]
        if a <= x < c and b <= y < d:
            l = (c - a) * (d - b)
            s = min(r, l) / max(r, l)
            ss += 1 - (1 - s) ** 2
            print(i, s)
        else:
            print("Error: No in", i)
            err = True

    if err == False:
        print("No Err")
        print("Score:", ss / N)

solve(N, XYR, ABCD)
