H, W, N, M = [int(_) for _ in input().split()]
AB = [[int(_) for _ in input().split()] for _ in range(N)]
CD = [[int(_) for _ in input().split()] for _ in range(M)]

def solve(H, W, N, M, AB, CD):
    cs = [[0] * (W + 2) for i in range(H + 2)]
    Z = 3
    for y in range(H + 2):
        cs[y][0] = Z
        cs[y][W + 1] = Z
    for x in range(W + 2):
        cs[0][x] = Z
        cs[H + 1][x] = Z
    for i in range(M):
        cs[CD[i][0]][CD[i][1]] = Z

    #print(cs)

    result = 0

    for i in range(N):
        y, x = AB[i]
        if cs[y][x] != 0:
            continue
        result += 1
        cs[y][x] = 1
        for dy, dx in ((0, -1), (0, +1)):
            cy, cx = y, x
            while 1:
                cy += dy
                cx += dx
                if cs[cy][cx] != 0:
                    break
                result += 1
                cs[cy][cx] = 1

    #print(cs)

    for i in range(N):
        y, x = AB[i]
        if (cs[y][x] & 2) == 2:
            continue
        result += (cs[y][x] == 0)
        cs[y][x] |= 2
        for dy, dx in ((-1, 0), (+1, 0)):
            cy, cx = y, x
            while 1:
                cy += dy
                cx += dx
                if cs[cy][cx] == Z:
                    break
                result += (cs[cy][cx] == 0)
                cs[cy][cx] |= 2

    #print(cs)

    return result

result = solve(H, W, N, M, AB, CD)
print(result)
