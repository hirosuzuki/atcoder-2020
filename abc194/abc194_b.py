from typing import List

N = int(input())
AB = [[int(_) for _ in input().split()] for _ in range(N)]

def solve(N: int, AB: List[List[int]]):
    iab = [(i, AB[i][0], AB[i][1]) for i in range(N)]
    sa = sorted(iab, key=lambda x:x[1])
    sb = sorted(iab, key=lambda x:x[2])
    #print(iab)
    #print(sa)
    #print(sb)
    if sa[0][0] != sb[0][0]:
        result = max(sa[0][1], sb[0][2])
    else:
        result = min(sa[0][1] + sb[0][2], max(sa[0][1], sb[1][2]), max(sa[1][1], sb[0][2]))
    print(result)

solve(N, AB)
