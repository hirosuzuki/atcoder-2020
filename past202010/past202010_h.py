N, M, K = [int(_) for _ in input().split()]
S = [input() for _ in range(N)]

def solve(N, M, K, S):
    result = 0
    for n in range(1, min(N, M) + 1):
        for y in range(0, N - n + 1):
            for x in range(0, M - n + 1):
                cs = [0] * 10
                for i in range(y,y+n):
                    for j in range(x,x+n):
                        cs[int(S[i][j])] += 1
                csmax = max(cs)
                # print(n, y, x, cs, csmax)
                if csmax + K >= n * n:
                    result = n
                    break
            if result == n:
                break
        if result < n:
            break
    return result

print(solve(N, M, K, S))
