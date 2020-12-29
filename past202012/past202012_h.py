H, W = [int(_) for _ in input().split()]
R, C = [int(_) for _ in input().split()]
S = [input() for _ in range(H)]

import sys
sys.setrecursionlimit(70000)
from collections import deque

def solve0(H, W, R, C, S):
    rs = [["#" if c == "#" else "x" for c in r] for r in S]

    def solve_sub(sy, sx):
        rs[sy][sx] = "o"
        for dy, dx, dc in ((-1, 0, "v"), (+1, 0, "^"), (0, -1, ">"), (0, +1, "<")):
            y, x = sy + dy, sx + dx
            if 0 <= y < H and 0 <= x < W and rs[y][x] == "x":
                c = S[y][x]
                if c == "." or c == dc:
                    solve_sub(y, x)

    solve_sub(R - 1, C - 1)

    for r in rs:
        print("".join(r))


def solve1(H, W, R, C, S):
    rs = [["#" if c == "#" else "x" for c in r] for r in S]

    q = deque()
    q.append((R - 1, C - 1))
    while q:
        sy, sx = q.popleft()
        if rs[sy][sx] != "o":
            rs[sy][sx] = "o"
            for dy, dx, dc in ((-1, 0, "v"), (+1, 0, "^"), (0, -1, ">"), (0, +1, "<")):
                y, x = sy + dy, sx + dx
                if 0 <= y < H and 0 <= x < W and rs[y][x] == "x":
                    c = S[y][x]
                    if c == "." or c == dc:
                        q.append((y, x))

    for r in rs:
        print("".join(r))

solve1(H, W, R, C, S)

