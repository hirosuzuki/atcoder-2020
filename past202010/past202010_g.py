N, M = [int(_) for _ in input().split()]
S = [input() for i in range(N)]

def calc(N, M, S, c, y, x):
    if S[y][x] == ".":
        return False
    cs = [[0] * M for i in range(N)]
    h = []
    cs[y][x] == 1
    h.append((y, x))
    cnt = 0
    while h:
        sy, sx = h.pop()
        for dy, dx in ((0, -1), (0, +1), (-1, 0), (+1, 0)):
            ty, tx = sy + dy, sx + dx
            if 0 <= ty < N and 0 <= tx < M and S[ty][tx] == "." and cs[ty][tx] == 0:
                cs[ty][tx] = 1
                h.append((ty, tx))
                cnt += 1
    return cnt == c

def solve(N, M, S):
    result = 0
    c = sum([r.count(".") for r in S])
    for y in range(N):
        for x in range(M):
            if calc(N, M, S, c, y, x):
                result += 1
    return result

print(solve(N, M, S))

