from typing import List

N, M = [int(_) for _ in input().split()]
AB = [[int(_) for _ in input().split()] for _ in range(M)]
K = int(input())
CD = [[int(_) for _ in input().split()] for _ in range(K)]

def solve(N: int, M: int, AB: List[List[int]], K: int, CD: List[List[int]]):
    result = 0
    for i in range(2**K):
        ds = [0] * (N + 1)
        for j in range(K):
            if (1<<j) & i:
                ds[CD[j][0]] += 1
            else:
                ds[CD[j][1]] += 1
        r = 0
        for a, b in AB:
            if ds[a] > 0 and ds[b] > 0:
                r += 1
        #print(i, ds, r)
        result = max(result, r)
    print(result)

solve(N, M, AB, K, CD)
