N, M, K = [int(_) for _ in input().split()]
H = [int(_) for _ in input().split()]
C = [int(_) for _ in input().split()]
AB = [[int(_) for _ in input().split()] for _ in range(M)]

from collections import defaultdict
from heapq import *
import heapq

MX = 10**5

def solve(N, M, K, H, C, AB):
    rs = [MX] * (N + 1)

    d = defaultdict(set)
    for a, b in AB:
        if H[b-1] > H[a-1]:
            d[a].add(b)
        if H[a-1] > H[b-1]:
            d[b].add(a)

    h = []
    for x in C:
        heappush(h, (0, x))

    while h:
        n, k = heappop(h)
        if rs[k] > n:
            rs[k] = n
            for y in d[k]:
                if rs[y] > n + 1:
                    heappush(h, (n + 1, y))

    for r in rs[1:]:
        print(r if r < MX else -1)

solve(N, M, K, H, C, AB)
