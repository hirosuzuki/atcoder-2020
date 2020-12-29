H, W= [int(_) for _ in input().split()]
S = [input() for _ in range(H)]

import sys
sys.setrecursionlimit(1000)

def solve(H, W, S):

    SL = sum(r.count("#") for r in S)

    result = []

    def solve_sub(xs):
        if len(xs) == SL:
            #print(xs)
            nonlocal result
            result = xs
        sy, sx = xs[-1]
        for dy, dx in ((-1, 0), (+1, 0), (0, -1), (0, +1)):
            ny, nx = sy + dy, sx + dx
            if 0 <= ny < H and 0 <= nx < W and S[ny][nx] == "#" and (ny, nx) not in xs:
                solve_sub(xs + [(ny, nx)])

    for y in range(H):
        for x in range(W):
            if S[y][x] == "#":
                solve_sub([(y, x)])
                if result:
                    return result

    return result

result = solve(H, W, S)

print(len(result))
for y, x in result:
    print(y+1, x+1)
