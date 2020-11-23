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
        for dy in (-1, +1):
            cy = y
            while 1:
                cy += dy
                csy = cs[cy]
                if csy[x] != 0:
                    break
                result += 1
                csy[x] = 1

    #print(cs)

    for i in range(N):
        y, x = AB[i]
        csy = cs[y]
        if (csy[x] & 2) == 2:
            continue
        result += (csy[x] == 0)
        csy[x] |= 2
        for dx in (-1, +1):
            cx = x
            while 1:
                cx += dx
                if csy[cx] == Z:
                    break
                result += (csy[cx] == 0)
                csy[cx] |= 2

    #print(cs)

    return result

result = solve(H, W, N, M, AB, CD)
print(result)
