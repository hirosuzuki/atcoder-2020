from typing import List, Tuple, DefaultDict, Set
from collections import defaultdict
from heapq import heappop, heappush

N, M, X, Y = [int(_) for _ in input().split()]
ABTK = [[int(_) for _ in input().split()] for _ in range(M)]

def solve(N: int, M: int, X: int, Y: int, ABTK: List[List[int]]):
    ds: DefaultDict[int, Set[Tuple[int, int, int]]] = defaultdict(lambda:set())
    for a, b, t, k in ABTK:
        ds[a].add((b, t, k))
        ds[b].add((a, t, k))
    tmax = 10**18
    ts = [tmax] * (N + 1)
    h = []
    heappush(h, (0, X))
    while h:
        t, y = heappop(h)
        if ts[y] <= t:
            continue
        ts[y] = t
        for z, zt, zk in ds[y]:
            ztt = (t + zk - 1) // zk * zk + zt
            if ts[z] > ztt:
                heappush(h, (ztt, z))
    #print(ts)
    if ts[Y] == tmax:
        print(-1)
    else:
        print(ts[Y])
    return

solve(N, M, X, Y, ABTK)
