from typing import List, Tuple

import sys
sys.setrecursionlimit(20000)

N = int(input())
XY = [[int(_) for _ in input().split()] for _ in range(N)]
M = int(input())
OP = [[int(_) for _ in input().split()] for _ in range(M)]
Q = int(input())
AB = [[int(_) for _ in input().split()] for _ in range(Q)]

def solve(N: int, A: List[List[int]], M: int, OP: List[List[int]], Q: int, AB: List[List[int]]):
    c: Tuple[int, int, int, int, int, int, int, int, int] = (
        1, 0, 0,
        0, 1, 0,
        0, 0, 1
    )
    cs: List[Tuple[int, int, int, int, int, int, int, int, int]] = [c]
    for o in OP:
        t: Tuple[int, int, int, int, int, int, int, int, int] = (
            1, 0, 0,
            0, 1, 0,
            0, 0, 1
        )
        if o[0] == 1:
            t: Tuple[int, int, int, int, int, int, int, int, int] = (
                0, -1, 0,
                1, 0, 0,
                0, 0, 1
            )
        elif o[0] == 2:
            t: Tuple[int, int, int, int, int, int, int, int, int] = (
                0, 1, 0,
                -1, 0, 0,
                0, 0, 1
            )
        elif o[0] == 3:
            t: Tuple[int, int, int, int, int, int, int, int, int] = (
                -1, 0, 0,
                0, 1, 0,
                2 * o[1], 0, 1
            )
        elif o[0] == 4:
            t: Tuple[int, int, int, int, int, int, int, int, int] = (
                1, 0, 0,
                0, -1, 0,
                0, 2 * o[1], 1
            )
        c: Tuple[int, int, int, int, int, int, int, int, int] = (
            c[0] * t[0] + c[1] * t[3] + c[2] * t[6],
            c[0] * t[1] + c[1] * t[4] + c[2] * t[7],
            c[0] * t[2] + c[1] * t[5] + c[2] * t[8],
            c[3] * t[0] + c[4] * t[3] + c[5] * t[6],
            c[3] * t[1] + c[4] * t[4] + c[5] * t[7],
            c[3] * t[2] + c[4] * t[5] + c[5] * t[8],
            c[6] * t[0] + c[7] * t[3] + c[8] * t[6],
            c[6] * t[1] + c[7] * t[4] + c[8] * t[7],
            c[6] * t[2] + c[7] * t[5] + c[8] * t[8],
        )
        cs.append(c)

    for a, b in AB:
        sx, sy = A[b - 1]
        c = cs[a]
        x = c[0] * sx + c[3] * sy + c[6]
        y = c[1] * sx + c[4] * sy + c[7]
        print(x, y)

    return

solve(N, XY, M, OP, Q, AB)
