from typing import List, Set, Dict

N, M = [int(_) for _ in input().split()]
A = [int(_) for _ in input().split()]
XY = [[int(_) for _ in input().split()] for _ in range(M)]

def solve(N: int, M: int, A: List[int], XY: List[List[int]]):
    rs: Dict[int, Set[int]] = {}
    for x, y in XY:
        if x not in rs:
            rs[x] = set()
        rs[x].add(y)
    #print(rs)
    result = -10**20
    dp: List[int] = [10**20] * N
    for i in range(N):
        r = A[i] - dp[i]
        result = max(result, r)
        if (i + 1) in rs:
            for r in rs[i + 1]:
                j = r - 1
                dp[j] = min(dp[j], dp[i], A[i])
        #print(i, dp)
    print(result)

solve(N, M, A, XY)
