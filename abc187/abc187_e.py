from typing import List, DefaultDict, Set, Tuple, Deque
from collections import defaultdict, deque

import sys
sys.setrecursionlimit(300000)

N = int(input())
AB = [[int(_) for _ in input().split()] for _ in range(N - 1)]
Q = int(input())
TEX = [[int(_) for _ in input().split()] for _ in range(Q)]

def solve(N: int, AB: List[List[int]], Q: int, TEX: List[List[int]]):
    es: DefaultDict[int, Set[int]] = defaultdict(set)
    for a, b in AB:
        es[a].add(b)
        es[b].add(a)

    ds: List[int] = [-1] * (N + 1)
    q: Deque[Tuple[int, int]] = deque()
    q.append((1, 0))
    while q:
        n, depth = q.popleft()
        ds[n] = depth
        for e in es[n]:
            if ds[e] < 0:
                q.append((e, depth + 1))

    adds: DefaultDict[int, int] = defaultdict(int)
    for t, e, x in TEX:
        a, b = AB[e - 1]
        if t == 1:
            if ds[a] < ds[b]:
                adds[1] += x
                adds[b] -= x
            else:
                adds[a] += x
        elif t == 2:
            if ds[a] < ds[b]:
                adds[b] += x
            else:
                adds[1] += x
                adds[a] -= x
    
    rs: List[int] = [-1] * (N + 1)
    q: Deque[Tuple[int, int]] = deque()
    q.append((1, 0))
    while q:
        n, value = q.popleft()
        rs[n] = value + adds[n]
        for e in es[n]:
            if rs[e] < 0:
                q.append((e, rs[n]))

    for r in rs[1:]:
        print(r)

    return

solve(N, AB, Q, TEX)
