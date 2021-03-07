from typing import List

N, M = [int(_) for _ in input().split()]
A = [int(_) for _ in input().split()]

def solve(N: int, M: int, A: List[int]):

    ns = [-1] * 1500001
    ms = [0] * 1500001
    for i in range(N):
        x = A[i]
        ms[x] = max(ms[x], i - ns[x])
        ns[x] = i
    
    i = N
    for x in range(1500001):
        ms[x] = max(ms[x], i - ns[x])

    #print(ns[:10])
    #print(ms[:10])

    result = 0
    while ms[result] <= M:
        result += 1

    print(result)

solve(N, M, A)
