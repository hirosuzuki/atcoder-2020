from typing import List, DefaultDict, Set
from collections import defaultdict

N, M = [int(_) for _ in input().split()]
AB = [[int(_) for _ in input().split()] for _ in range(M)]

def solve(N: int, M: int, AB: List[List[int]]):

    es: DefaultDict[int, Set[int]] = defaultdict(set)
    ebs: List[int] = [0] * (N + 1)
    for a, b in AB:
        es[a].add(b)
        es[b].add(a)
        ebs[a] |= 1 << (b - 1)
        ebs[b] |= 1 << (a - 1)
    #print(es)
    #print(ebs)

    fs: List[int] = [0] * (2**N)
    for i in range(1, 2**N):
        l = i.bit_length()
        j = i ^ (1 << (l - 1))
        if j == 0:
            fs[i] = 1
            continue
        #if fs[j] and all(k in es[l] for k in range(1, l) if j & (1 << (k - 1))):
        if fs[j] and ((ebs[l] & j) == j):
            fs[i] = 1
    #print(fs)

    INF = 1000000000000000000000000000
    rs: List[int] = [INF] * (2**N)

    rs[0] = 0
    for i in range(1, 2**N):
        if fs[i]:
            rs[i] = 1

    #print(rs)

    for i in range(1, 2**N):
        r = INF
        j = i
        while j:
            v = rs[j] + rs[i^j]
            r = min(r, v)
            j -= 1
            j &= i
        rs[i] = r

    print(rs[-1])

solve(N, M, AB)
