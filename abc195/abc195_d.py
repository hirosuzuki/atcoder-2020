from typing import List

N, M, Q = [int(_) for _ in input().split()]
WV = [[int(_) for _ in input().split()] for _ in range(N)]
X = [int(_) for _ in input().split()]
Query = [[int(_) for _ in input().split()] for _ in range(Q)]

def solve(N: int, M: int, Q: int, WV: List[List[int]], X: List[int], Query: List[List[int]]):
    WV.sort(key=lambda x:(x[1], -x[0]), reverse=True)
    #print(WV)
    for q in Query:
        xs = X[:q[0] - 1] + X[q[1]:]
        xs.sort()
        r = 0
        for w, v in WV:
            for i in range(len(xs)):
                if xs[i] >= w:
                    r += v
                    xs[i] = 0
                    break
        print(r)

solve(N, M, Q, WV, X, Query)
